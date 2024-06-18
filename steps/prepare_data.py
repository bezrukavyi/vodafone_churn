import pickle
from steps.set_missings import set_missings
from utils.helpers import reduce_mem_usage
from steps.load_data import load_train_data, load_test_data
from steps.feature_selection import feature_selection
from utils.pipeline import Pipeline, PipelineStep
import sklearn


load_train_data_step = PipelineStep("load_train_data", load_train_data)
load_test_data_step = PipelineStep("load_test_data", load_test_data)
set_missings_step = PipelineStep("set_missings", set_missings)
reduce_mem_usage_step = PipelineStep("reduce_mem_usage", reduce_mem_usage)
feature_selection_step = PipelineStep("feature_selection", feature_selection)


# Main Transform Pipeline
transform_pipeline = Pipeline(
    "TRANSFORM",
    [
        set_missings_step,
        reduce_mem_usage_step,
        feature_selection_step,
    ],
)


def process_train_data():
    print("Processing train data...")
    transformed_train_data = transform_pipeline.run(load_train_data(None))

    print("Shape:", transformed_train_data.shape)
    print("Columns:", transformed_train_data.columns)

    save_pickle_data("cache/transformed_train_data.pkl", transformed_train_data)


def process_test_data():
    print("Processing test data...")
    transformed_test_data = transform_pipeline.run(load_test_data(None))

    print("Shape:", transformed_test_data.shape)
    print("Columns:", transformed_test_data.columns)

    save_pickle_data("cache/transformed_test_data.pkl", transformed_test_data)


def save_pickle_data(name, data):
    with open(name, "wb") as f:
        pickle.dump(data, f)

    return data


def load_split_processed_data():
    with open("cache/transformed_train_data.pkl", "rb") as f:
        train_data = pickle.load(f)

    with open("cache/transformed_test_data.pkl", "rb") as f:
        test_data = pickle.load(f)

    return (train_data, test_data)


def load_processed_data():
    with open("cache/processed_data.pkl", "rb") as f:
        data = pickle.load(f)

    return data


def process_data():
    train_data_pipeline = Pipeline(
        "train",
        [
            load_train_data_step,
            set_missings_step,
        ],
    )

    test_data_pipeline = Pipeline(
        "test",
        [
            load_test_data_step,
            set_missings_step,
        ],
    )

    train_data = train_data_pipeline.run()
    test_data = test_data_pipeline.run()

    save_pickle_data("cache/processed_data.pkl", (train_data, test_data))

    return train_data, test_data
