# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 11:49:23 2017

@author: useradmin
"""
import pandas as pd
import matplotlib.pyplot as plt
from directories import farmdirs

aps_test = pd.read_pickle(farmdirs['pickels']+'aps_toplot.p')
met_jd = pd.read_pickle(farmdirs['pickels']+'met_jd.p')
aps_test = aps_test.sum(axis=1)
aps_test = aps_test[aps_test>0]
aps_test = aps_test[aps_test<4]


high_hum = met_jd[met_jd.Humidity<85
                  ]
fig, ax1 = plt.subplots()
ax1.plot(high_hum.index, high_hum.Humidity, marker = 'o', )


ax1.set_ylim(50,110)
ax2=ax1.twinx()
ax2.plot(aps_test.index, aps_test, marker ='o', linewidth=0, color ='red')

