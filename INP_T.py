# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:20:17 2017

@author: eardo
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
import pandas as pd


#==============================================================================
# num2words={-15:'minus15',-16:'minus16',-17:'minus17',-18:'minus18',
#            -19:'minus19',-20:'minus20',-21:'minus21',
#            -22:'minus22', -23:'minus23', -24:'minus24',-25: 'minus25'}
# 
# #defining a function
# 
# 
# INP=[]
# point=[]
# paths=[]
# fday=[]
# day=[]
# date=[]
# Tlist=[]
# 
# 
# dayp=[]
# fdayp=[]
# fday17=[]
# datep17=[]
# datep20=[]
# datep23=[]
# excels_list=[]
# time_run=[]
# INP_Tlist=[]
# start_t=[]
# end_t=[]
# 
# df = pd.DataFrame({'Date':[], 'Start_time':[],'End_time':[], 'INP_T':[]})
# 
# day_folder='W:\\'
# out_folder='C:\\Users\\eardo\\Desktop\\Farmscripts\\'
# keyword=''
# """
# This section of the code creates the time series plots, taking data from the
# excel files specified and searching for the INP concentration at a specified 
# temperature
# """
# 
# for name in glob.glob(day_folder+'/*'): 
#     if os.path.isdir(name):
#         paths.append(name)
#     else:
#         continue
# 
# paths.sort()    
# number_days=len(paths)
# n=0
# for T in range(-25,-14):
#     
#     n+=1
#     for i in range(0,number_days):
#         extension = 'csv'
#         path=paths[i]
#         print path
#         os.chdir(path)
#         excels = [i for i in glob.glob('*'+keyword+'*.{}'.format(extension))]
#         excels_list.append(excels)
#         #print(excels)
#         number_excels=len(excels)
#         if number_excels==0:
#             #print('no excels on the '+str(path[-6:]))
#             continue
#         daily_reading=0
#         for i in range(0,number_excels):
#                 datain=np.genfromtxt(path+'\\'+excels[i],delimiter=',',skip_header=1,usecols=(0,1),dtype=float)
#                 df=pd.DataFrame(datain, columns = ['T', 'INP'])
#                 df2=df.drop_duplicates(['T'], keep = 'last')
#                 data=df2.as_matrix()
#                 #print(len(data))
#                 filename=excels[i]          
#                 day.append(path[-6:-4]+'/'+path[-4:-2]+'/'+path[-2:])
#                 
#                 fday.append(path[-6:-4]+path[-4:-2]+path[-2:]+filename[17:21]+filename[22:26])
#                 start_t.append(filename[17:21])
#                 end_t.append(filename[22:26])
#                 Tlist.append(T)
#                 #print(filename)
#                 
#                 try:
#                     filename=int((filename[5:11])+(filename[17:21])+(filename[22:26]))
#                 except ValueError:
#                     #print(filename)
#                     filename='nan'
#                     pass
#                 time_run.append(filename)
#                 try:
#                     
#                     for i in range(0,len(data)):
#                         #print(i)
#                         
#                         #if Ti/T>1 and Ti-1 >T and Ti+1<T
# 
#                         #print (data[i,0])
#                         #if data[i,0]/T<=1 and data[i-1,0]>=T and data[i+1,0]<=T:
#                         try:
#                             notequalto = data[i,0]!=data[i+1,0] and data[i,0]!=data[i-1,0]
#                             
#                         except IndexError:
#                             equalto=0
#                             pass
#                         if data[i,0]/T>=1 and data[i-1,0]>T and data[i+1,0]<T and notequalto==True:
#                             #print (data[i,0])
#                             point=data[i-1:i+1]                
#                             m=(point[1,1]-point[0,1])/(point[1,0]-point[0,0])
#                             INP_T=point[0,1]+m*(T-point[0,0])
#                             print('INP concentration for'+str(filename)+ '=' + str(INP_T))
#                             INP_Tlist.append(INP_T)
#                             #print 'added data'+str(INP_T)
#                             pass
#                         if data[i,0]/T>=1 and data[i-1,0]>T and data[i+1,0]<T and notequalto==False:
#                             INP_Tlist.append('triple')
#                             pass
#                     if data[0,0]<=T:
#                         #print(data[0,1])
#                         #print('Freezing starts below specified T')
#                         #print(data[0,0],'This is the first freezing value')
#                         #INP_T=data[0,1]
#                         #INP_Tlist.append(INP_T)
#                         INP_Tlist.append('below')
#                         #print 'added frezbelow'+str(INP_T)
#                         pass
#         
#                     if data[-1,0]>=T:
#                         #print(data[-1,1])
#                         #print('Freezing ends before specified T')
#                         #print(data[-1,0],'This is the last freezing value')
#                         #INP_T=data[-1,1]
#                         #INP_Tlist.append(INP_T)
#                         INP_Tlist.append('before')
#                         #print 'added frezends'+str(INP_T)
#                         pass
#                     
# #                    else:
# #                        INP_Tlist.append('else')
# #                        pass
#                 
# 
#                 except IndexError:
#                     #print("Your csv file is empty for this day")
#                     INP_Tlist.append('nan')
#                     
#                     continue
#                 if INP_Tlist:
#                     x=np.vstack((time_run, start_t))
#                     x=np.vstack((x, end_t))
#                     x=np.vstack((x, INP_Tlist))
#                     x=np.vstack((x, Tlist))
#                     x=np.transpose(x)
#                     #print x
#                     
#                 else:
#                     continue
# 
#     #np.savetxt(day_folder+'INP output.csv',INP_Tlist,delimiter=',')
# 
# df3=pd.DataFrame(x, columns = ['Date', 'start', 'end', 'INP', 'T'])
# df3=df3[df3!='before'];df3=df3[df3!='below'];
# df3['INP']=df3['INP'].astype(float)
# df3['T']=df3['T'].astype(float)
# 
# #d3=df[df.INP!='inf'] 
# df3.to_csv(out_folder+"INPs.csv", delimiter=',')
# ax1=df3.plot.scatter(x='T', y='INP', logy=True)
# fig = ax1.get_figure()
# fig.savefig(out_folder+keyword+'Binned INP')
# 
# df4=(df3.iloc[:,[3,4]]).dropna(how='any')
# df4.to_csv(out_folder+keyword+'.csv')
# df5=df4.pivot(index=None, columns='T', values='INP')
# ax2=df5.plot.box(logy=True)
# fig = ax2.get_figure()
# fig.savefig(out_folder+keyword+'boxplots')
# 
# 
# #==============================================================================
# minus15=df5[-15.0].dropna().describe()
# minus16=df5[-16.0].dropna().describe()
# minus17=df5[-17.0].dropna().describe()
# minus18=df5[-18.0].dropna().describe()
# minus19=df5[-19.0].dropna().describe()
# minus20=df5[-20.0].dropna().describe()
# minus21=df5[-21.0].dropna().describe()
# minus22=df5[-22.0].dropna().describe()
# minus23=df5[-23.0].dropna().describe()
# #minus24=df5[-24.0].dropna().describe()
# m#minus25=df5[-25.0].dropna().describe()
# 
# stats=(pd.concat([minus15,minus16,minus17,minus18,minus19,minus20,minus21,minus22,minus23],axis=1)).T
# 
# fig1=plt.plot()
# plt.subplot(111)
# ax3=plt.fill_between(stats.index, stats['25%'],stats['75%'], alpha=0.2)
# plt.yscale('log', nonposy='clip')
# plt.title('25 to 75% confidence intervals for INP data')
# plt.xlabel('T')
# plt.ylabel('INP')
# plt.savefig(out_folder+keyword+'Boxplots')
# 
# #==============================================================================
# 
# #df3.plot.box(x=minus'T', y='INP', logy=True)
# #==============================================================================
# # INPconc=np.genfromtxt(day_folder+'INP output.csv')
# # INPrun=np.genfromtxt(day_folder+'INP run.csv')
# # 
# #==============================================================================
# #==============================================================================
# # for i in range(0,len(fday)):
# #     b=0
# #     a=fday[i]
# #     b=datetime.datetime(int('20'+a[0:2]),int(a[2:4]),int(a[4:6]))
# #     date.append(b) 
# #     c=str(fday[i][6:10])
# #     start_tlist.append(c)
# #     d=str(fday[i][10:14])
# #     end_tlist.append(d)
# # 
# #     
# # x=np.transpose(np.vstack((date, start_tlist, end_tlist, INP_Tlist)))
# # df2=pd.DataFrame(x, columns = ['Date', 'Start_time','End_time', 'INP_T'])
# # df= df.append(df2, ignore_index=True)
# #==============================================================================
#==============================================================================
import datetime
glodir=('C:\\Users\\eardo\\Desktop\\Farmscripts\\glomap data\\160509\\')
zero_day = datetime.date(2001,1,1)
start_day = datetime.date(2001, 9, 15)
end_day = datetime.date(2001, 10,31)


