# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 12:30:16 2018

@author: eardo
"""
import pandas as pd
from directories import farmdirs


binned = pd.read_pickle(farmdirs['pickels']+ 'binned_INPs_witherrors_timestamps.p')
aps = pd.read_pickle(farmdirs['pickels']+'aps.p')
smps = pd.read_pickle(farmdirs['pickels']+'smps.p')
met  = pd.read_pickle(farmdirs['pickels']+'met.p')
wind = pd.read_pickle(farmdirs['pickels'] + 'wind.p')


out = 'C:\\Users\\eardo\\Desktop\\To upload\\'

binned.to_csv(out+'binned_INPs.csv')
aps.to_csv(out+ 'aps.csv')
smps.to_csv(out + 'smps.csv')
met.to_csv(out+ 'met.csv')
wind.to_csv(out +'wind.csv')


