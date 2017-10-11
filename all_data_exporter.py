# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:58:04 2017

@author: eardo
"""
import os 
from glob import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
topfolder = 'X:\\'


no_heat_files=[]
match_files=[]
all_files=[]
files_without_key=[]


os.chdir(topfolder)
a=glob('*\\')
key_terms=['Heat', 'heat']

def getdata_on_keyword(folders_list):
    
    counter =0
    heat_files = []
    unheated_data=[]
    heated_data =pd.DataFrame(columns = ['T', 'INPs_perL', 'F', 'K', 'INPs_perdrop', 
                                 'INPerr_pos', 'INPerr_neg', 'delta_INP_pos',
                                 'delta_INP_neg'])
    unheated_data =pd.DataFrame(columns = ['T', 'INPs_perL', 'F', 'K', 'INPs_perdrop', 
                             'INPerr_pos', 'INPerr_neg', 'delta_INP_pos',
                             'delta_INP_neg'])
    
    for ifolder in range(len(a)):
        os.chdir(topfolder+ a[ifolder])
        #print 'looking in {}'.format(a[ifolder])
        files_in_folder=glob('*Data*.csv')
        all_files.extend(files_in_folder)    
        for s in range(len(files_in_folder)):        
            #Watch the in/not in clause in the next step!
            #to get heat remove the NOT!!!
            #print files_in_folder[s]
            if 'eat'  in files_in_folder[s]:
                #print ('heat in {}'.format(files_in_folder[s]))
                if 'PC' in files_in_folder[s]:
                    #print files_in_folder[s]
                    heat_files.append(files_in_folder[s])
                    df = pd.read_csv(files_in_folder[s])
                    
                    if 'ff' in df.columns.values:
                        
                        print '{} not updated to include errors'.format(files_in_folder[s])
                        continue
                    else:
                        counter +=1
                        heated_data = heated_data.append(df)
# =============================================================================
#                         fig, ax = plt.subplots()
#                         ax = plt.scatter(df['T'], df['INPs_perL'], label = files_in_folder[s])
#                         plt.yscale('log')
#                         plt.legend()
#                     
# =============================================================================
                else:
                    df_noheat = pd.read_csv(files_in_folder[s])
                    
                    if 'ff' in df.columns.values:
                        #print '{} not updated to include errors'.format(files_in_folder[s])
                        continue
                    else:
                        unheated_data = unheated_data.append(df_noheat)
            else:
                continue
                
                
    return heated_data, all_files, counter
            
exported, all_files, count = getdata_on_keyword(a)
exported['neg_mag'] = exported.loc[:,'INPerr_neg'].apply(np.log10)-exported.loc[:,'INPs_perL'].apply(np.log10)
exported['neg_mag'] = exported.loc[:,'neg_mag'].apply(np.absolute)
trimmed = exported [exported.loc[:,'neg_mag']<1]
trimmed.drop(['K', 'INPs_perdrop','INPerr_pos', 'INPerr_neg', 'neg_mag'], axis =1, inplace =True)
trimmed.to_csv('C:\\Users\\eardo\\Desktop\\Farmscripts\\'+'all_heated_data.csv')
                       