felds=pd.read_csv(glodir+'INP_spectra_danny_feldspar.csv', delimiter =',', index_col=0)
day = list(felds.columns)

for i in range(len(day)):
    #day[i]="'"+day[i]+" days'"
    day[i]=int(day[i])
    day[i] = datetime.timedelta(day[i])
    day[i]=day[i]+zero_day

felds = felds.transpose()
felds['date']=day
feld_mask=  (felds['date'] > start_day) & (felds['date'] <=  end_day)
felds_data=felds.loc[feld_mask]

Nie=pd.read_csv(glodir+'INP_spectra_danny_m3_Niemand.csv', delimiter =',', index_col=0)
Nie=Nie.transpose()
Nie['date']=day
Nie_mask=  (Nie['date'] > start_day) & (Nie['date'] <=  end_day)
Nie_data=Nie.loc[Nie_mask]


total=pd.read_csv(glodir+'INP_spectra_danny_m3_total.csv', delimiter =',', index_col=0)
total=total.transpose()
total['date']=day
total_mask=  (total['date'] > start_day) & (total['date'] <=  end_day)
total_data=total.loc[total_mask]

marine=pd.read_csv(glodir+'INP_spectra_danny_marine.csv', delimiter =',', index_col=0)
marine=marine.transpose()
marine['date']=day
marine_mask=  (marine['date'] > start_day) & (marine['date'] <=  end_day)
marine_data=marine.loc[marine_mask]



del marine_mask, total_mask, Nie_mask, feld_mask, felds, total, marine, Nie, day, date
    






























