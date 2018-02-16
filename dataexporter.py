# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 09:50:10 2018

@author: eardo
"""

import pandas as pd
from directories import farmdirs
import datetime
import numpy as np

binned = pd.read_pickle(farmdirs['pickels']+ 'binned_INPs_witherrors_timestamps.p')
unique  = binned.drop_duplicates(subset = 'start')
unique = unique.drop(['Date','INP', 'T', 'INP_plus','INP_minus'], axis=1)

unique = pd.merge(unique, B_25, how='left', on =['start']).rename(columns ={'INP':'_25_'})
unique = pd.merge(unique, B_20, how='left', on =['start']).rename(columns ={'INP':'_20_'})
unique = pd.merge(unique, B_15, how='left', on =['start']).rename(columns ={'INP':'_15_'})

a=[binned['T']==-25]
b=[binned['T']==-20]
c=[binned['T']==-15]
correct = binned[(binned['T']==-25) | (binned['T']==-20)| (binned['T']==-15)].drop(['Date',  'INP_plus','INP_minus'], axis=1).reset_index(drop=True)
pivoted= correct.pivot_table(index=['start','end'],columns = 'T').reset_index()

pivoted['runtime'] = (pivoted['end']-pivoted['start']) / np.timedelta64(1, 'm')