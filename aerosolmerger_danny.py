# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:48:21 2017

@author: Daniel O'Sullivan

Notes: a is the list of day folders. The code works by 1)Globbing the top folder,
2) globbing for SMPS files, importing data
and getting geometeric diameter as per Mohler 2008, then outputting averaged 
3) globbing for APS files and doing the same as 2)
and 4) merging the SMPS and APS by reglobbing again!

Fun no? 
"""

import numpy as np
import os as os
import glob as glob
import csv
import matplotlib.pyplot as plt
import pandas as pd


chi=1.2
rho0=1
rho=2.4


infolder = 'W:\\'
os.chdir(infolder)


s_list=[]
a_list=[]
smps_count=pd.Series()
#Glob top folder

a=glob.glob('*\\')
filelist=[]
out1=np.empty(shape=(1,2))
out2=np.empty(shape=(1,2))
out3=np.empty(shape=(1,2))
out1[:] = np.NAN
out2[:] = np.NAN
out3[:] = np.NAN
#%%
#####################################################################
#Glob SMPS folders
n=0
index=0
for dayfolder in range(len(a)):                 
    os.chdir(infolder+ a[dayfolder]+'SMPS\\')
    s_files = glob.glob('*.csv')
    if len(s_files) ==0:
        continue
    else:
    
#SMPS Calcs

        
        for i in range(len(s_files)):
                indata= np.genfromtxt(s_files[i], delimiter =',', skip_header=34, skip_footer = 30 )
                s_list.append(s_files[i])
                s_dates = [x[0:6] for x in s_list]
                s_times = [x[7:11] for x in s_list]
                dW= indata[:,1:]
                sizes= (indata[:,0])/1000
                SMPSavnum=np.mean(dW, axis = 1)
                DpSMPS=(1/chi)*sizes
                smps_cols=(np.ndarray.tolist(sizes))
                smps_df=pd.DataFrame((np.transpose(dW)))
                smps_df.columns=smps_cols
                
                if smps_df.mean().sum():
                    smps_count = smps_count.append(pd.Series(smps_df.mean().sum(), index=[index]))
                else:
                    smps_count = smps_count.append(pd.Series('NaN', index=[index]))
                index+=1
                
        
        s_dates=pd.Series(s_dates)
        s_times=pd.Series(s_times).replace('.csv','NaN').replace('csv','NaN')
        
        
        

    

        DpSMPS = np.array(DpSMPS)
        SMPSavnum = np.array (SMPSavnum)
        outtime = s_files[i][6:11]
        outname = infolder+ a[dayfolder]+'SMPSav '+outtime+'.csv'
        q=np.transpose(np.vstack((DpSMPS, SMPSavnum)))
        np.savetxt(outname, q, delimiter = ',')
        #plt.title(str(files[i]))
        #plt.xscale('log')
        
        #plt.yscale('log')
        plt.ylabel('dw')
        plt.xlabel('Dp ($\mu$m)')
        n+=1
smpsav_df = pd.concat([s_dates, s_times, smps_count], axis =1)
    
'''
#%%
######################################################################
#glob APS folders
for dayfolder in range(len(a)):
    os.chdir(infolder+ a[dayfolder]+'APS\\')
    a_files = glob.glob('*.csv')
    if len(a_files) ==0:
        continue
    else:
    
#APS Calcs
        
        for i in range(len(a_files)):
                APSdata= np.genfromtxt(a_files[i], delimiter =',', skip_header=7)[:,5:54]
                a_list.append(a_files[i])                
                a_dates = pd.Series([x[0:6] for x in a_list])
                a_times = pd.Series([x[7:11] for x in a_list]).replace('.csv', np.NAN).replace('csv', np.NAN)
                a

                with open(a_files[0]) as csvfile:
                    reader = csv.reader(csvfile, delimiter =',')
                    APShead=[row for row in reader]
            
        APSheader = APShead[6]
        APSsize= (APSheader[5:54])
        APSsize = [float(x) for x in APSsize]
        APSsize = np.array(APSsize)
        
        APSdata[APSdata == 0] = np.nan  
        
        APSavnum=np.nanmean(APSdata, axis = 0) 
        DpAPS=(((chi*rho0)/rho)**0.5)*APSsize
        z=np.transpose(np.vstack((DpAPS, APSavnum)))
        
        outtime = a_files[i][6:11]
        outname = infolder+ a[dayfolder]+'APSav '+outtime+'.csv'
        
        np.savetxt(outname, z, delimiter = ',')
        
        aps_cols=(np.ndarray.tolist(APSsize))
        aps_df=pd.DataFrame(APSdata)
        aps_df.columns=aps_cols
        aps_count = aps_df.mean().sum()

        
        
        plt.xlim(0.01, 20)
        ax2 = plt.scatter(DpAPS, APSavnum, c = 'red')
        plt.ylim(0.01,100)
        plt.xscale('log')
        plt.yscale('log')
#%%
#merge smps and aps in all folders    
################################################################

os.chdir(infolder)

a=glob.glob('*\\')
for dayfolder in range(len(a)):
    os.chdir(infolder+ a[dayfolder])
    smps_files = glob.glob('SMPS*.csv')
    aps_files = glob.glob('APS*.csv')
    if len(smps_files)== 0 or len(aps_files) == 0:
        continue
    else:
        for smpsrun in range(len(smps_files)):
            smps_data=np.genfromtxt(smps_files[smpsrun], delimiter = ',')
        for apsrun in range(len(aps_files)):
            aps_data = np.genfromtxt(aps_files[apsrun], delimiter = ',')
            
            
            
            merged = np.vstack((smps_data, aps_data))
            
            plt.scatter(merged[:,0], merged[:,1])
            plt.xscale('log')
            plt.yscale('log')
            plt.ylim(0.0001,100)
            outname = infolder+ a[dayfolder]+'merged.csv'
            np.savetxt(outname, merged, delimiter = ',')
            

         
print ' Data has been merged :)'
'''
del s_list
#del s_files