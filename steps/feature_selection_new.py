FEATURES = [
    "sms_in_cnt_std_total",
    "casual_act_count",
    "loc_market_share",
    "imei_mean_days_usage",
    "SUM_of_Count_events_susp_app_sum",
    "voice_mts_in_dwork_part_mea_mnt3",
    "num_act_days_std_total",
    "voice_out_td_cnt_std_total",
    "MV_dou_net",
    "non_accum_internet_vol_td_total",
    "voice_in_td_cnt_td_mnt3",
    "MAX_of_day_cnt_susp_app_sum",
    "data_3g_tv_cnt_std_mnt3",
    "content_cnt_mea_diff",
    "days_of_end_last_ppm",
    "num_act_days_min_total",
    "num_act_days_mea_mnt3",
    "Balance_uah",
    "sum_paym_6_month",
    "day_end_gba",
    "sms_in_cnt_max_total",
    "voice_in_tar_dur_min_mnt1",
    "voice_mts_in_dwork_part_mea_total",
    "other_cnt_sms_in_sum",
    "voice_in_tar_dur_min_total",
    "num_act_days_td_total",
    "all_cnt_std_mnt3",
    "all_cnt_mea_diff",
    "non_accum_internet_vol_mea_diff",
    "sms_in_cnt_mea_total",
    "casual_topic_cnt_sms_in_sum",
    "num_act_days_min_mnt3",
    "num_act_days_std_mnt3",
    "num_act_days_mea_total",
    "voice_mts_in_drest_part_mea_total",
    "bank_companies_cnt_sms_in_sum_share",
    "data_3g_tv_cnt_max_total",
    "voice_mts_in_dwork_part_std_total",
    "days_of_last_ppm",
    "all_cnt_std_total",
    "all_cnt_std_mnt1",
    "lt",
    "num_act_days_min_mnt1",
    "sms_in_cnt_mea_mnt3",
    "num_act_days_mea_mnt1",
    "loc_is_obl_center",
    "device_days_usage",
    "conn_in_uniq_cnt_mea_total",
    "content_cnt_mea_mnt3",
]


def feature_selection_new(dataframe):
    return dataframe[FEATURES + ["target", "abon_id"]]
