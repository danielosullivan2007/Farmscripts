# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 11:00:32 2017

@author: useradmin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from directories import farmdirs

from myfuncs import jd_to_date



met = pd.read_pickle(farmdirs['pickels']+'met.p')
cols = list(met)
met.drop([cols[0], cols[3], 
          cols[4], cols[11], cols[10], cols[14],
          cols[16]], axis =1, inplace =True)
met_jd = [met.index[i].to_julian_date() for i in range(len(met.index))]
met['jd'] = met_jd
met.read_pickle(farmdirs['pickels']+'met_jd_hourly.p')


INPs = pd.read_pickle(farmdirs['pickels']+'INPs.p').drop('Datetime', axis=1)
INPs['mid'] = INPs.start_datetime + (INPs.end_datetime-INPs.start_datetime)/2
INPs_start_jd = [INPs.start_datetime[i].to_julian_date() for i in range(len(INPs.index))]
INPs_end_jd = [INPs.end_datetime[i].to_julian_date() for i in range(len(INPs.index))]
INPs_mid_jd = [INPs.mid[i].to_julian_date() for i in range(len(INPs.index))]

INPs['start_jd'] = INPs_start_jd
INPs['end_jd'] = INPs_end_jd
INPs['mid_jd'] =INPs_mid_jd
del INPs_start_jd, INPs_end_jd, INPs_mid_jd ,met_jd

INPs_25 = INPs[INPs['T']==-25]
INPs_20 = INPs[INPs['T']==-25]
INPs_18 = INPs[INPs['T']==-25]