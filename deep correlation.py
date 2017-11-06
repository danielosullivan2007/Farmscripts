# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:10:58 2017

@author: useradmin
"""
import numpy as np
import pandas as pd
import seaborn as sns
import os
import glob as glob
from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler()
#from bokeh import mpl
from bokeh.plotting import figure
from bokeh.charts import TimeSeries, output_file, show
import matplotlib.pyplot as plt

import socket
host= socket.gethostname()

if host == 'see4-234':
    picdir = 'C:\\Users\\eardo\\Desktop\\farmscripts\\Pickels\\'
    figdir= 'C:\\Users\\eardo\\Desktop\\farmscripts\\Figures\\'
else:

    picdir = 'C:\\Users\\useradmin\\Desktop\\Farmscripts\\Pickels\\'
    figdir = 'C:\\Users\\useradmin\\Desktop\\Farmscripts\\Figures\\'

os.chdir(picdir)
#figdir =  

to_import  = glob.glob('*data at minus*.csv')
names = ['Temp','Unnamed: 0',
 'INP',
 'MEAN_WIND_SPEED',
 'MAX_GUST_DIR',
 'MAX_GUST_SPEED',
 'MAX_GUST_CTIME',
 'Dry Bulb Temperature',
 'Dew Point Temperature',
 'Grass Temperature',
 'Concrete Temperature',
 '10cm Soil Temperature',
 'Rainfall Total since 0900',
 'rain_past_hour',
 'Radiation Total since 0900',
 'Humidity',
 'APS Total',
 'SMPS Total',
 '3',
 'demott']


df = pd.DataFrame(columns = names)


for i in range(len(to_import)):
    x = pd.read_csv(to_import[i])
    x['Temp']=-1*float(to_import[i][13:15])
    join =   [df, x]
    df = pd.concat(join).drop('Unnamed: 0', axis =1)

df = df[['3','Temp', 'INP',
         '10cm Soil Temperature',
 'APS Total',
 'Concrete Temperature',
 'Dew Point Temperature',
 'Dry Bulb Temperature',
 'Grass Temperature',
 'Humidity',
 'MAX_GUST_CTIME',
 'MAX_GUST_DIR',
 'MAX_GUST_SPEED',
 'MEAN_WIND_SPEED',
 'Radiation Total since 0900',
 'Rainfall Total since 0900',
 'rain_past_hour',
 'SMPS Total',
 'demott']].rename(columns ={'3':'Date'})


df.drop( ['MAX_GUST_CTIME','MAX_GUST_DIR', 'demott','10cm Soil Temperature'])
df.Date= pd.to_datetime(df['Date'])
df.reset_index(inplace =True, drop =True)
df.dropna(inplace =True)
df.set_index('Date')
df = df[df['APS Total']<10000]

df['log_APS'] = df['APS Total'].apply(np.log10)
#]
T = -25
df_T = df[df['Temp']== T].reset_index(drop=True)

#removing high APS points, normalize
df_plot = df_T[df_T['APS Total']<10000]
df_plot.reset_index(drop = True, inplace =True)


df_tonorm=df_plot.loc[:,'INP':]
cols=df_plot.loc[:,'INP':].columns.values
min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(df_tonorm)
df_normalized = pd.DataFrame(np_scaled)
df_normalized.columns = cols

df_normalized['Date']=df_T['Date']
df_normalized.drop 
bins=[0,1]
values = []
df_normalized['Rain'] = df_normalized['Rainfall Total since 0900']>0
#==============================================================================
# sns.pairplot(data =df_apstrim, y_vars=['INP'],
#              x_vars= ['Humidity','Dry Bulb Temperature' ,'MEAN_WIND_SPEED','Rainfall Total since 0900'])   
# sns.pairplot(data =df_apstrim, y_vars=['INP'],
#              x_vars= ['SMPS Total','log_APS'])   
# #sns.residplot('INP', 'log_APS', data =df_apstrim)
# 
# 
#==============================================================================
cols= df_plot.columns.values.tolist()
x=[i for i in enumerate(cols)]
choice1= 0
choice2= 4



fig1, ax1 = plt.subplots()
ax1= sns.lmplot(x=cols[choice1], y =cols[choice2], data = df_normalized, hue='Rain',
           fit_reg=False)

fig2, ax2=plt.subplots()
sns.lmplot(x=cols[choice1], y =cols[choice2], data = df_normalized)



p1 = figure(x_axis_type="datetime",x_axis_label = 'Date', y_axis_label = 'Min_Max Normalized Variable',
            title="Time Series for T = {}".format(T),plot_width=1000)
#p1.scatter(x= df_normalized['Date'], y=df_normalized['SMPS Total'], legend ='SMPS Total')
p1.line(x= df_normalized['Date'], y=df_normalized[cols[choice2]],color ='red', legend = cols[choice2], alpha =0.4)
p1.scatter(x= df_normalized['Date'], y=df_normalized[cols[choice2]],color ='red', legend = cols[choice2])
#
#p1.scatter(x= df_normalized['Date'], y=df_normalized[cols[18]],color = 'black', legend = cols[18])
#p1.line(x= df_normalized['Date'], y=df_normalized[cols[18]],color = 'black', legend = cols[18], alpha =0.2)

p1.scatter(x= df_normalized['Date'], y=df_normalized[cols[choice1]],color = 'black', legend = cols[choice1])
p1.line(x= df_normalized['Date'], y=df_normalized[cols[choice1]],color = 'black', legend = cols[choice1], alpha =0.4)

#p1.scatter(x= df_normalized['Date'], y=df_normalized[cols[9]],color = 'blue', legend = cols[9])
#p1.line(x= df_normalized['Date'], y=df_normalized[cols[9]],color = 'blue', legend = cols[9], alpha =0.2)

output_file(figdir+'timeseries.html')
show(p1)



