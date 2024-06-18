FEATURES = [
    "voice_in_td_cnt_mea_mnt1",
    "lt",
    "num_act_days_td_mnt3",
    "num_act_days_min_mnt1",
    "voice_mts_in_dwork_part_mea_mnt1",
    "voice_out_td_cnt_td_mnt3",
    "voice_mts_in_dwork_part_max_mnt1",
    "all_cnt_std_mnt3",
    "all_cnt_min_mnt3",
    "device_days_usage",
    "imei_mean_long_days_usage",
    "num_act_days_std_mnt1",
    "voice_out_short_part_mea_mnt3",
    "Balance_uah",
    "sms_in_cnt_std_mnt3",
    "voice_in_mts_avg_dur_min_mnt3",
    "voice_mts_in_dwork_part_min_mnt3",
    "voice_in_td_cnt_td_mnt3",
    "voice_mts_in_drest_part_td_mnt3",
    "voice_in_tar_dur_min_mnt1",
    "voice_out_td_cnt_min_mnt3",
    "com_num_part_td_mnt3",
    "voice_mts_in_dwork_part_std_mnt1",
    "conn_com_part_min_mnt1",
    "voice_in_kievstar_part_std_mnt1",
    "tsoa_call_cnt",
    "num_act_days_mea_mnt3",
    "active_gba",
    "days_of_end_last_ppm",
    "myvf_day_usage",
    "voice_in_tar_dur_mea_wk1",
    "MV_dou_net",
    "voice_mts_out_dwork_partmea_mnt3",
    "voice_mts_in_nwork_part_mea_mnt1",
    "days_of_last_ppm",
    "num_act_days_max_mnt1",
    "voice_mts_in_dwork_part_max_mnt3",
    "voice_in_kievstar_part_max_mnt3",
    "voice_in_td_cnt_min_mnt1",
    "cnt_paym_6_month",
    "conn_com_part_max_mnt3",
    "abon_id",
    "loc_is_obl_center",
    "data_3g_tv_cnt_std_mnt3",
    "device_brand_other",
    "num_act_days_mea_mnt1",
    "voice_out_tar_dur_min_mnt3",
    "MV_DOU_AP",
    "non_accum_internet_vol_std_mnt3",
    "voice_in_kievstar_part_mea_mnt1",
    "loc_market_share",
    "voice_mts_out_nwork_partmin_mnt1",
    "data_3g_tv_cnt_std_mnt1",
    "sum_paym_6_month",
    "conn_in_uniq_cnt_td_mnt3",
    "num_act_days_mea_wk1",
    "num_act_days_min_mnt3",
    "voice_mts_out_dwork_partmax_mnt3",
    "device_height_mm",
    "active_ppm",
    "voice_mts_in_drest_part_mea_wk1",
    "day_end_gba",
    "ks_num_part_mea_wk1",
    "imei_mean_days_usage",
    "device_type_rus_other",
    "voice_mts_in_dwork_part_mea_mnt3",
    "device_has_lte",
    "non_accum_internet_vol_min_mnt3",
    "voice_mts_in_drest_part_mea_mnt1",
    "device_type_smartphone",
    "num_act_days_std_mnt3",
    "voice_mts_in_dwork_part_min_mnt1",
    "all_cnt_std_mnt1",
    "voice_in_life_part_mea_mnt3",
    "bs_count_ppm_mn3",
    "conn_com_part_max_mnt1",
    "voice_out_tar_dur_mea_wk1",
    "non_accum_internet_vol_mea_wk1",
    "device_type_phone",
    "content_cnt_mea_mnt3",
    "voice_mts_in_drest_part_std_mnt1",
    "gprs_tar_vol_std_mnt1",
    "gprs_tar_vol_min_mnt1",
    "voice_in_kievstar_part_max_mnt1",
    "device_brand_nan",
    "voice_mts_out_nrest_partmea_wk1",
    "device_sim_count",
    "device_android_version",
    "conn_out_uniq_cnt_mea_wk1",
    "MV_dou",
    "avg_paym_6_month",
]


def feature_selection(dataframe):
    return dataframe[FEATURES + ["target"]]


