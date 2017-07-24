# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 17:50:11 2017

@author: useradmin
"""
import pandas as pd

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import datetime as dt







fig, ax1 =plt.subplots()
df_out['end'] = pd.to_datetime(df_out['end'])
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax1 = ax1.plot_date(df_out['end'],df_out['INPs'])[0]



# Set the major tick formatter to use your date formatter.

# This simply rotates the x-axis tick labels slightly so they fit nicely.

