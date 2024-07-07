import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import json
import optuna
from utils.helpers import create_or_load_optuna_study
from utils.model import save_model
import lightgbm as lgb
import numpy as np
import sklearn.datasets
import sklearn.metrics
from imblearn.over_sampling import SMOTE
from steps.prepare_data import load_split_processed_data, process_train_data, process_test_data
import sklearn
import random
from sklearn.model_selection import train_test_split, KFold
import warnings
import pdb
from imblearn.under_sampling import RandomUnderSampler
import pickle

warnings.filterwarnings("ignore")

SEED = 42
np.random.seed(SEED)
random.seed(SEED)

version = "fixing_overfitting_v15"

with open("cache/train_data_pipeline.pkl", "rb") as f:
    train_data = pickle.load(f)

print("Train data shape:", train_data.shape)


def oversampling(train_data, size=0.6):
    train_x = train_data.drop(columns="target")
    train_y = train_data.target

    not_churn_data_count = train_data[train_data.target == 0].shape[0]

    not_churn_count_strategy = int(not_churn_data_count * size)
    churn_count_strategy = int(not_churn_data_count * size)

    rus = RandomUnderSampler(random_state=SEED, sampling_strategy={0: not_churn_count_strategy})
    train_x, train_y = rus.fit_resample(train_x, train_y)

    smote = SMOTE(random_state=SEED, sampling_strategy={0: not_churn_count_strategy, 1: churn_count_strategy})
    resampled_x, resampled_y = smote.fit_resample(train_x, train_y)

    return resampled_x, resampled_y


sub_train_x, sub_val_x, sub_train_y, sub_val_y = train_test_split(
    train_data.drop(columns="target"),
    train_data.target,
    test_size=0.2,
    random_state=SEED,
)

sub_train_data = sub_train_x
sub_train_data["target"] = sub_train_y

resampled_x, resampled_y = oversampling(sub_train_data, size=0.6)

static_params = {
    "random_state": SEED,
    "seed": SEED,
    "objective": "binary",
    "metric": "auc",
    "verbosity": -1,
    "boosting_type": "gbdt",
    "feature_pre_filter": False,
    # "early_stopping_rounds": 100,
    "n_jobs": -1,
}


def objective(trial):
    params = {
        **static_params,
        "lambda_l1": trial.suggest_int("lambda_l1", 5, 15),
        "lambda_l2": trial.suggest_int("lambda_l2", 5, 15),
        "learning_rate": trial.suggest_categorical(
            "learning_rate", [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
        ),
        "num_leaves": trial.suggest_int("num_leaves", 50, 100, step=5),
        "feature_fraction": trial.suggest_float("feature_fraction", 0.2, 1.0),
        "bagging_fraction": trial.suggest_float("bagging_fraction", 0.2, 1.0),
        "max_depth": trial.suggest_int("max_depth", 9, 15),
        "min_child_samples": trial.suggest_int("min_child_samples", 10, 150, step=10),
        "n_estimators": trial.suggest_int("n_estimators", 100, 400, step=50),
        "drop_rate": trial.suggest_categorical("drop_rate", [0.1, 0.2, 0.3, 0.4]),
    }

    print("Params:", params)

    f1_scores = []
    auc_scores = []

    model_cls = lgb.LGBMClassifier(**params)

    model_cls = model_cls.fit(resampled_x, resampled_y)

    threshold = 0.5

    train_X = sub_train_x[resampled_x.columns]
    train_y_true = sub_train_y

    train_y_pred_proba = model_cls.booster_.predict(train_X)
    train_y_pred = (train_y_pred_proba >= threshold).astype(int)

    train_roc_auc_score = sklearn.metrics.roc_auc_score(train_y_true, train_y_pred_proba)
    train_f1_score = sklearn.metrics.f1_score(train_y_true, train_y_pred, pos_label=1)

    auc_scores.append(train_roc_auc_score)
    f1_scores.append(train_f1_score)

    print("ROC AUC:", train_roc_auc_score, "F1 Score:", train_f1_score)

    val_X = sub_val_x[resampled_x.columns]
    val_y_true = sub_val_y

    val_y_pred_proba = model_cls.booster_.predict(sub_val_x)
    val_y_pred = (val_y_pred_proba >= threshold).astype(int)

    val_roc_auc_score = sklearn.metrics.roc_auc_score(sub_val_y, val_y_pred_proba)
    val_f1_score = sklearn.metrics.f1_score(sub_val_y, val_y_pred, pos_label=1)

    auc_scores.append(val_roc_auc_score)
    f1_scores.append(val_f1_score)

    print("VAL ROC AUC:", val_roc_auc_score, "VAL F1 Score:", val_f1_score)

    if val_roc_auc_score < 0.897:
        return -100

    return (
        0.7 * np.mean(auc_scores) + 0.3 * np.mean(f1_scores) - (10 * np.std(auc_scores)) - (10 * np.std(f1_scores))
    )


study_name = f"LightGbmV5_{version}"

study = optuna.create_study(
    study_name=study_name,
    storage="sqlite:///example.db",
    direction="maximize",
    load_if_exists=True,
)

try:
    study.optimize(objective, n_trials=1000)

finally:
    trial = study.best_trial

    model_params = {**static_params, **trial.params}

    print("Best params:", model_params)

    # save best params
    with open(f"parameters/{study_name}.json", "wb") as f:
        f.write(json.dumps(model_params).encode())

    print("Done!")
