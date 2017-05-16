# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 12:10:42 2017
@author: eardo
"""
import matplotlib.pyplot as plt
import numpy as np
import os as os
import scipy.ndimage as ndimage
from matplotlib.gridspec import GridSpec
import datetime
import matplotlib.cm as cm
from scipy.stats import gaussian_kde


'''DATA MUST BE IN LOG BINS BY INP NUMBER'''

import numpy as np
import os as os
import matplotlib.pyplot as plt

import socket
host = socket.gethostname()

if host == 'see4-234':
    #pickdir = ('C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\')
    indir = ('C:\\Users\\eardo\\Desktop\\Farmscripts\\')
    glodir = ('C:\\Users\eardo\\Desktop\\Farmscripts\\glomap data\\160509\\')
elif host == 'Daniels-Air.home':
    pickdir = ('//Users//Daniel//Desktop//farmscripts//Pickels//')
    indir = ('//Users//Daniel//Desktop//farmscripts//')
    #glodir = ('//Users//Daniel//Desktop//farmscripts//glomap data//160509//')


percent = [0.2, 0.5, 0.8]



os.chdir(indir)

'''DMT_T=np.genfromtxt('demott.csv', delimiter = ',')[:,0]
DMT_I=np.genfromtxt('demott.csv', delimiter = ',')[:,1]
DMT_T= DMT_T[np.logical_not(np.isnan(DMT_T))]
DMT_I=DMT_I[np.logical_not(np.isnan(DMT_I))]
pettersup=np.genfromtxt('pettersup.csv', delimiter = ',')
pupT=pettersup[:,0]
pupT= pupT[np.logical_not(np.isnan(pupT))]
pupINP=pettersup[:,1]
pupINP= pupINP[np.logical_not(np.isnan(pupINP))]
pettersdown= np.genfromtxt('pettersdown.csv', delimiter = ',')
pdownT=pettersup[:,0]
pdownT= pupT[np.logical_not(np.isnan(pupT))]
pdownINP=pettersdown[:,1]
pdownINP= pdownINP[np.logical_not(np.isnan(pupINP))]'''


indata= np.genfromtxt('all data_1.csv', delimiter = ',')
inx= indata[:,0]*-1
iny=indata[:,1]
inxy=np.stack([inx,iny])
inz = gaussian_kde(inxy)(inxy)


idx=inz.argsort()
inx, iny, inz =inx[idx], iny[idx], inz[idx]
inz[inz < 0.01] = 'nan'

xedges= np.linspace(5, 30, 70)
yedges  = np.logspace(-2, 2.5, 70)



H, xedges, yedges = np.histogram2d(inx, iny, bins=(xedges, yedges))


sum1=np.sum(H)
H=H/sum1*100
z=np.transpose(H)
degree_sign= u'\N{DEGREE SIGN}'
indata= np.genfromtxt('all data_1.csv', delimiter = ',')




T=inx
INP=iny

x,y=np.meshgrid(xedges[0:-1]*-1,yedges[0:-1])


#Smoothing step
#z = ndimage.gaussian_filter(z, sigma=0.2, order=0)
data2=np.genfromtxt('all data_1.csv',  delimiter=',')
#Change Figure size
fig=plt.figure(figsize= (8,4))

#set levels for contour plot

levels = np.linspace(0.001, np.max(z), 10)
#################################################

#GLOMAP DATA
zero_day = datetime.date(2001,1,1)
start_day = datetime.date(2001, 9, 15)
end_day = datetime.date(2001, 10,31)

felds=pd.read_csv(glodir+'INP_spectra_danny_feldspar.csv', delimiter =',', index_col=0)/1000
day = list(felds.columns)

for i in range(len(day)):
    #day[i]="'"+day[i]+" days'"
    day[i]=int(day[i])
    day[i] = datetime.timedelta(day[i])
    day[i]=day[i]+zero_day


felds = felds.transpose()
felds['date']=day
feld_mask=  (felds['date'] > start_day) & (felds['date'] <=  end_day)
feld_data=felds.loc[feld_mask]

feld_data=felds.loc[feld_mask].T.reset_index()
feld_data['T'] = feld_data['# Temps']*-1
feld_data=feld_data.T
feld_data.columns=list(feld_data.loc['T'])
feld_data.drop('# Temps', inplace = True)
feld_data.set_index('', inplace =True)
feld_data.drop('', inplace =True)


feld_data_stats = pd.DataFrame()
for i in range (len(list(feld_data.columns))):
    feld_data_stats[i]=pd.to_numeric(feld_data.iloc[:,i]).describe(percentiles=percent)

feld_data_stats = feld_data_stats.T
feld_data_stats.index = feld_data_stats.index*-1

marine=pd.read_csv(glodir+'INP_spectra_danny_marine.csv', delimiter =',', index_col=0)/1000
marine=marine.transpose()
marine['date']=day
marine_mask=  (marine['date'] > start_day) & (marine['date'] <=  end_day)
marine_data=marine.loc[marine_mask]

marine_data=marine.loc[marine_mask].T.reset_index()
marine_data['T'] = marine_data['# Temps']*-1
marine_data=marine_data.T
marine_data.columns=list(marine_data.loc['T'])
marine_data.drop('# Temps', inplace = True)
marine_data.set_index('', inplace =True)
marine_data.drop('', inplace =True)



marine_data_stats = pd.DataFrame()
for i in range (len(list(marine_data.columns))):
    marine_data_stats[i]=pd.to_numeric(marine_data.iloc[:,i]).describe(percentiles=percent)
marine_data_stats = marine_data_stats.T
marine_data_stats.index = marine_data_stats.index*-1


Nie=pd.read_csv(glodir+'INP_spectra_danny_m3_Niemand.csv', delimiter =',', index_col=0)/1000
Nie=Nie.transpose()
Nie['date']=day
Nie_mask=  (Nie['date'] > start_day) & (Nie['date'] <=  end_day)
Nie_data=Nie.loc[Nie_mask]

Nie_data=Nie.loc[Nie_mask].T.reset_index()
Nie_data['T'] = Nie_data['# Temps']*-1
Nie_data=Nie_data.T
Nie_data.columns=list(Nie_data.loc['T'])
Nie_data.drop('# Temps', inplace = True)
Nie_data.set_index('', inplace =True)
Nie_data.drop('', inplace =True)



Nie_data_stats = pd.DataFrame()
for i in range (len(list(Nie_data.columns))):
    Nie_data_stats[i]=pd.to_numeric(Nie_data.iloc[:,i]).describe(percentiles=percent)

Nie_data_stats = Nie_data_stats.T
Nie_data_stats.index = Nie_data_stats.index*-1

##################################################
#Setup fig
fig = plt.figure(figsize=(12, 4))
ax2 = fig.add_subplot(131)

ax1 = fig.add_subplot(1,3,2)
p1=ax1.contourf(x,y,z, levels = levels, extend = 'max', cmap ='jet', alpha =1 )
p2=plt.plot(feld_data_stats.index, feld_data_stats['20%'], linewidth =1.5, color = 'k')
p2=plt.plot(feld_data_stats.index, feld_data_stats['80%'], linewidth =1.5, color = 'k')
p2=plt.plot(marine_data_stats.index, marine_data_stats['20%'], linewidth =1.5, color = 'cyan')
p2=plt.plot(marine_data_stats.index, marine_data_stats['80%'], linewidth =1.5, color = 'cyan')
p2=plt.fill_between(feld_data_stats.index, feld_data_stats['20%'],feld_data_stats['80%'], alpha =0.4, color = 'black')
p3=plt.fill_between(marine_data_stats.index, marine_data_stats['20%'],marine_data_stats['80%'], alpha = 0.7)
#ax1.plot(pupT, pupINP)




#p1=ax1.contourf(x,y,z)


ax0 = fig.add_subplot(1,3,3)
p1=ax0.contourf(x,y,z, levels = levels, extend = 'max', cmap ='jet', alpha =1 )
p2=plt.plot(Nie_data_stats.index, Nie_data_stats['20%'], linewidth =1.5, color = 'k')
p2=plt.plot(Nie_data_stats.index, Nie_data_stats['80%'], linewidth =1.5, color = 'k')
p2=plt.fill_between(Nie_data_stats.index, Nie_data_stats['20%'],Nie_data_stats['80%'], alpha =0.4, color = 'black')


cmap = plt.get_cmap()
cmap.set_under('white')



cbaxes=fig.add_axes([1, 0.1, 0.02, 0.8]) 
cb = fig.colorbar(p1, cax = cbaxes, label='% of Total Observations', format ='%0.2f')


    



p2=ax2.plot(data2[:,0],data2[:,1], linewidth=0,marker="o", zorder =0 )
#p2 =ax2.scatter(x, y, c=z, s=40, edgecolor='', cmap='OrRd')

#ax2.scatter(DMT_T,DMT_I, marker="x", color = "red")
#ax0 properties
ax0.set_yscale('log')
ax0.set_xlim(-30,-5)
ax0.set_ylim(0.001,100)
ax0.set_xlabel('T ('+degree_sign+'C)')
ax0.set_ylabel('[INP] /L')
ax0.get_yaxis().set_tick_params(which='both', direction='out')
ax0.get_xaxis().set_tick_params(which='both', direction='out')
ax0.set_title("Niemand", fontsize=14)
ttl0 = ax0.title
ttl0.set_position([.5, 1.05])

#################
#ax1 properties
ax1.set_yscale('log')
ax1.set_xlim(-30,-5)
ax1.set_ylim(0.001,100)
ax1.set_xlabel('T ('+degree_sign+'C)')
ax1.set_ylabel('[INP] /L')
ax1.get_yaxis().set_tick_params(which='both', direction='out')
ax1.get_xaxis().set_tick_params(which='both', direction='out')
ax1.set_title("Feldspar + Marine", fontsize=14)
ttl1 = ax1.title
ttl1.set_position([.5, 1.05])



######################
#ax2 properties


ax2.set_yscale('log')
ax2.set_xlim(-30,-5)
ax2.set_ylim(0.001,100)
ax2.get_yaxis().set_tick_params(which='both', direction='out')
ax2.get_xaxis().set_tick_params(which='both', direction='out')
ax2.set_xlabel('T ('+degree_sign+'C)')
ax2.set_ylabel('[INP] /L')
ax2.set_title("Original Data", fontsize=14)
ttl2 = ax2.title
ttl2.set_position([.5, 1.05])

#####################
#==============================================================================
# otherdata = "/Users/eardo/Desktop/Farmscripts/Past Data"
# os.chdir(otherdata)
# pastdata=np.genfromtxt('Past Data.csv', skip_header=0, delimiter =",")
# Garcia = pastdata[1:,0:2]
# Belosi = pastdata[1:,2:4]
# ax2.scatter(Belosi[:,0],Belosi[:,1], marker="x", color = "red")
# ax2.scatter(Garcia[:,0], Garcia[:,1], marker="x", color = "green")
#==============================================================================


plt.tight_layout()
plt.tight_layout()

fig.savefig('contour.png', dpi=100)
plt.show()