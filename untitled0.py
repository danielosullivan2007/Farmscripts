# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:16:17 2017

@author: useradmin
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os as os
import scipy.ndimage as ndimage
from matplotlib.gridspec import GridSpec
import datetime
import matplotlib.cm as cm
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from matplotlib.ticker import LogFormatter 
from matplotlib.ticker import LogFormatterMathtext 
import myfuncs
'''DATA MUST BE IN LOG BINS BY INP NUMBER'''

import numpy as np
import os as os
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import socket
host = socket.gethostname()


##############################################################################
'''Changes to required directory'''
if host == 'see4-234':
    #pickdir = ('C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\')
    indir = ('C:\\Users\\eardo\\Desktop\\Farmscripts\\')
    picdir='C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\'
    glodir = ('C:\\Users\eardo\\Desktop\\Farmscripts\\glomap data\\')
elif host == 'Daniels-Air.home':
    pickdir = ('//Users//Daniel//Desktop//farmscripts//Pickels//')
    indir = ('//Users//Daniel//Desktop//farmscripts//')
    
elif host == 'SEE-L10840':
    indir = ('C:\\Users\\useradmin\\Desktop\\Farmscripts\\')
    glodir = ('C:\\Users//useradmin//Desktop//Farmscripts//glomap data//')    
    picdir = ('C:\\Users\\useradmin\\Desktop\\Farmscripts\\Pickels\\')
    #glodir = ('//Users//Daniel//Desktop//farmscripts//glomap data//160509//')

elif host =='Feynman':
    indir = ('C:\\Users\\Danny\\Desktop\\farmscripts\\')
    glodir = ('C:\\Users\\Danny\\Desktop\\farmscripts\\glomap data\\')
    picdir = ('C:\\Users\\Danny\\Desktop\\farmscripts\\Pickels\\')
    
percent = [0.2, 0.5, 0.8]



os.chdir(indir)



Nie=pd.read_csv(glodir+'INP_spectra_danny_m3_Niemand.csv', delimiter =',')/1000
Nie=Nie.transpose()
Nie['date']=day
Nie_mask=  (Nie['date'] > start_day) & (Nie['date'] <=  end_day)
Nie_data=Nie.loc[Nie_mask]


Nie_data=Nie.loc[Nie_mask].T.reset_index()
Nie_data['T'] = Nie_data['Temp']*-1
Nie_data=Nie_data.T
Nie_data.columns=list(Nie_data.loc['T'])
Nie_data.drop('Temp', inplace = True)
Nie_data.set_index('', inplace =True)
Nie_data.drop('', inplace =True)


Nie_data_stats = pd.DataFrame()
for i in range (len(list(Nie_data.columns))):
    Nie_data_stats[i]=pd.to_numeric(Nie_data.iloc[:,i]).describe(percentiles=percent)

Nie_data_stats = Nie_data_stats.T
Nie_data_stats.index = Nie_data_stats.index*-1
Nie_data_stats.drop ([  0,  -1,  -2,  -3,  -4,  -5,  -6,  -7,  -8,  -9, -10, -11,-12], inplace = True)
