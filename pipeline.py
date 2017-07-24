#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:47:31 2017

@author: Daniel
"""

import socket
import pandas as pd
import matplotlib.pyplot as plt
import glob
import numpy as np
import os
import matplotlib.dates as mdates
from datetime import datetime

#barbados
#indir = 'C:\\Users\\useradmin\\Desktop\\Barbados Data'


smps_counter = 0
counter = 0
notes_date=[]
note=[]
notes_loc=[]
host = socket.gethostname()

if host == 'Daniels-MacBook-Air.local':
    indir ="//Users//Daniel//Desktop//farmscripts//test data//"
    indir_INP = indir
    
else:
    indir = 'C:\\Users\\useradmin\\Desktop\\Farm\\Formatted Correctly\\'
    indir_INP = '\\Users\\useradmin\\Desktop\\Farmscripts\\'
    out_folder='C:\\Users\\useradmin\\Desktop\\Farmscripts\\'


a= glob.glob(indir+'/*/')
df_summary=pd.DataFrame(columns = {'start_datetime', 'end_datetime',
                                    'APS_count', 'SMPS_count'})
dict_INPs={}
df_meta=pd.DataFrame()
df_smps=pd.DataFrame()
df_APS=pd.DataFrame(columns =[  u'<0.523', u'0.542',
       u'0.583', u'0.626', u'0.673', u'0.723', u'0.777', u'0.835', u'0.898',
       u'0.965', u'1.037', u'1.114', u'1.197', u'1.286', u'1.382', u'1.486',
       u'1.596', u'1.715', u'1.843', u'1.981', u'2.129', u'2.288', u'2.458',
       u'2.642', u'2.839', u'3.051', u'3.278', u'3.523', u'3.786', u'4.068',
       u'4.371', u'4.698', u'5.048', u'5.425', u'5.829', u'6.264', u'6.732',
       u'7.234', u'7.774', u'8.354', u'8.977', u'9.647', u'10.37', u'11.14',
       u'11.97', u'12.86', u'13.82', u'14.86', u'15.96', u'17.15', u'18.43',
       u'19.81', u'datetime'])
df_APSreader=pd.DataFrame(columns =[  u'<0.523', u'0.542',
       u'0.583', u'0.626', u'0.673', u'0.723', u'0.777', u'0.835', u'0.898',
       u'0.965', u'1.037', u'1.114', u'1.197', u'1.286', u'1.382', u'1.486',
       u'1.596', u'1.715', u'1.843', u'1.981', u'2.129', u'2.288', u'2.458',
       u'2.642', u'2.839', u'3.051', u'3.278', u'3.523', u'3.786', u'4.068',
       u'4.371', u'4.698', u'5.048', u'5.425', u'5.829', u'6.264', u'6.732',
       u'7.234', u'7.774', u'8.354', u'8.977', u'9.647', u'10.37', u'11.14',
       u'11.97', u'12.86', u'13.82', u'14.86', u'15.96', u'17.15', u'18.43',
       u'19.81', u'datetime'])

    
def get_data(indir):
    os.chdir(indir)
    a=glob.glob('Data*')
    global smps_counter, counter,df_smps
    global df_meta, notes_loc, notes_date, notes
    global dict_INPs
    if not a:
        no_data_flag=1
        print 'no NIPI runs with Data *.csv in Dayfolder'
    else:    
        no_data_flag=0
        
        for i in range(len(a)):
            
            #start= a[i][5:11]+"_"+a[i][12:16]
            #end = a[i][5:11]+"_"+a[i][17:21]
            start= a[i][5:11]+"_"+a[i][17:21]
            end = a[i][5:11]+"_"+a[i][22:26]
            
            start_datetime = datetime.strptime(start, '%y%m%d_%H%M')
            end_datetime =  datetime.strptime(end, '%y%m%d_%H%M')
            df_meta= df_meta.append(pd.DataFrame({'start':[start_datetime], 'end':[end_datetime]}),ignore_index = True)
            dict_INPs[start_datetime]=pd.read_csv(a[i], delimiter =",", header =0)
            cols=df_meta.columns.tolist()
            cols = cols[-1:] + cols[:-1]
            df_meta=df_meta[cols]
            #print df_meta
      
    notes_loc = glob.glob(indir+'/*.txt')
    for i in range(len(notes_loc)):
        
        if notes_loc[i] == []:
            continue
        else:
            text_read= open(notes_loc[0],'r')
           
            
            notes_date.append(datetime.strptime(
                    [notes_loc[0].replace(indir,"")][0][0:6], '%y%m%d'))
            note.append(text_read.read())
            print ('comment is {}'.format(note[i]))
    
            

     
#APS SECTION

    os.chdir(indir+'APS')
    #print os.getcwd()
    global df_APS, df_out
    x=glob.glob('*.csv')
    for i in range(len(x)):
        df_APSreader=pd.read_csv(x[i], delimiter =',', header =6).iloc[:, 4:56] 
        df_APSreader['datetime']=pd.to_datetime (pd.read_csv(x[i], delimiter =',', header =6).iloc[:, 1]+" "+
          pd.read_csv(x[i], delimiter =',', header =6).iloc[:, 2])
        df_APS=df_APS.append(df_APSreader)
    cols=df_APS.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df_APS=df_APS[cols]

#Averaging
    apsavs=pd.DataFrame()
    aps_total =pd.DataFrame()
    for i in range(len(df_meta)):
        
        aps_mask=  (df_APS['datetime'] > df_meta['start'][i]) & (df_APS['datetime'] <=  df_meta['end'][i])
        if df_APS.loc[aps_mask]['datetime'].empty:
            
            continue
        
        else:
            
             apsavs = apsavs.append(df_APS.loc[aps_mask].mean(axis=0), ignore_index=True)
             
            #INP_start, INP_end, last_data, first_data, diff_to_end, diff_from_start = 
            
            #get_t_diffs(aps, aps_mask)
            
            #timediffs_aps = compile_t_diffs(INP_start, INP_end, last_data, first_data, diff_to_end, diff_from_start)
    frames1 = [apsavs, df_meta]
    apsavs = pd.concat (frames1, axis =1, ignore_index= False, join= 'outer')
    aps_total= aps_total.append(apsavs.sum(axis=1),ignore_index=True)
    cols=apsavs.columns.tolist()
    cols = cols[-2:] + cols[:-2]
    apsavs = apsavs[cols]
    #print "df_meta", df_meta
    #print "aps_total", aps_total
    if no_data_flag==1:
        print 'no csv files in APS folder'
    else:    
        df_meta['APS']= aps_total.T
         
#SMPS Section
    
    if 'SMPS' in os.listdir(indir):
       
        counter +=1
        
        df_smps = pd.DataFrame()
        os.chdir(indir+'SMPS')
        z=glob.glob('*.csv')
        
        if not z:
            print 'no CSV files in SMPS folder'
            
            
           # df_smps = df_smps.append(x, ignore_index=True)
        else:
            for i in range(len(z)):
                df=pd.read_csv(z[i], delimiter =',', header =25, skip_footer=30)
                df=df.drop(df.index[2:8])
                
    
                df = df.transpose()
                
                df.columns = df.iloc[0][:]
                df=df.drop(df.index[0])
                df['datetime']=pd.to_datetime(df['Date']+" "+df['Start Time'])
                df=df.drop(['Date', 'Start Time'], axis =1)
                
                df_smps = df_smps.append(df, ignore_index=True)
                
                datetimes = df_smps['datetime']
               #print datetimes
            df_smps.drop('datetime', axis =1, inplace = True)
            df_smps = df_smps.iloc[:,1:].astype(float)
            df_smps.insert(0,'datetimes', datetimes)
           # df_smps.iloc[0:, 1:] = df_smps.iloc[0:, 1:].astype(float)

#Averaging
    smps_avs = pd.DataFrame()
    smps_total=pd.DataFrame()
    
    for i in range (len(df_meta)):
        
        #print "length df_meta is {}".format(len(df_meta))
       
        #print "number of cycles is {}".format(i) 
        if df_smps.empty:
            continue
        else: 
            smps_mask = (df_smps['datetimes'] > df_meta['start'][i]) & (df_smps['datetimes']  <=  df_meta['end'][i])
            
        if df_smps.loc[smps_mask]['datetimes'].empty:    
            continue
        else:
            smps_avs=smps_avs.append(df_smps.loc[smps_mask].mean(axis=0, skipna = True), ignore_index=True)
            
           
    smps_total = smps_total.append(smps_avs.sum(axis=1), ignore_index=True).T
    #print smps_total
    smps_total.columns=['SMPS_total']
    
    cols=smps_avs.columns.tolist()
    cols = cols[-2:] + cols[:-2]
    smps_avs = smps_avs[cols]
    df_meta['SMPS']= smps_total
            
            #print "smps total count is {}".format(smps_total.tail(1))
                 #print 'Warning: SMPS averages is zero for {}'.format(dayfolder)
    
    return df_meta
            

df_out = pd.DataFrame()
for i in range(len(a)):
    
    dayfolder=a[i]
    print ('Analyzing {}').format(datetime.strftime(datetime.strptime(a[i][52:58],'%y%m%d'),'%d-%m-%y'))
    os.chdir(dayfolder)
    df_meta=pd.DataFrame()
    #pdb.set_trace()
    #print dayfolder
    get_data(dayfolder)
    df_out=df_out.append(df_meta)



#%%

os.chdir(indir_INP)
INPs = pd.read_csv('INPs.csv',delimiter =',')
INPs.dropna(axis =0, inplace = True)
INPs.dropna(axis =0, inplace = True)

def timefix(time):
    
    correct_time = datetime.strptime(str((time)), '%Y-%m-%d %H:%M:%S')
    return correct_time

INPs['start']=INPs['start'].apply(timefix)
INPs['end']=INPs['end'].apply(timefix)


df_out.reset_index(inplace = True)

#%%
df_INP=pd.DataFrame()
for i in range(len(df_out)):
        INP_mask=  (INPs['start'] == df_out['start'][i]) & (INPs['end'] ==  df_out['end'][i])
        if INPs.loc[INP_mask].empty:
            print 'empty'
            continue
        
        else:
            
             df_INP = df_INP.append(INPs.loc[INP_mask], ignore_index=True)
             
df_out['INPs'] =df_INP['INP']
#df_out.dropna(axis=0, inplace = True)
#%%
df_out['Date']=df_out.start.dt.date
notes_out =pd.DataFrame ([i for i in zip(notes_date, note)], 
                          columns =['date', 'note'])
notes_out.date=pd.to_datetime(notes_out.date)
notes_out.index = notes_out.date

df_out = df_out.drop(u'level_0', errors ='ignore').set_index('Date').join(
        notes_out.set_index('date'),  how ='left')
df_out.drop(df_out.columns[0], axis =1, inplace =True)
#%%
fig, ax1 = plt.subplots()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
ax1.plot(df_out['end'],df_out['SMPS'], color = 'blue')

#plt.legend(loc = 'upper left', bbox_to_anchor = (1,1))  
ax1.plot(df_out['end'],df_out['APS']*100, color = 'green')
ax1.legend(loc = 'upper left', bbox_to_anchor = (0,1))   
ax2= ax1.twinx()
end=np.asarray(df_out['end'])
INP=np.asarray(df_out['INPs'])

ax2.scatter(end, INP, color = 'red')
ax2.legend(loc = 'upper left', bbox_to_anchor = (0,1)) 
ax1.set_ylabel('particles cm$^{-3}$')
ax2.set_yscale('log')
ax2.set_ylim(1,100)
ax1.set_xlabel('Date')
ax2.set_ylabel('INPs L$^{-1}$')

#ax1 = ax1.plot_date(df_out['end'],df_out['INPs'])[0]
#plt.legend(loc = 'upper right', bbox_to_anchor = (0.985,0.85))  

#%%    
#==============================================================================
# from sqlalchemy import create_engine
# import pandas as pd
# engine = create_engine('mysql://root:vercetti85@localhost/barbados')
# connection = engine.connect()
# 
# if df_out.empty:
#     pass
# 
# else:
#     df_out.to_sql('summary', con = connection, if_exists='replace', index = False)   
# 
# 
# 
# connection.close()
# 
#==============================================================================
