# -*- coding: utf-8 -*-
"""
Created on Wed Oct 05 12:20:24 2016

@author: py15asm
"""
''' This code takes the data from the OPC N2 and the APS and compares it. You need the starting time of both diveices be the same. Then you set the starting time and the end time over you want to average (in minutes, better to use integers) and you get the plot of both readings. You can make the data smoother or not by changing one parameter in the end of the code). The APS data has to be in concentration.'''
import numpy as np
import matplotlib.pyplot as plt
from directories import farmdirs
import pylab
import pandas as pd
import datetime
#%%

chi=1.2
rho0=1
rho=1.5



'''minutes all aver you want to average'''
start=0
end=26
'''title of the plot'''
title='160930 roof vs intlet morning'+'.png'
'''OPCN2 data''' 

OPCdlogDp=[0.152610163,0.159700843,0.129094696,0.105915499,0.074292326,0.114573221,0.161150909,0.124938737,0.096910013,0.113943352,0.09017663,0.096910013,0.079181246,0.06694679,0.057991947,0.038918066]
OPCbincenter=np.array([0.460000008,0.659999996,0.914999962,1.194999993,1.465000033,1.829999983,2.534999967,3.5,	4.5,	5.75,	7.25,	9,	11,	13,	15,	16.75])
#name of the OPC file
dataOPCN2=np.genfromtxt(farmdirs['pickels']+'OPC_outside.csv',delimiter=',',skip_header=20,dtype=np.float64)
dfOPC = pd.read_csv(farmdirs['pickels']+'OPC_outside.csv',delimiter=',',skiprows=19)
dfOPC.dropna(axis =0, how = 'any', inplace =True)
dt1= datetime.datetime(2016, 9, 30, 12, 13, 27)
dt2= datetime.datetime(2016, 9, 30, 12, 39, 07)
aps = pd.read_pickle(farmdirs['pickels']+'aps.p')


#delimiter to indicate how the data are separated (coma in csv)
#skip header skips the number of lines you set. data type sets the type

a=start*60
b=end*60
OPCN2=dataOPCN2[a:b,1:17]
OPCN2flow=dataOPCN2[a:b,23]
OPCN2counting=np.array(OPCN2.sum(axis=0))
for i in range(0,(b-a)):
   for j in range(0,15):
       OPCN2[i,j]=OPCN2[i,j]/OPCN2flow[i]   
OPCN2avg=OPCN2.mean(axis=0)
OPCN2davg=np.divide(OPCN2avg,OPCdlogDp)
OPCN2avgflow=np.mean(OPCN2flow[i])
errOPCN2=np.sqrt(OPCN2counting)/(OPCdlogDp)
errOPCN2=errOPCN2/(OPCN2avgflow*(b-a))


aps_mask=  (aps['datetime'] > dt1) & (aps['datetime'] <=  dt2)
aps = aps.loc[aps_mask]

aps_mod = aps.T.reset_index()[0:50]
aps_mod.rename(columns = {'index':'sizes'}, inplace =True)
aps_mod.sizes = pd.to_numeric(aps_mod.sizes)
aps_mod.sizes=(((chi*rho0)/rho)**0.5)*aps_mod.sizes

aps_mod.sort_values(by=['sizes'], inplace =True)
aps_mod['logsize']=aps_mod.sizes.apply(np.log10)
aps_mod['blow'] = aps_mod.logsize.diff()
aps_mod.iloc[:,1:] = aps_mod.iloc[:,1:]/(aps_mod['blow'])
aps_mod.drop(['logsize','blow'], axis =1, inplace =True)
aps_mod['mean'] = aps_mod.iloc[:,1:].mean(axis =1)

'''plotting'''
f, (ax1, ax2) = plt.subplots(1, 2, sharey=False, figsize =(6,2.5))  
dt1 =datetime.datetime
ax2.errorbar(OPCbincenter, OPCN2davg,yerr=errOPCN2, label='_nolegend_', ls='none')
ax2.plot(OPCbincenter, OPCN2davg,label='OPC',marker='o',
         lw=0, markerfacecolor='c')
ax2.plot(aps_mod['sizes'], aps_mod['mean'], marker ='o', lw=0, label = 'APS (inlet)')
#plt.errorbar(APSbincenter, APSdavg,label='APS')

#end of the smoothing

ax2.set_xlabel('Particle Size D$\mathregular{_p} (\mu m $)', fontsize =8)
ax2.set_ylabel('dN/dlogDp (cm$^{-3}$)', fontsize = 8)
ax2.set_xlim([0.1,100])
ax2.set_ylim([0.0001,50])
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")
plt.yscale('log')
plt.xscale('log')
ax2.legend(numpoints =1, fontsize=8)
#ax2.grid(which ='both')
#plt.title(title)
#pylab.savefig('OPC in the roof vs APS inlet.png')




inlet_calc = pd.read_csv(farmdirs['pickels']+'inlet_eff.csv')
inlet_pm10 = pd.read_csv(farmdirs['pickels']+'inlet_pm10.csv')
x=inlet_calc['size_um']
y = inlet_calc['percent']



ax1.plot(x, y, label = 'Splitter \nefficiency (Calc.)')
ax1.set_xlim([0.1,100])
ax1.set_ylabel('% Transmission', fontsize = 8)
ax1.set_xlabel('Particle Size D$\mathregular{_p} (\mu m $)', fontsize =8)
ax1.set_xscale('log')
#ax1.grid(which ='both')

x=inlet_pm10['Size']
y = inlet_pm10['Percent']*100
ax1.plot(x,y, label = 'PM10 Head \n efficiency')
ax1.legend(loc=3, fontsize =8, numpoints =1)







