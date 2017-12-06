# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 12:17:55 2017

@author: eardo
"""

import pandas as pd
import matplotlib.pyplot as plt
from directories import farmdirs
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from myfuncs import degree_sign
import matplotlib.ticker as ticker

data = pd.read_csv(farmdirs['pickels']+'all_data_with_met.csv')
data_85RH = pd.read_csv(farmdirs['pickels']+'all_data_with_met_rh85.csv')
data.reset_index(inplace=True)
data_85RH.reset_index(inplace=True)




data = data[data['APS Total']<30000]
#data['INP']= 10**data['INP']

data['APS Total']= data['APS Total'].apply(np.log10)
data_85RH['APS Total']= data_85RH['APS Total'].apply(np.log10)



import seaborn as sns


# =============================================================================
# c=0
# for i in range(-24, -16):
#     c+=1
#     plt.figure(c)
#     print i
#     data_atT = data[data['Temp']==i]
#     sns.jointplot(x='APS Total', y = 'INP',data =data_atT, kind ='reg',marginal_kws=dict(bins=10))
#     plt.savefig(farmdirs['figures']+'APS v INP_all RH at {}'.format(i))
#     
# =============================================================================
# =============================================================================
# for i in range(-24, -16):
#     c+=1
#     plt.figure(c)
#     print i
#     data_atT_85RH = data_85RH[data_85RH['Temp']==i]
#     sns.jointplot(x='APS Total', y = 'INP',data =data_atT_85RH, kind ='reg',marginal_kws=dict(bins=10))
#     plt.savefig(farmdirs['figures']+'APS v INP_85RH at {}'.format(i))
# =============================================================================


T1=-23
T2=-18

p1 = data_85RH[data_85RH['Temp']==T1]
p2 = data_85RH[data_85RH['Temp']==T2]

x=p1['APS Total']
y=p1.INP
fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=True, figsize =(6,3))
sns.regplot(x=x, y=y, data = p1, ax =ax1, ci=95)
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
r_value=str(round(r_value, 2))
p_value=str(round(p_value, 2))
text = ' $T=  {}$'.format(T1)+degree_sign+'$C$ \n $R=  {}$ \n $p=  {}$'.format(r_value, p_value)
plt.text(0.05,0.05, text, transform=ax1.transAxes, bbox={'facecolor':'gray', 'alpha':0.3, 'pad':5})
ax1.set_xlabel('$\mathregular{log_{10} \/\ [APS \/\ Total]}$')
ax1.set_ylabel('$\mathregular{log_{10} \/\ [INP]}$')


x=p2['APS Total']
y=p2.INP
sns.regplot(x='APS Total', y='INP', data = p2, ax =ax2, 
            line_kws ={'color':'blue'}, scatter_kws={'color':'blue', 'alpha':0.8})

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
r_value=str(round(r_value, 2))
p_value=str(round(p_value, 2))
text = ' $T=  {}$'.format(T2)+degree_sign+'$C$ \n $R=  {}$ \n $p=  {}$'.format(r_value, p_value)
plt.text(1.1,0.05, text, transform=ax1.transAxes,bbox={'facecolor':'gray', 'alpha':0.3, 'pad':5})

for ax in (ax1, ax2):
    ax.set_xlabel('$\mathregular{log_{10} \/\ [APS \/\ Total]}$')
    ax.set_ylabel('$\mathregular{log_{10} \/\ [INP]}$')
    for label in ax.xaxis.get_ticklabels()[::2]:
        label.set_visible(False)
        for label in ax.yaxis.get_ticklabels()[::2]:
            label.set_visible(False)

ax2.set_ylabel('')
plt.tight_layout(w_pad =0)



