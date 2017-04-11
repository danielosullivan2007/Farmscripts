# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:13:39 2016

@author: ed11gcep
"""

import os, os.path
import glob
import numpy as np
from os import listdir
import numpy as np
import matplotlib.pyplot as plt
import pylab
import matplotlib.pyplot as plt
import datetime


num2words={-15:'minus15',-16:'minus16',-17:'minus17',-18:'minus18',
           -19:'minus19',-20:'minus20',-21:'minus21',
           -22:'minus22', -23:'minus23', -24:'minus24',-25: 'minus25'}
b='Blan'
c='Port'
#defining a function

INP=[]
point=[]
paths=[]
fday=[]
day=[]
date=[]
APS_reading=[]
APS_date=[]
dateAPS=[]
INPp17=[]
INPp20=[]
INPp21=[]
dayp=[]
fdayp=[]
fday17=[]
datep17=[]
datep20=[]
datep23=[]
APSrangesum1=[]
time_run=[]
APS_concentration=[]
#aero_full=np.genfromtxt(path+'\\'+'APS data.csv',delimiter=',',skip_header=True,usecols=1)


T=-20
day_folder='W:\\'
out_folder='C:\Users\eardo\Desktop\Farmscripts\INP_T'
"""
This section of the code creates the time series plots, taking data from the
excel files specified and searching for the INP concentration at a specified 
temperature
"""

for name in glob.glob(day_folder+'/*'): 
    if os.path.isdir(name):
        paths.append(name)
    else:
        continue

paths.sort()    
number_days=len(paths)

for i in range(0,number_days):
    extension = 'csv'
    path=paths[i]
    os.chdir(path)
    excels = [i for i in glob.glob('*.{}'.format(extension))]
    #print(excels)
    number_excels=len(excels)
    if number_excels==0:
        print('no excels on the '+str(path[-6:]))
        continue
    daily_reading=0

    
    for i in range(0,number_excels):
        data=np.genfromtxt(path+'\\'+excels[i],delimiter=',',skip_header=1,usecols=(0,1,2),dtype=float)
         #print(len(data))
        time=excels[i]          
        day.append(path[-6:-4]+'/'+path[-4:-2]+'/'+path[-2:])
        
        fday.append(path[-6:-4]+path[-4:-2]+path[-2:]+time[17:21]+time[22:26])
        print(time)
        
        try:
            time=int((time[5:11])+(time[17:21])+(time[22:26]))
        except ValueError:
            time='nan'
            pass
        time_run.append(time)
        try:
        
            for i in range(0,len(data)):
                #print(i)
                if data[i,0]/T>=1 and data[i-1,0]>T and data[i+1,0]<T: 
                    point=data[i-1:i+1]                
                    m=(point[1,1]-point[0,1])/(point[1,0]-point[0,0])
                    INP_T=point[0,1]+m*(T-point[0,0])
                    print('INP concentration = %s'%INP_T)
                    INPp21.append(INP_T)
                    pass
            print(data[0,0])
            if data[0,0]<T:
                #print(data[0,1])
                print('Freezing starts below specified T')
                print(data[0,0],'This is the first freezing value')
                INP21=data[0,1]
                INPp21.append(INP21)
                pass
    
            if data[-1,0]>T:
                #print(data[-1,1])
                print('Freezing ends before specified T')
                print(data[-1,0],'This is the last freezing value')
                INP21=data[-1,1]
                INPp21.append(INP21)
                pass
        except IndexError:
            print("Your csv file is empty for this day")
            INPp21.append(0)
            continue






np.savetxt(day_folder+'INP output.csv',INPp21,delimiter=',')
np.savetxt(day_folder+'INP run.csv',time_run,delimiter=',')
INPconc=np.genfromtxt(day_folder+'INP output.csv')
INPrun=np.genfromtxt(day_folder+'INP run.csv')



for i in range(0,len(fday)):
    b=0
    a=fday[i]
    b=datetime.datetime(int('20'+a[0:2]),int(a[2:4]),int(a[4:6]))
    date.append(b) 

inplen=len(INPconc)   
outputfileINP=np.zeros((inplen,2)) 
outputfileINP[:,0]=INPconc
outputfileINP[:,1]=INPrun    

np.savetxt(out_folder+'INP data'+num2words[T]+'.csv',outputfileINP,delimiter=',')

#==============================================================================
# #APS
# 
# 
# for i in range(0,number_days):
#     try:
#         extension = 'csv'
#         path=paths[i]
#         path1=path+'\\'+'APS'
#         os.chdir(path1)
#         excels = [i for i in glob.glob('*.{}'.format(extension))]
#         #print(excels)
#     
#         day=excels[0]
#         day1=day[0:6]
#         day2=int(day1)
#         APS_date.append(day2)
#     except (TypeError,IndexError,WindowsError):
#             continue
#     number_excels=len(excels)
#     if number_excels==0:
#         #print('no excels on the '+str(path[-6:]))
#         continue
#     daily_reading=0
#     alldata=np.empty((0,56))
#     
#     for j in range(0,number_excels):
# 
# 
# 
#         dataAPS=np.genfromtxt(path+'\\APS\\'+excels[j],delimiter=',',skip_header=7,dtype=float)
#         APS=dataAPS[:,0:56]
#         APSrange=dataAPS[:,14:56]
#         APSrangemean=APSrange[:,0:42].mean(axis=0)
#         APSrangesum=np.sum(APSrangemean)
#         #print(APSrangesum)
#         APSrangesum1.append(APSrangesum)
#         #print(APSrangesum1)
# 
#     APSrangesum2=np.sum(APSrangesum1)
#     APS_concentration.append(APSrangesum2)
#     #print(APSrangesum2)
#     APSrangesum1=[]   
# 
# aeroconc=np.genfromtxt(day_folder+'aerosol output.csv')
# aerorun=np.genfromtxt(day_folder+'aerosol day.csv')
# 
# 
# 
# """
#     nint=float(len(alldataw0))
#     ints=int(nint/180)  
#    
#     for j in range(0,ints):
#         uAPS=np.array(alldata[j*180:(i+1)*180,14:56],dtype='float')
#         APSday=str(alldata[j*180,1])
#         APStime=str(alldata[j*180,2])
#         hist=uAPS.mean(axis=0)
#         dot_reading=np.sum(hist)
#         APS_reading.append(dot_reading)
#         APS_date.append('20'+APSday[6:8]+APSday[0:2]+APSday[3:5]+APStime[0:2]+APStime[3:5])
# """
# for i in range(0,number_excels):
#     b=0
#     #a=excels[i]
#     #d=datetime.datetime(int(excels[0:4]),int(excels[4:6]),int(excels[6:8]))
#     #dateAPS.append(d) 
#     inplen=len(INPconc)
#     aerolen=len(aeroconc)
# np.savetxt(day_folder+'Aerosol output.csv',APS_concentration,delimiter=',')
# np.savetxt(day_folder+'Aerosol day.csv', APS_date,delimiter=',')
# 
# 
# 
# #INPconc=np.genfromtxt(day_folder+'INP output.csv')
# #INPrun=np.genfromtxt(day_folder+'INP run.csv')
#==============================================================================




#==============================================================================
# outputfileaero=np.zeros((aerolen,2)) 
# outputfileaero[:,0]=aeroconc
# outputfileaero[:,1]=aerorun
#==============================================================================


#==============================================================================
# np.savetxt(out_folder+'Aero data.csv',outputfileaero,delimiter=',')
#==============================================================================