# report_LightGbmV1_p025_r080_090auc = [
#     "num_act_days_mea_mnt3",
#     "device_days_usage",
#     "num_act_days_std_mnt3",
#     "num_act_days_mea_mnt1",
#     "num_act_days_min_mnt3",
#     "loc_market_share",
#     "num_act_days_min_mnt1",
#     "lt",
#     "days_of_last_ppm",
#     "Balance_uah",
#     "day_end_gba",
#     "all_cnt_std_mnt1",
#     "sms_in_cnt_std_mnt3",
#     "content_cnt_mea_mnt3",
#     "voice_out_tar_dur_min_mnt3",
#     "device_has_lte",
#     "voice_in_tar_dur_min_mnt1",
#     "sum_paym_6_month",
#     "voice_in_td_cnt_td_mnt3",
#     "days_of_end_last_ppm",
#     "imei_mean_long_days_usage",
#     "voice_in_mts_avg_dur_min_mnt3",
#     "voice_out_short_part_mea_mnt3",
#     "all_cnt_std_mnt3",
#     "data_3g_tv_cnt_std_mnt3",
#     "all_cnt_min_mnt3",
#     "voice_in_kievstar_part_mea_mnt1",
#     "voice_mts_in_dwork_part_mea_mnt3",
#     "abon_id",
#     "voice_in_td_cnt_mea_mnt1",
#     "loc_is_obl_center",
#     "conn_out_uniq_cnt_mea_wk1",
#     "data_3g_tv_cnt_std_mnt1",
#     "voice_mts_in_dwork_part_max_mnt3",
#     "active_gba",
#     "voice_in_td_cnt_min_mnt1",
#     "device_brand_other",
#     "voice_out_td_cnt_min_mnt3",
#     "voice_out_td_cnt_td_mnt3",
#     "voice_mts_in_dwork_part_mea_mnt1",
#     "voice_mts_in_drest_part_mea_wk1",
#     "tsoa_call_cnt",
#     "imei_mean_days_usage",
#     "avg_paym_6_month",
#     "voice_out_tar_dur_mea_wk1",
#     "non_accum_internet_vol_std_mnt3",
# ]


# report_LightGbmV1_p041_r064_089auc = [
#     "num_act_days_min_mnt3",
#     "device_days_usage",
#     "loc_market_share",
#     "num_act_days_mea_mnt1",
#     "Balance_uah",
#     "lt",
#     "voice_out_tar_dur_min_mnt3",
#     "day_end_gba",
#     "num_act_days_mea_mnt3",
#     "days_of_last_ppm",
#     "num_act_days_min_mnt1",
#     "content_cnt_mea_mnt3",
#     "voice_mts_in_dwork_part_mea_mnt3",
#     "all_cnt_std_mnt1",
#     "all_cnt_min_mnt3",
#     "days_of_end_last_ppm",
#     "voice_out_short_part_mea_mnt3",
#     "imei_mean_days_usage",
#     "sms_in_cnt_std_mnt3",
#     "device_brand_other",
#     "imei_mean_long_days_usage",
#     "device_has_lte",
#     "voice_in_td_cnt_mea_mnt1",
#     "loc_is_obl_center",
#     "sum_paym_6_month",
#     "abon_id",
#     "voice_in_kievstar_part_mea_mnt1",
#     "voice_in_tar_dur_mea_wk1",
#     "non_accum_internet_vol_mea_wk1",
#     "voice_mts_out_dwork_partmea_mnt3",
#     "num_act_days_std_mnt3",
#     "voice_in_td_cnt_min_mnt1",
#     "voice_in_td_cnt_td_mnt3",
#     "data_3g_tv_cnt_std_mnt3",
#     "all_cnt_std_mnt3",
# ]


# report_LightGbmV2_p068_r033_090auc = [
#     "num_act_days_mea_mnt1",
#     "num_act_days_mea_wk1",
#     "device_brand_other",
#     "num_act_days_min_mnt3",
#     "active_ppm",
#     "device_has_lte",
#     "loc_market_share",
#     "num_act_days_min_mnt1",
#     "num_act_days_td_mnt3",
#     "voice_mts_in_drest_part_mea_wk1",
#     "voice_mts_in_drest_part_mea_mnt1",
#     "device_days_usage",
#     "device_type_rus_other",
#     "voice_in_kievstar_part_mea_mnt1",
#     "num_act_days_std_mnt3",
#     "voice_mts_in_dwork_part_min_mnt1",
#     "MV_dou_net",
#     "num_act_days_std_mnt1",
#     "device_type_smartphone",
#     "loc_is_obl_center",
#     "Balance_uah",
#     "ks_num_part_mea_wk1",
#     "voice_mts_in_dwork_part_min_mnt3",
#     "lt",
#     "voice_mts_in_dwork_part_max_mnt3",
#     "cnt_paym_6_month",
#     "active_gba",
#     "voice_in_kievstar_part_std_mnt1",
#     "conn_in_uniq_cnt_td_mnt3",
#     "voice_in_kievstar_part_max_mnt1",
#     "content_cnt_mea_mnt3",
#     "device_android_version",
#     "voice_in_life_part_mea_mnt3",
#     "days_of_end_last_ppm",
#     "voice_mts_in_dwork_part_mea_mnt1",
#     "num_act_days_mea_mnt3",
#     "imei_mean_long_days_usage",
#     "bs_count_ppm_mn3",
#     "com_num_part_td_mnt3",
#     "voice_mts_out_nrest_partmea_wk1",
#     "voice_mts_in_drest_part_std_mnt1",
#     "MV_DOU_AP",
#     "voice_mts_out_nwork_partmin_mnt1",
#     "device_brand_nan",
#     "day_end_gba",
#     "voice_mts_in_dwork_part_std_mnt1",
#     "all_cnt_std_mnt1",
#     "sum_paym_6_month",
# ]


