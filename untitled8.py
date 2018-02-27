# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 15:27:26 2018

@author: eardo
"""


# -*- coding: utf-8 -*-
"""
Created on Wed May 03 18:03:08 2017

@author: eardo
"""
import pandas as pd
import numpy as np
import os as os
import glob 
import matplotlib.pyplot as plt
import decimal 
import matplotlib.cm as cm
from directories import farmdirs
import itertools
from matplotlib import rc
from myfuncs import degree_sign, num2words
import  seaborn as sns


chi=1.2
rho0=1
rho=2.4

key_terms= ["Data"]


a= float(0.0000594)
b=float(3.33)
c=float(0.0264)
d=float(0.0033)

min_T=-25
max_T=-10

outdata=pd.DataFrame()
step =5

RH=100 #RH for all plots

indir = farmdirs['pickels']
indir2 = farmdirs['home']

# Using contourf to provide my colorbar info, then clearing the figure
Z = [[0,0],[0,0]]
levels = range(min_T,max_T+step,step)
CS3 = plt.contourf(Z, levels, cmap= 'jet')
plt.clf()

fig, (ax, ax1) =plt.subplots(1,2, sharey=True, figsize =(5,2.5))
fig1, (ax2, ax3) =plt.subplots(1,2, figsize =(5,2.5), sharey=True, sharex=True)

def meyers(Tcelcius):
    A=-0.639
    B=0.1296
    T=Tcelcius+273.15
    p_water = np.exp(54.842763-6763.22/T - 4.21*np.log(T) + 0.000367*T + np.tanh(0.0415*(T - 218.8))*(53.878- 1331.22/T - 9.44523*np.log(T) + 0.014025*T))
    p_ice = np.exp(9.550426 - 5723.265/T + 3.53068*np.log(T) - 0.00728332*T )
    ice_ss = (p_water/p_ice)-1
    meyers_inp = np.exp(A+100*B*(ice_ss))
    
    return meyers_inp
######################################################################################################
#==============================================================================
# indir = ('W:\SMPS')
# 
# os.chdir(indir)
# df_smps = pd.DataFrame(columns= ['NaT',u'Date', u'Start Time',u' 14.1', u' 14.6',u' 15.1',u' 15.7',u' 16.3',
#  u' 16.8',u' 17.5', u'514.0',u'532.8',u'552.3',u'572.5',u'593.5',u'615.3',u'637.8',u'661.2',u'685.4', u'710.5'])
# a=glob.glob('*.csv')
# 
# for i in range(len(a)):
#     df=pd.read_csv(a[9], delimiter =',', header =25, skip_footer=30)
#     df=df.drop
#     df.loc[-1] = pd.to_datetime(df.iloc[0][1:]+" "+df.iloc[1][1:])
#     df.index = df.index + 1  # shifting index
#     df = df.sort()  # sorting by index
#     df = df.transpose()
#     df=df.set_index(df[0])
#     df.columns = df.iloc[0][:]
#     df=df.drop(df.index[0])
#     df_smps = df_smps.append(df)
# 
# df_smps.to_pickle('C:\Users\eardo\Desktop\Farmscripts\Pickels\smps.p')
#==============================================================================
#########################################################################################################
#==============================================================================
# indir = ('W:\APS')
# 
# os.chdir(indir)
# 
# a=glob.glob('*.csv')
# df_out=pd.DataFrame(columns =[u'Date', u'Start Time', u'Aerodynamic Diameter', u'<0.523', u'0.542',
#        u'0.583', u'0.626', u'0.673', u'0.723', u'0.777', u'0.835', u'0.898',
#        u'0.965', u'1.037', u'1.114', u'1.197', u'1.286', u'1.382', u'1.486',
#        u'1.596', u'1.715', u'1.843', u'1.981', u'2.129', u'2.288', u'2.458',
#        u'2.642', u'2.839', u'3.051', u'3.278', u'3.523', u'3.786', u'4.068',
#        u'4.371', u'4.698', u'5.048', u'5.425', u'5.829', u'6.264', u'6.732',
#        u'7.234', u'7.774', u'8.354', u'8.977', u'9.647', u'10.37', u'11.14',
#        u'11.97', u'12.86', u'13.82', u'14.86', u'15.96', u'17.15', u'18.43',
#        u'19.81', u'datetime'])
# 
# for i in range(len(a)):
#     df=pd.read_csv(a[i], delimiter =',', header =6).iloc[:, 1:56]
#     df['datetime']=pd.to_datetime(df['Date']+" "+df['Start Time'])
#     df=df.drop(u'Aerodynamic Diameter', axis=1)
#     df_out = df_out.append(df)
# 
# df_out.to_pickle(indir+"APS.p")
#==============================================================================




##############################################################################################################################
#indir = ('/Users/Daniel/Desktop/Farmscripts/Pickels/')
#indir = ('C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\')
os.chdir(indir)
aps=pd.read_pickle(indir+"aps.p")

aps['datetimes']=aps.datetime
x=list(aps.iloc[:,0:51])
y = [float(i) for i in x]
y.sort()
x= [str(i) for i in y]
z=list(aps)[51:]
x.extend(z)
aps=aps[x]

aps = aps.reset_index(drop = True)
INPs =pd.read_pickle(indir+"INPs.p")
met = pd.read_pickle(indir+ "met.p")

met.reset_index(inplace=True)
met.rename(columns ={'Datetime':'datetimes'}, inplace =True)
met['rain_past_hour']=met['Rainfall Total since 0900'].diff(periods=1)
for i in range(len(met)):
    if met['Time'][i] == '09:00':
        met.rain_past_hour[i] = np.nan



wind = pd.read_pickle(indir+ "wind.p")
wind.reset_index(inplace=True)
wind.rename({'OB_END_TIME':'datetimes'}, inplace=True)
wind['datetimes']=wind.OB_END_TIME
smps = pd.read_pickle(indir+"SMPS.p")
#smps=smps.drop([u'<0.523', u'Aerodynamic Diameter', u'Date',
       #u'Start Time'], axis =0)

smps = smps.rename(columns ={'index':'datetime'})
range_T=range(min_T,max_T, step)
len_T=len(range_T)
colors = iter(cm.jet(np.linspace(0, 1, len_T)))

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Observed INPs ($\mathregular{L^{-1}}$)')
ax.set_ylabel('Predicted INPs ($\mathregular{L^{-1}}$)')
ax.set_xlim(0.02,100)
ax.set_ylim(0.02,100)
 


q=[0.001,100]
r=[0.001,100]
ax.plot(q,r)


ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xlabel('Observed INPs ($\mathregular{L^{-1}}$)')
#ax1.set_ylabel('Predicted INPs $\mathregular{L^{-1}}$')
ax1.set_xlim(0.02,100)
ax1.set_ylim(0.02,100)
 
q=[0.01,100]
r=[0.01,100]

q_half=[0.01, 100]
r_half=[0.02, 200]

q_double=[0.01, 100]
r_double=[0.005, 50]





ax1.plot(q,r)
ax1.plot(q_half,r_half, color = 'b', linestyle = 'dashed')
ax1.plot(q_double,r_double, color = 'b', linestyle = 'dashed')
ax1.text(0.03, 40, '(b) Meyers 1992', fontsize=10)


ax.plot(q,r, color = 'b')
ax.plot(q_half,r_half, color = 'b', linestyle = 'dashed')
ax.plot(q_double,r_double, color = 'b', linestyle = 'dashed')
ax.text(0.03, 40, '(a) Demott 2010', fontsize=10)


T_list=[]
meyers_list=[]