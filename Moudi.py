# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 12:57:18 2017

@author: eardo
"""
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')


import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


os.chdir('W:\\Moudi\\171220\\')
files= glob.glob('*Data*.csv')
stage_list=[]
moudi_list = {'PR':' 18 µm',
              'S2': '5.6 - 18 µm',
              'S3' : '3.2 - 5.6 µm', 
              'S4':'1.8 - 3.2 µm', 
              'S5': '1-1.8 µm', 
              'S8': '0.18 - 1 µm ??'}


fig, ax = plt.subplots()
for i in range(len(files)):
    data = pd.read_csv(files[i])
    stage_list.append(files[i][27:29])
    yerr = [data['INPerr_neg'], data['INPerr_pos']]
    label = moudi_list[stage_list[i]]
    plt.errorbar(data['T'], data['INPs_perL'], yerr = yerr, lw=1, fmt = 'o', label = label)
    plt.legend(fontsize =8, numpoints =1)
    ax.set_yscale('log')
    ax.set_ylim(0.0001, 1000)
    plt.xlabel ('µ')