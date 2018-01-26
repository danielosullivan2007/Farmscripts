# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 10:40:08 2018

@author: eardo
"""

import pandas as pd
from directories import farmdirs
import matplotlib.pyplot as plt
from myfuncs import degree_sign

binned = pd.read_pickle(farmdirs['pickels']+ 'binned_INPs_witherrors_timestamps.p')
raw = pd.read_csv(farmdirs['pickels'] + 'INPs_trim_witherrs.csv')

fig, ax = plt.subplots(figsize = (4,4))
ax.plot(raw['T'], raw['INPs_perL'], lw=0, marker ='o', alpha = 0.7)
ax.plot(binned['T'], binned['INP'], lw=0, marker ='o', color = 'r')
ax.set_xlabel('T ('+degree_sign+'C)',fontsize =14)
ax.set_ylabel('[INP] $\mathregular{L^{-1}}$', fontsize=14)

ax.set_yscale('log')

