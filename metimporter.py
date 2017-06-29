# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 13:06:28 2017

@author: eardo
"""

import glob
import os
import pandas as pd
import numpy as np

#==============================================================================
# #create files list
# path =r'C:\Users\eardo\Desktop\Farmscripts\MetData'
# allFiles = glob.glob(path + "/*.csv")
# frame = pd.DataFrame()
# list_ = []
# 
# 
# for file_ in allFiles:
#     df = pd.read_csv(file_,index_col=None, header=6, usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))
#     list_.append(df)
# frame = pd.concat(list_)
# 
# #fix the fact that times are of variable length
# frametime =frame['Time'].tolist()
# for i in range(0,len(frametime)):
#     frametime[i]=str(frametime[i])
#     if len(frametime[i])==1:
#         frametime[i]='000'+frametime[i]
#     if len(frametime[i])==3:
#         frametime[i]='0'+frametime[i]
#         
# frame['Time']=frametime        
# #pull out times only
# 
# dati=list(frametime)
# framedate =frame['Date'].tolist()
# 
# #remove / from dates
# for i in range(0,len(frametime)):
#     string=''
#     string=string+framedate[i][-2:]
#     if framedate[i][-7:-5].find('/')>=0:
#         string=string+'0'+framedate[i][-6]
#         
#     else:
#         string=string+framedate[i][-7:-5]
#         
#     if framedate[i][:2].find('/')>=0:
#         string=string+'0'+framedate[i][0]
#     else:
#         string=string+framedate[i][:2]
#     string=string+frametime[i]
#     
#     framedate[i]=string
#     
# 
#==============================================================================

os.chdir('C:\Users\eardo\Desktop\Farmscripts\MetData\Wind')
windimp = pd.read_csv('Bramham HCM data.csv',index_col=None, header=0)
windDT =windimp.ix[:,2]
windarray=pd.DataFrame.as_matrix(windimp)
windDT=windDT.tolist()
windDT=tuple(windDT)
 

windDT2=list(windDT)
windDT3=list(windDT)
for i in range(0,len(windDT2)):
    windDT2[i]=windDT[i][11:]   

for i in range(0,len(windDT2)):
    windDT3[i]=windDT[i][:10]  

for i in range(0,len(windDT2)):
    if windDT2[i]=='':
        windDT2[i]='00:00:00'
        
windDT2=([s.replace(':', '') for s in windDT2])

for i in range(0,len(windDT2)):
    windDT2[i]=windDT2[i][:-2]   
windDT2=pd.Series(windDT2)  

windDT3=pd.Series(windDT3)  
  


newlist=list(windDT2)
for i in range(0,len(newlist)):
    string=windDT3[i][-2:]+windDT3[i][-7:-5]+windDT3[i][:2]+windDT2[i]
    newlist[i]=string

newlist=pd.Series(newlist)
result=pd.concat([newlist, windimp], axis=1)
result=pd.concat([windDT3, result], axis=1)

framedate=pd.Series(framedate)

  

result.to_csv('wind.csv', delimiter=',')
frame.to_csv('metall.csv', delimiter=',')
framedate.to_csv('metalldatetime', delimiter=',')
