# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 10:10:48 2017

@author: eardo
"""

import pandas as pd
import glob as glob
import os 


indir = 'V:\\All met data\\'
os.chdir('V:\\All met data\\')
files = glob.glob('*')


met=pd.DataFrame()
for i in range(len(files)):
    df = pd.read_table(files[i], header =0, usecols = range(15))
    met = met.append(df)