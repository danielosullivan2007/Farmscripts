# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 17:25:07 2017

@author: eardo
"""
import os, os.path
import glob
import numpy as np
from os import listdir
import numpy as np
import matplotlib.pyplot as plt
import pylab
import matplotlib.pyplot as plt
import pandas as pd


infolder='C:\\Users\\eardo\\Desktop\\Farmscripts\\Heat data\\'
os.chdir(infolder)
heat=pd.read_csv('heat.csv')
noheat=pd.read_csv('noheat.csv')


ax1 = heat.plot.scatter('T','INP', color = 'r')
ax2 = noheat.plot.scatter('T','INP', ax=ax1, logy = True, color='b')




df4_heat=(heat.iloc[:,[1,2]]).dropna(how='any')

df5_heat=df4_heat.pivot(index=None, columns='T', values='INP')
ax3=df5_heat.plot.box(logy=True)


df6_heat=(heat.iloc[:,[1,2]]).dropna(how='any')
df7_heat=df4_heat.pivot(index=None, columns='T', values='INP')
ax4=df5_heat.plot.box(logy=True, ax =ax3)
#==============================================================================
# fig = ax2.get_figure()
# fig.savefig(out_folder+keyword+'boxplots')
#==============================================================================
