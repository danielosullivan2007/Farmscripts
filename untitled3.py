# -*- coding: utf-8 -*-
"""
Created on Tue Jul 04 15:34:35 2017

@author: useradmin
"""

def get_smpsavs(df_meta):
    smps_avs = pd.DataFrame()
    smps_total=pd.DataFrame()
    for i in range (len(df_meta)):
        if df_SMPS.empty: 
            continue
        else: 
            smps_mask = (df_SMPS['datetimes'] > df_meta['start'][i]) & (df_SMPS['datetimes']  <=  df_meta['end'][i])
            if df_SMPS.loc[smps_mask]['datetimes'].empty:
                    
                continue
            else:
                
                smps_avs=smps_avs.append(df_SMPS.loc[smps_mask].mean(axis=0, skipna = True), ignore_index=True)
#==============================================================================
#             INP_start, INP_end, last_data, first_data, diff_to_end, diff_from_start = get_t_diffs(smps, smps_mask)
#             timediffs_smps = compile_t_diffs(INP_start, INP_end, last_data, first_data, diff_to_end, diff_from_start)
#==============================================================================
    frames2 = [smps_avs, df_meta]
    smps_avs = pd.concat (frames2, axis =1, ignore_index= False, join= 'outer')
    smps_total = smps_total.append(smps_avs.sum(axis=1), ignore_index=True).T
    smps_total.columns=['SMPS_total']
    cols=smps_avs.columns.tolist()
    cols = cols[-2:] + cols[:-2]
    smps_avs = smps_avs[cols]
    df_meta['SMPS']= smps_total
    return df_meta, smps_avs

x ,y =get_smpsavs(dayfolder)