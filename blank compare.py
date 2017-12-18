# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 16:11:00 2017

@author: eardo
"""

from datetime import datetime
import os, os.path
from glob import glob
import numpy as np
from os import listdir
os.chdir('C:\\Users\\eardo\\Desktop\\farmscripts\\')
import numpy as np
import matplotlib.pyplot as plt
import pylab
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import matplotlib.patches as mpatches
import socket
from directories import farmdirs
from myfuncs import degree_sign


blanks = pd.read_csv(farmdirs['pickels']+'blanks.csv')
data = pd.read_csv(farmdirs['pickels']+'MFC2_3data.csv')
hepas =  pd.read_csv(farmdirs['pickels']+'hepas.csv')
hepas =hepas[hepas['sample']!='a']


fig, ax =plt.subplots(figsize =(5,5))
ax.scatter(blanks['temp'], blanks['K'], color='r', alpha =0.3, label = 'MilliQ water')
ax.scatter(hepas['temp'], hepas['K'], color ='b', label ='Hepa filter on inlet')
ax.scatter(data['T'], data['K'], color ='k', alpha =0.7)
ax.set_yscale('log')
ax.set_ylim(10, 10000)
ax.set_xlabel('T ('+degree_sign+'C)')
ax.set_ylabel('INPs (/mL water)', fontsize =8)
plt.legend(scatterpoints=1, fontsize =8)


