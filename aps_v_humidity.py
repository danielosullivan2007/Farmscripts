# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 11:49:23 2017

@author: useradmin
"""
import pandas as pd
import matplotlib.pyplot as plt
from directories import farmdirs
import numpy as np

aps_test = pd.read_pickle(farmdirs['pickels']+'aps_toplot.p')
met_jd = pd.read_pickle(farmdirs['pickels']+'met_jd.p')
aps_test = aps_test.sum(axis=1)
aps_test = aps_test[aps_test>0]
aps_test = pd.DataFrame(aps_test).rename(columns = {0:'aps'})
join= pd.concat([aps_test, met_jd], axis=1)
join['log_aps']=join['aps'].apply(np.log10)
join=join[join['Humidity']>90]

fig, ax1 = plt.subplots()
ax1.plot(join.index, join.Humidity, marker = 'o', )


ax1.set_ylim(50,110)
ax2=ax1.twinx()
ax2.plot(join.index, join.aps, marker ='o', linewidth=0, color ='red')

fig1, ax3 =plt.subplots()
ax3.scatter( join.Humidity, join.aps)

import seaborn as sns

sns.jointplot('log_aps', 'Humidity', data = join)
cols = list(met_jd)

