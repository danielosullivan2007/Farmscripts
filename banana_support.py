# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 11:00:32 2017

@author: useradmin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from directories import farmdirs
import datetime
from myfuncs import jd_to_date, date_to_jd

tillage = pd.read_csv(farmdirs['pickels']+'activities.csv')
tillage.Start = pd.to_datetime(tillage.Start, format='%d/%m/%Y %H:%M')
tillage.End = pd.to_datetime(tillage.End, format='%d/%m/%Y %H:%M')
#tillage.drop(3, inplace =True)


tillage['Start_jd'] = [tillage.Start[i].to_julian_date() for i in range(len(tillage.Start))]
tillage['End_jd'] = [tillage.End[i].to_julian_date() for i in range(len(tillage.End))]


met = pd.read_pickle(farmdirs['pickels']+'met.p')
cols = list(met)
met.drop([cols[0], cols[3], 
          cols[4], cols[11], cols[10], cols[14],
          cols[16]], axis =1, inplace =True)
met_jd = [met.index[i].to_julian_date() for i in range(len(met.index))]
met['jd'] = met_jd
met.to_pickle(farmdirs['pickels']+'met_jd.p')



INPs = pd.read_pickle(farmdirs['pickels']+'binned_INPs_witherrors_timestamps.p')
INPs.drop('Date', axis =1, inplace =True)
#INPs.dropna(how='any', axis =0, inplace =True)
INPs.INP_plus = INPs.INP_plus.astype(float)
INPs.INP_minus = INPs.INP_minus.astype(float)

INPs.rename(columns  = {'start':'start_datetime', 'end':'end_datetime'}, inplace =True)
pd.to_datetime(INPs.start_datetime)
INPs.start_datetime = INPs.start_datetime.apply(np.datetime64)
INPs.end_datetime = INPs.end_datetime.apply(np.datetime64)

INPs.reset_index(drop=True, inplace =True)
INPs_mid = [(INPs.start_datetime[i] + (INPs.end_datetime[i]-INPs.start_datetime[i])/2) for i in range(len(INPs))]
INPs_start_jd = [INPs.start_datetime[i].to_julian_date() for i in range(len(INPs.index))]
INPs_end_jd = [INPs.end_datetime[i].to_julian_date() for i in range(len(INPs.index))]
INPs_mid_jd = [INPs_mid[i].to_julian_date() for i in range(len(INPs.index))]

INPs['start_jd'] = INPs_start_jd
INPs['end_jd'] = INPs_end_jd
INPs['mid_jd'] =INPs_mid_jd
INPs.reset_index(drop=True, inplace =True)
INPs.dropna(how='any', axis =0, inplace =True)



#INPs=INPs[(INPs.INP-INPs.INP_minus)>0] #negative error cannot exceed
#INPs=INPs[(((INPs.INP +INPs.INP_plus).apply(np.log10))/INPs.INP.apply(np.log10)) <2]
#INPs=INPs[(INPs.INP/(INPs.INP-INPs.INP_minus)) <10]
del INPs_start_jd, INPs_end_jd, INPs_mid_jd ,met_jd

INPs_25 = INPs[INPs['T']==-25]
INPs_24 = INPs[INPs['T']==-24]
INPs_23 = INPs[INPs['T']==-23]
INPs_20 = INPs[INPs['T']==-20]
INPs_18 = INPs[INPs['T']==-18]


minp = date_to_jd(2016, 9,27)
maxp = date_to_jd(2016, 10,28)