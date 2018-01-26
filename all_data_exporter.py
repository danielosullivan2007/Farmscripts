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
from directories import farmdirs
from datetime import datetime


##for heated files, 
topfolder = 'W:\\'


no_heat_files=[]
match_files=[]
all_files=[]
files_without_key=[]
skip_list = ['Moud', 'heat', 'heated', 'Heat', 'HEAT']

os.chdir(topfolder)
a=glob('*\\')


def getdata_on_keyword(folders_list):
    
    counter =0
    exported_files = []
    unheated_data=[]
    exported_data =pd.DataFrame(columns = ['T', 'INPs_perL', 'F', 'K', 'INPs_perdrop', 
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
            if any(word in files_in_folder[s] for word in skip_list):
                continue
                print ('heat in {}'.format(files_in_folder[s]))
            elif 'PC' in files_in_folder[s]:
                #print files_in_folder[s]
                exported_files.append(files_in_folder[s])
                df = pd.read_csv(files_in_folder[s])
                df['start'] = datetime.strptime( files_in_folder[s][5:11]+ ' '+ files_in_folder[s][17:21],  '%y%m%d %H%M')
                df['end'] = datetime.strptime( files_in_folder[s][5:11]+ ' '+ files_in_folder[s][22:26],'%y%m%d %H%M')
                
                if 'ff' in df.columns.values:
                    
                   # print '{} not updated to include errors'.format(files_in_folder[s])
                    continue
                else:
                    print files_in_folder[s]
                    exported_data = exported_data.append(df)

                
                
    return exported_data, all_files, exported_files
            
exported, all_files, exported_files = getdata_on_keyword(a)
exported['neg_mag'] = exported.loc[:,'INPerr_neg'].apply(np.log10)-exported.loc[:,'INPs_perL'].apply(np.log10)
exported['neg_mag'] = exported.loc[:,'neg_mag'].apply(np.absolute)
trimmed = exported [exported.loc[:,'neg_mag']<1]
trimmed.drop(['K', 'INPs_perdrop','INPerr_pos', 'INPerr_neg', 'neg_mag'], axis =1, inplace =True)
trimmed.to_csv(farmdirs['pickels']+'INPs_trim_witherrs.csv')
                       


