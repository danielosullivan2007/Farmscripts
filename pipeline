#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:47:31 2017

@author: Daniel
"""


import pandas as pd

import glob
import os
from datetime import datetime

#indir = '/Users/Daniel/Desktop/Barbados/'
topdir = 'Y:\\'
indir = 'Y:\\'

a= glob.glob(indir+'/*/')
df_summary=pd.DataFrame(columns = {'start_datetime', 'end_datetime',
                                    'APS_count', 'SMPS_count'})
dict_INPs={}
df_meta=pd.DataFrame()
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
    
    print a
    global df_meta
    global dict_INPs
    if not a:
        no_data_flag=1
        print 'no data files on this day'
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
            print df_meta
        
        
#APS SECTION

    os.chdir(indir+'APS')
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
    print "df_meta", df_meta
    print "aps_total", aps_total
    if no_data_flag==1:
        print 'no data'
    else:    
        df_meta['APS']= aps_total.T

#SMPS Section
    if 'SMPS' in os.listdir(indir):
        df_smps = pd.DataFrame()
        os.chdir(indir+'SMPS')
        z=glob.glob('*.csv')
        if not z:
            print 'no SMPS files on this day'
            
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
                print datetimes
            df_smps.drop('datetime', axis =1, inplace = True)
            df_smps = df_smps.iloc[:,1:].astype(float)
            df_smps.insert(0,'datetimes', datetimes)
           # df_smps.iloc[0:, 1:] = df_smps.iloc[0:, 1:].astype(float)

#Averaging
    smps_avs = pd.DataFrame()
    smps_total=pd.DataFrame()
    for i in range (len(df_meta)):
        #print len(df_meta)
        if df_smps.empty: 
            continue
        else: 
            smps_mask = (df_smps['datetimes'] > df_meta['start'][i]) & (df_smps['datetimes']  <=  df_meta['end'][i])
            if df_smps.loc[smps_mask]['datetimes'].empty:
                    
                continue
            else:
                
                smps_avs=smps_avs.append(df_smps.loc[smps_mask].mean(axis=0, skipna = True), ignore_index=True)
#==============================================================================
#             INP_start, INP_end, last_data, first_data, diff_to_end, diff_from_start = get_t_diffs(smps, smps_mask)
#             timediffs_smps = compile_t_diffs(INP_start, INP_end, last_data, first_data, diff_to_end, diff_from_start)
#==============================================================================
        if no_data_flag==1:
            print 'no data'  
        else:
            frames2 = [smps_avs, df_meta.drop('APS', axis =1)]
            smps_avs = pd.concat (frames2, axis =1, ignore_index= False, join= 'outer')
            print smps_avs
            smps_total = smps_total.append(smps_avs.sum(axis=1), ignore_index=True).T
            smps_total.columns=['SMPS_total']
            cols=smps_avs.columns.tolist()
            cols = cols[-2:] + cols[:-2]
            smps_avs = smps_avs[cols]
            df_meta['SMPS']= smps_total
            return df_meta

df_out = pd.DataFrame()
for i in range(len(a)):
    
    dayfolder=a[i]
    
    os.chdir(dayfolder)
    df_meta=pd.DataFrame()
    
    print dayfolder
    get_data(dayfolder)
    df_out=df_out.append(df_meta)
    
    #get_APSavs(df_meta)
   # print df_meta
#rename to make more readable



'''apsavs = get_APSavs(df_meta)
df_meta, smps_avs = get_smpsavs(df_meta)'''


#==============================================================================
# sql_in = pd.read_sql('select * from summary', con = connection, index_col = 'id')
# for i in range (len(sql_in)):
#         if i ==0:
#             continue
#         
#         write_mask = (df_meta['end_datetime'] != sql_in['end_datetime'][i])
#         if df_meta.loc[write_mask]['end_datetime'].empty:
# 
#             continue
#         else: 
#         
#             to_write = df_meta.loc[write_mask]
#==============================================================================
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('mysql://root:vercetti85@localhost/barbados')
connection = engine.connect()

if df_out.empty:
    pass
else:
    df_out.to_sql('summary', con = connection, if_exists='replace', index = False)   



connection.close()
