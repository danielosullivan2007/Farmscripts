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




chi=1.2
rho0=1
rho=2.4


infolder = 'W:\\'
os.chdir(infolder)



#Glob top folder

a=glob.glob('*\\')[17:18] 
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

for dayfolder in range(len(a)):                 
    os.chdir(infolder+ a[dayfolder]+'SMPS\\')
    files = glob.glob('*.csv')
    if len(files) ==0:
        continue
    else:
    
#SMPS Calcs


        for i in range(len(files)):
                indata= np.genfromtxt(files[i], delimiter =',', skip_header=34, skip_footer = 30 )
            
        sizes= (indata[:,0])/1000
        dW= indata[:,1:]
        SMPSavnum=np.mean(dW, axis = 1)
        DpSMPS=(1/chi)*sizes
        fig = plt.figure() 
        ax1=plt.scatter(DpSMPS, SMPSavnum)
        DpSMPS = np.array(DpSMPS)
        SMPSavnum = np.array (SMPSavnum)
        outtime = files[i][6:11]
        outname = infolder+ a[dayfolder]+'SMPSav '+outtime+'.csv'
        q=np.transpose(np.vstack((DpSMPS, SMPSavnum)))
        np.savetxt(outname, q, delimiter = ',')
        plt.title(str(files[i]))
        plt.xscale('log')
        plt.yscale('log')
        plt.ylabel('dw')
        plt.xlabel('Dp ($\mu$m)')

#%%
######################################################################
#glob APS folders
for dayfolder in range(len(a)):
    os.chdir(infolder+ a[dayfolder]+'APS\\')
    files = glob.glob('*.csv')
    if len(files) ==0:
        continue
    else:
    
#APS Calcs
        
        for i in range(len(files)):
                APSdata= np.genfromtxt(files[i], delimiter =',', skip_header=7)[:,5:54]

                with open(files[0]) as csvfile:
                    reader = csv.reader(csvfile, delimiter =',')
                    APShead=[row for row in reader]
            
        APSheader = APShead[6]
        APSsize= (APSheader[5:54])
        APSsize = [float(x) for x in APSsize]
        APSsize = np.array(APSsize)
        
        APSdata[APSdata == 0] = np.nan  
        
        APSavnum=np.mean(APSdata, axis = 0) 
        DpAPS=(((chi*rho0)/rho)**0.5)*APSsize
        z=np.transpose(np.vstack((DpAPS, APSavnum)))
        
        outtime = files[i][6:11]
        outname = infolder+ a[dayfolder]+'APSav '+outtime+'.csv'
        
        np.savetxt(outname, z, delimiter = ',')
        
        
        plt.xlim(0.01, 20)
        ax2 = plt.scatter(DpAPS, APSavnum, c = 'red')
        plt.ylim(0.01,100)
        plt.xscale('log')
        plt.yscale('log')
#%%
#merge smps and aps in all folders    
################################################################

os.chdir(infolder)

a=glob.glob('*\\')[17:18]
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
            
            
            
            outname = infolder+ a[dayfolder]+'merged.csv'
            np.savetxt(outname, merged, delimiter = ',')
         
print ' Data has been merged :)'
