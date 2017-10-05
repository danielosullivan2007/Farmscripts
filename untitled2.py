# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:40:22 2017

@author: useradmin
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel('Book5.xlsx')
sns.set_style("whitegrid")
sns.set_context("paper", rc={"font.size":1,"axes.titlesize":12,"axes.labelsize":15}) 
ax1=sns.boxplot(x=data['Type'],y = data['amount'], orient ='v', width =0.5)
ax1.tick_params(labelsize=10)

plt.ylabel('$\mathregular{log_{10}}$ no. of cloud-modifying particles', fontsize =12)
plt.xlabel('test')

#ax2=plt.grid(ls='-', alpha =0.5, zorder=100)

#plt.title('Measured particles versus simulated from )