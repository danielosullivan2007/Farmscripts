# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:07:43 2018

@author: eardo
"""

import pandas as pd
import matplotlib.pyplot as plt
from directories import farmdirs

inlet_calc = pd.read_csv(farmdirs['pickels']+'inlet_eff.csv')
inlet_pm10 = pd.read_csv(farmdirs['pickels']+'inlet_pm10.csv')
x=inlet_calc['size_um']
y = inlet_calc['percent']


fig, ax = plt.subplots()
ax.plot(x, y, label = 'Splitter efficiency (Calc.)')
ax.set_ylabel('% Transmission', fontsize = 8)
ax.set_xlabel('Particle Size  D$\mathregular{_p} (\mu m $)', fontsize =8)
ax.set_xscale('log')
ax.grid(which ='both')

x=inlet_pm10['Size']
y = inlet_pm10['Percent']*100
ax.plot(x,y, label = 'PM10 Head efficiency')
plt.legend(loc=3, fontsize =8)