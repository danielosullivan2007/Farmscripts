#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 21:33:37 2017

@author: Daniel
"""

import shutil
import os
import glob

APSfiles=[]
files =[]
source = '/Users/Daniel/Desktop/Test Data/'
Organized = '/Users/Daniel/Desktop/Organized/'


os.chdir(source)
APS_files = [i for i in  glob.glob('*APS*')]
APS_dates = [i[0:7] for i in APS_files]
APS_dates= list(set(APS_dates))

os.chdir(Organized)

for i in range(len(APS_dates)):
    
    if not os.path.exists(Organized+APS_dates[i]):
        os.mkdir(APS_dates[0])
    
    
    os.chdir(Organized+APS_dates[i])
    [shutil.copy ((source+j),os.getcwd()) for j in APS_files if APS_dates[i] in j]
    