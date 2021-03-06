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


infolder = 'Y:\\'
os.chdir(infolder)


s_list=[]
a_list=[]
smps_count=pd.Series()
aps_count=pd.Series()
#Glob top folder

a=glob.glob('*\\')
filelist=[]
out1=np.empty(shape=(1,2))
out2=np.empty(shape=(1,2))
out3=np.empty(shape=(1,2))
out1[:] = np.NAN
out2[:] = np.NAN
out3[:] = np.NAN


#####################################################################
#Glob SMPS folders
n=0
index=0

if 'smps' in locals():
    del smps

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
                
                '''SMPS sizes'''
                DpSMPS=(1/chi)*sizes
                smps_cols=(np.ndarray.tolist(sizes))
                smps_df=pd.DataFrame((np.transpose(dW)))
                smps_df.columns=smps_cols
                
                if smps_df.mean().sum():
                    smps_count = smps_count.append(pd.Series(smps_df.mean().sum(), index=[index]))
                else:
                    smps_count = smps_count.append(pd.Series('NaN', index=[index]))
                index+=1
                
# =============================================================================
#         
# =============================================================================
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

        n+=1
        
        s_size = DpSMPS.T
        s_counts = SMPSavnum.T
        
        smps_run = dict(zip(s_size, s_counts))
        smps_to_append = (pd.DataFrame(smps_run, index =[0]))
        
        if 'smps' not in locals():
            smps = pd.DataFrame(smps_run, index =[0])
            print 'Exists'
        else:
            smps=pd.concat([smps, smps_to_append])
            
smpsav_df = pd.concat([s_dates, s_times, smps_count], axis =1)




######################################################################
#glob APS folders
index=0
if 'aps' in locals():
    del aps

for dayfolder in range(len(a)):
    os.chdir(infolder+ a[dayfolder]+'APS\\')
    a_files = glob.glob('*.csv')
    if len(a_files) ==0:
        continue
    else:
    
#APS Calcs
        
        for i in range(len(a_files)):
                
                APSdata= np.genfromtxt(a_files[i], delimiter =',', skip_header=7)[:,5:54]
                aps_df = pd.DataFrame(APSdata)
                a_list.append(a_files[i])                
                a_dates = pd.Series([x[0:2]+"-"+ x[2:4]+"-"+x[4:6] for x in a_list])
                a_times = pd.Series([x[7:9]+":"+x[9:11] for x in a_list]).replace('.c:sv', np.NAN).replace('cs:v', np.NAN)
                if aps_df.mean().sum():
                    aps_count = aps_count.append(pd.Series(aps_df.mean().sum(), index=[index]))
                else:
                    aps_count = aps_count.append(pd.Series('NaN', index=[index]))
                    index+=1
                

                with open(a_files[0]) as csvfile:
                    reader = csv.reader(csvfile, delimiter =',')
                    APShead=[row for row in reader]
            
        APSheader = APShead[6]
        APSsize= (APSheader[5:54])
        APSsize = [float(x) for x in APSsize]
        APSsize = np.array(APSsize)
        
        APSdata[APSdata == 0] = np.nan  
        
        APSavnum=np.nanmean(APSdata, axis = 0) 
        '''APS Section'''
        DpAPS=(((chi*rho0)/rho)**0.5)*APSsize
        z=np.transpose(np.vstack((DpAPS, APSavnum)))
        
        outtime = a_files[i][6:11]
        outname = infolder+ a[dayfolder]+'APSav '+outtime+'.csv'
        
        np.savetxt(outname, z, delimiter = ',')
        
        aps_cols=(np.ndarray.tolist(APSsize))
        aps_df=pd.DataFrame(APSdata)
        aps_size = aps_df.columns
        
        

        
# =============================================================================
#         plt.xlim(0.01, 20)
#         ax2 = plt.scatter(DpAPS, APSavnum, c = 'red', zorder =20)
#         plt.ylim(0.01,1000)
#         plt.xscale('log')
#         plt.yscale('log')
# =============================================================================
        
        aps_count.reset_index(drop = True, inplace = True)
        aps_result = pd.concat([a_dates, a_times, aps_count], axis =1)
        aps_result.columns = ['a_dates', 'a_times', 'a_count']
        aps_result['datetime']=pd.to_datetime(aps_result['a_dates']+" "+aps_result['a_times'], yearfirst =True)
        aps_result.set_index('datetime', inplace = True)
        
        
        size = DpAPS.T
        counts = APSavnum.T
        
        aps_run = dict(zip(size, counts))
        aps_to_append = (pd.DataFrame(aps_run, index =[0]))
        
        if 'aps' not in locals():
            aps = pd.DataFrame(aps_run, index =[0])
            print 'Exists'
        else:
            aps=pd.concat([aps, aps_to_append])
        #aps_result.to_pickle('C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\aps.p')
        

#%%
#merge smps and aps in all folders    
################################################################

os.chdir(infolder)
aps = aps.T
aps['average'] = aps.mean(axis =1)
fig = plt.figure(figsize =(3,3))


plt.scatter(aps.index, aps['average'], c = 'c', zorder =21, linewidth=0.)

smps=smps.T
smps['average']= smps.mean(axis=1)
smps = smps.drop([smps.index[0],0.61375])
plt.scatter(smps.index, smps['average'], c = 'c', zorder =23, linewidth=0.1)
plt.ylabel('dN (# of particles)')
plt.xlabel('Volume Equivalent Diameter ($\mu$m)')
plt.ylim(0.001,1000)

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
            
            plt.scatter(merged[:,0], merged[:,1], alpha =0.5, linewidth=0)
            plt.xscale('log')
            plt.yscale('log')
            plt.ylim(0.001,1000)
            plt.xlim(0.01, 20)
            outname = infolder+ a[dayfolder]+'merged.csv'
            np.savetxt(outname, merged, delimiter = ',')
            

         
print ' Data has been merged :)'