# report_LightGbmV2_p069_r033_090auc = [
#     "num_act_days_mea_wk1",
#     "num_act_days_mea_mnt1",
#     "active_ppm",
#     "device_brand_other",
#     "num_act_days_min_mnt3",
#     "device_type_rus_other",
#     "loc_market_share",
#     "MV_dou_net",
#     "device_has_lte",
#     "num_act_days_td_mnt3",
#     "voice_mts_in_drest_part_mea_mnt1",
#     "voice_mts_in_dwork_part_min_mnt1",
#     "voice_mts_in_drest_part_mea_wk1",
#     "device_days_usage",
#     "num_act_days_std_mnt3",
#     "Balance_uah",
#     "loc_is_obl_center",
#     "conn_in_uniq_cnt_td_mnt3",
#     "num_act_days_min_mnt1",
#     "device_type_smartphone",
#     "ks_num_part_mea_wk1",
#     "voice_mts_in_dwork_part_min_mnt3",
#     "lt",
#     "voice_in_kievstar_part_mea_mnt1",
#     "num_act_days_std_mnt1",
#     "MV_dou",
#     "voice_in_kievstar_part_std_mnt1",
#     "voice_in_life_part_mea_mnt3",
#     "voice_mts_in_dwork_part_mea_mnt3",
#     "active_gba",
#     "conn_com_part_min_mnt1",
#     "voice_mts_in_dwork_part_max_mnt3",
#     "cnt_paym_6_month",
#     "device_sim_count",
#     "voice_mts_in_nwork_part_mea_mnt1",
#     "num_act_days_mea_mnt3",
#     "day_end_gba",
#     "content_cnt_mea_mnt3",
#     "imei_mean_long_days_usage",
#     "days_of_end_last_ppm",
#     "voice_mts_in_dwork_part_std_mnt1",
#     "myvf_day_usage",
#     "voice_out_short_part_mea_mnt3",
#     "com_num_part_td_mnt3",
#     "tsoa_call_cnt",
#     "device_brand_nan",
#     "sms_in_cnt_std_mnt3",
#     "voice_mts_in_drest_part_td_mnt3",
#     "voice_mts_out_nwork_partmin_mnt1",
# ]


# report_LightGbmV2_p070_r033_090auc = [
#     "num_act_days_min_mnt3",
#     "device_days_usage",
#     "num_act_days_mea_mnt1",
#     "loc_market_share",
#     "Balance_uah",
#     "lt",
#     "day_end_gba",
#     "days_of_end_last_ppm",
#     "num_act_days_std_mnt3",
#     "days_of_last_ppm",
#     "device_brand_other",
#     "all_cnt_std_mnt1",
#     "voice_out_short_part_mea_mnt3",
#     "voice_mts_in_dwork_part_mea_mnt3",
#     "num_act_days_min_mnt1",
#     "imei_mean_long_days_usage",
#     "content_cnt_mea_mnt3",
#     "sms_in_cnt_std_mnt3",
#     "abon_id",
#     "voice_out_tar_dur_min_mnt3",
#     "myvf_day_usage",
#     "imei_mean_days_usage",
#     "sum_paym_6_month",
# ]


# report_LightGbmV2_balanced = [
#     "num_act_days_mea_wk1",
#     "device_brand_other",
#     "num_act_days_min_mnt1",
#     "active_ppm",
#     "voice_mts_in_drest_part_mea_mnt1",
#     "num_act_days_td_mnt3",
#     "num_act_days_min_mnt3",
#     "MV_dou_net",
#     "voice_mts_in_dwork_part_max_mnt3",
#     "num_act_days_std_mnt1",
#     "num_act_days_std_mnt3",
#     "device_type_rus_other",
#     "device_sim_count",
#     "voice_mts_in_drest_part_std_mnt1",
#     "voice_mts_out_dwork_partmax_mnt3",
#     "device_brand_nan",
#     "voice_mts_in_dwork_part_std_mnt1",
#     "voice_in_kievstar_part_mea_mnt1",
#     "non_accum_internet_vol_mea_wk1",
#     "voice_mts_in_dwork_part_min_mnt1",
#     "num_act_days_mea_mnt1",
#     "num_act_days_max_mnt1",
#     "gprs_tar_vol_std_mnt1",
#     "device_days_usage",
#     "voice_mts_in_drest_part_td_mnt3",
#     "device_type_phone",
#     "voice_in_kievstar_part_max_mnt3",
#     "device_type_smartphone",
#     "voice_in_kievstar_part_max_mnt1",
#     "gprs_tar_vol_min_mnt1",
#     "voice_mts_in_dwork_part_max_mnt1",
#     "voice_mts_in_dwork_part_mea_mnt1",
#     "conn_com_part_max_mnt1",
#     "device_height_mm",
#     "non_accum_internet_vol_min_mnt3",
#     "conn_com_part_max_mnt3",
# ]
