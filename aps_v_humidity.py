# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 11:49:23 2017

@author: useradmin
"""
import pandas as pd
import matplotlib.pyplot as plt
from directories import farmdirs
import numpy as np



aps_test = pd.read_pickle(farmdirs['pickels']+'aps_toplot_RH100.p')
met_jd = pd.read_pickle(farmdirs['pickels']+'met_jd.p')
aps_test = aps_test.sum(axis=1)
aps_test = aps_test[aps_test>0]
aps_test = pd.DataFrame(aps_test).rename(columns = {0:'aps'})
join= pd.merge(aps_test, met_jd, left_index=True, right_index=True)

RH = 0
title = 'RH >0%'
join['log_aps']=join['aps'].apply(np.log10)
join=join[join['Humidity']>RH]

fig, ax1 = plt.subplots()
ax1.plot(join.index, join.Humidity, marker = 'o', )


ax1.set_ylim(50,110)
ax2=ax1.twinx()
ax2.plot(join.index, join.aps, marker ='o', linewidth=0, color ='red')

fig1, ax3 =plt.subplots()
ax3.scatter( join.Humidity, join.aps)

import seaborn as sns

ax=sns.jointplot( 'Humidity', 'log_aps',data = join, kind ='reg')
cols = list(met_jd)
#plt.ylim(0,100)
plt.xlabel('% RH')
plt.ylabel('log$_{10}$ APS Count')
plt.ylim(0,2.5)
plt.text(100,2.1,title, color ='r')

###################################################################
smps_test = pd.read_csv(farmdirs['pickels']+'smps_RH100.csv')
smps_test.set_index('datetime', inplace =True)
smps_test = smps_test.sum(axis=1)
smps_test = smps_test[smps_test>0]
smps_test = pd.DataFrame(smps_test).rename(columns = {0:'smps'})
join_smps= pd.merge(smps_test, met_jd, left_index=True, right_index=True)
join_smps=join_smps[join_smps['Humidity']>RH]
join_smps['log_smps']=join_smps['smps'].apply(np.log10)

ax=sns.jointplot( 'Humidity', 'log_smps',data = join_smps, kind ='reg')
cols = list(met_jd)
#plt.ylim(0,100)
plt.xlabel('% RH')
plt.ylabel('log$_{10}$ SMPS Count')

plt.text(100,4.1,title, color ='r')