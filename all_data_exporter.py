# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:58:04 2017

@author: eardo
"""
import os 
from glob import glob
import pandas as pd

unheated_data =pd.DataFrame(columns = ['T', 'INPs_perL', 'F', 'K', 'INPs_perdrop', 
                                 'INPerr_pos', 'INPerr_neg', 'delta_INP_pos',
                                 'delta_INP_neg'])

topfolder = 'W:\\'

key_terms=['Heat', 'heat']
no_heat_files=[]
match_files=[]
all_files=[]
files_without_key=[]


os.chdir(topfolder)
a=glob('*\\')


for ifolder in range(len(a)):
    os.chdir(topfolder+ a[ifolder])
    files_in_folder=glob('*Data*.csv')
    all_files.extend(files_in_folder)    
    for s in range(len(files_in_folder)):        
        if key_terms[0] not in files_in_folder[s]:
            if 'PC' in files_in_folder[s]:
                no_heat_files.append(files_in_folder[s])
                df = pd.read_csv(files_in_folder[s])
                unheated_data = unheated_data.append(df)
        else:
            df_heat = pd.read_csv(files_in_folder[s])
        
unheated_data.drop(['K', 'INPs_perdrop','INPerr_pos', 'INPerr_neg'], axis =1, inplace =True)
unheated_data.to_csv('C:\\Users\\eardo\\Desktop\\Farmscripts\\='+'all_data.csv')
                       

