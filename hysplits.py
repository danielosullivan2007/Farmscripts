# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 10:39:59 2017

@author: eardo
"""

 -*- coding: utf-8 -*-
"""
Created on Tue May 23 12:22:41 2017
@author: eardo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import datetime
import math

degree_sign= u'\N{DEGREE SIGN}'
import socket
host = socket.gethostname()


if host== 'Daniels-Air.home':
    indir = ('//Users//daniel//Desktop//farmscripts//')

if host == 'see4-234':
    #pickdir = ('C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\')
    indir = ('C:\\Users\\eardo\\Desktop\\Farmscripts\\')

    
os.chdir(indir)
hysplit=pd.read_excel('hysplits.xlsx', converters={'Date':str,'Time':str})
hysplit['Time']=hysplit['Time'].str.strip('  ')


hysplit ['Date'] =[hysplit['Date'][i][0:10] for i in range(len(hysplit['Date']))]
hysplit['Datetime']=hysplit['Date']+" "+ hysplit['Time']

#==============================================================================
hysplit['Datetime']=pd.to_datetime(hysplit['Datetime'])
# hysplit['Date']=pd.to_datetime(hysplit['Date'])
#==============================================================================
alldata=pd.read_csv('alldata_withdates.csv', delimiter =',')
alldata['start_datetime'] = pd.to_datetime(alldata.start_datetime)

West=hysplit.loc[ (hysplit['D1'] == 'W')]
East=hysplit.loc[ (hysplit['D1'] == 'E')]

east_data=pd.DataFrame()

start_date=datetime.date(2016,9,26)
end_date=datetime.date(2016,10,30)

date_list = [start_date + datetime.timedelta(days=x) for x in range(0, 30)]
hysplit.Date = pd.to_datetime(hysplit.Date)
majorD1 = pd.DataFrame(columns=['averageD1'])
outdata=pd.DataFrame()
counter=0
for x in range(len(date_list)):
    W_count=[]
    N_count=[]
    E_count=[]
    S_count=[]
    datemask = hysplit['Date'] == date_list[x]
    #print date_list[x], datemask
    df = hysplit.loc[datemask]['Date']
    if hysplit.loc[datemask]['Date'].empty:
        #print 'empty'
        continue
        
        
    else: 
        W_count.append(sum(hysplit.loc[datemask]['D1'].str.count('W')))
        N_count.append(sum(hysplit.loc[datemask]['D1'].str.count('N')))
        S_count.append(sum(hysplit.loc[datemask]['D1'].str.count('S')))
        E_count.append(sum(hysplit.loc[datemask]['D1'].str.count('E')))
        
        for i in range(len (hysplit.loc[datemask]['D1'].reset_index())):
            #print i
            if len(hysplit.loc[datemask]['D1']) ==0 :
                continue
            else:
                #print hysplit.loc[datemask]
                majorD1  = majorD1.append(hysplit.loc[datemask].reset_index().ix[i], ignore_index = True )
            
            
            if W_count > E_count and W_count >N_count and W_count > S_count:
                #print 'W', W_count
                majorD1['averageD1'][counter] = 'W'
                
            elif E_count > W_count and E_count >N_count and E_count >S_count:
                #print 'E'
                majorD1['averageD1'][counter] = 'E'
                        
            elif N_count > W_count and N_count >E_count and N_count >S_count:
                #print 'N'
                majorD1['averageD1'][counter] = 'N'
                        
            elif S_count > W_count and S_count >E_count and S_count >N_count:
                #print 'S'
                majorD1['averageD1'][counter] = 'S'
            counter +=1

            
majorD1.drop_duplicates('Date', keep = 'last', inplace = True)
majorD1.reset_index(inplace =True)

alldata['date']= np.nan

for i in range (len(alldata['start_datetime'])):
    alldata['date'][i] = alldata['start_datetime'][i].date()
        
        
for i in range(len(majorD1.averageD1)):
        
        date_mask=  alldata['date'] == majorD1.Date[i].date()
        x= alldata.loc[date_mask]
        x['avdir']= majorD1.averageD1[i]
        if alldata.loc[date_mask].empty:
            continue
        else: 
            
            outdata = outdata.append(x, ignore_index=True)

         
east_datamask = outdata['avdir'] == 'E'
west_datamask = outdata['avdir'] == 'W'
north_datamask = outdata['avdir'] == 'N'
south_datamask = outdata['avdir'] == 'S'
fig = plt.figure(figsize=(5, 5))

east_data = outdata.loc[east_datamask]
west_data = outdata.loc[west_datamask]
north_data = outdata.loc[north_datamask]
south_data = outdata.loc[south_datamask]

ax1 = fig.add_subplot(111)
line1 = plt.scatter(east_data['T'], east_data['INP'], color = 'k', label = 'East')
line2 = plt.scatter(west_data['T'], west_data['INP'], color = 'red', label = 'West')
line3 = plt.scatter(north_data['T'], north_data['INP'], color = 'green', label = 'North')
line4= plt.scatter(south_data['T'], south_data['INP'], color= 'b', label ='South')
ax1.yaxis.set_label_position("right")
ax1.yaxis.tick_right()
#ax4 = plt.scatter(south_data['T'], south_data['INP'], color = 'b', label = 'South')

plt.ylim(0.02)
plt.yscale('log')
plt.legend(loc =3)
#plt.title('[INPs] vs. major origin of back trajectory')
plt.xlabel('T ('+degree_sign+'C)')
plt.ylabel('[INP] /L')
#==============================================================================
#             continue
#         
#         else:
#             
#             apsavs=apsavs.append(aps.loc[aps_mask].mean(axis=0), ignore_index=True)
#==============================================================================

              
    #==============================================================================
# for i in range(len(alldata.start_datetime)):
#     print i
#     East_mask=  (  alldata['start_datetime'][i] > East['Datetime']) & (alldata['end_datetime'][i] >= East['Datetime'] )
#     east_data.append(alldata.loc[East_mask])
#==============================================================================