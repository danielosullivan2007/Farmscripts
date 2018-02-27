# -*- coding: utf-8 -*-
"""
Created on Fri Feb 09 13:05:01 2018

@author: Daniel
"""


import pandas as pd
import matplotlib.pyplot as plt
from directories import farmdirs

data=pd.read_csv(farmdirs['pickels']+ 'INPs_trim_witherrs.csv')
pd.to_datetime(data['start'])
times = data.iloc[:,6:8]
pd.to_datetime(times['start'])
times['difference'] = times['end']-times['start']
