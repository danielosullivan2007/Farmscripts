# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 12:10:42 2017
@author: eardo
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os as os
import scipy.ndimage as ndimage
from matplotlib.gridspec import GridSpec
import datetime
import matplotlib.cm as cm
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from matplotlib.ticker import LogFormatter 
from matplotlib.ticker import LogFormatterMathtext 
import myfuncs
'''DATA MUST BE IN LOG BINS BY INP NUMBER'''

import numpy as np
import os as os
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import socket

from directories import farmdirs
host = socket.gethostname()
highruns_unheated_df =pd.DataFrame(columns = ['T', 'INPs_perL', 'F', 'K', 'INPs_perdrop', 
                             'INPerr_pos', 'INPerr_neg', 'delta_INP_pos',
                             'delta_INP_neg'])

##############################################################################


indir =farmdirs['home']
picdir= farmdirs['pickels']
glodir = farmdirs['glodir1']

    
percent = [0.2, 0.5, 0.8]



os.chdir(indir)

'''
#Paramaterisations
DMT_T=np.genfromtxt('demott.csv', delimiter = ',')[:,0]
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


indata= np.genfromtxt(picdir+'INPs_trim_witherrs_reorder.csv', delimiter = ',', skip_header=1)[:,1:]
indata = np.delete(indata, 1, 0)
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



T=inx
INP=iny

x,y=np.meshgrid(xedges[0:-1]*-1,yedges[0:-1])



#data2=np.genfromtxt('all data_1.csv',  delimiter=',')
'''#Change Figure size'''
fig=plt.figure(figsize= (8,4))

'''#set levels for contour plot'''
levels = np.linspace(0.001, np.max(z), 10)
#################################################
'''#GLOMAP DATA'''
zero_day = datetime.date(2001,1,1)
start_day = datetime.date(2001, 9, 15)
end_day = datetime.date(2001, 10,31)

data_key2=pd.read_csv (picdir+'heat_INPs_trim_witherrs.csv', delimiter =',')
felds=pd.read_csv(glodir+'INP_spectra_danny_feldspar.csv', delimiter =',', index_col='Temp')/1000

#felds.drop(labels ='date', axis=1, inplace =True)
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




#found = av_between(start_day, end_day, felds, felds['date'])

feld_data=felds.loc[feld_mask].T.reset_index()
feld_data['T'] = feld_data['Temp']*-1
feld_data=feld_data.T
feld_data.columns=list(feld_data.loc['T'])
feld_data.drop('Temp', inplace = True)
feld_data.set_index('', inplace =True)
feld_data.drop('', inplace =True)


feld_data_stats = pd.DataFrame()
for i in range (len(list(feld_data.columns))):
    feld_data_stats[i]=pd.to_numeric(feld_data.iloc[:,i]).describe(percentiles=percent)

feld_data_stats = feld_data_stats.T
feld_data_stats.index = feld_data_stats.index*-1


#%%

felds_int = pd.read_csv(glodir + 'INP_spectra_danny_m3_feldspar-Leeds_internally_mixed.csv',delimiter =',', index_col='Temp')/1000
felds_int= felds_int.transpose()
felds_int['date']=day

felds_int_data = myfuncs.av_between(start_day, end_day, felds_int, felds_int['date']).T.reset_index()
felds_int_data['T'] = felds_int_data['Temp']*-1
felds_int_data=felds_int_data.T
felds_int_data.columns=list(felds_int_data.loc['T'])
felds_int_data.drop('Temp', inplace = True)
felds_int_data.set_index('', inplace =True)
felds_int_data.drop('', inplace =True)

felds_int_stats = pd.DataFrame()
for i in range (len(list(felds_int_data.columns))):
    felds_int_stats[i]=pd.to_numeric(felds_int_data.iloc[:,i]).describe(percentiles=percent)

felds_int_stats = felds_int_stats.T
felds_int_stats.index = felds_int_stats.index*-1

#%%

marine=pd.read_csv(glodir+'INP_spectra_danny_marine.csv', delimiter =',', index_col='Temp')/1000
marine=marine.transpose()
marine['date']=day
marine_mask=  (marine['date'] > start_day) & (marine['date'] <=  end_day)
marine_data=marine.loc[marine_mask]

marine_data=marine.loc[marine_mask].T.reset_index()
marine_data['T'] = marine_data['Temp']*-1
marine_data=marine_data.T
marine_data.columns=list(marine_data.loc['T'])
marine_data.drop('Temp', inplace = True)
marine_data.set_index('', inplace =True)
marine_data.drop('', inplace =True)



marine_data_stats = pd.DataFrame()
for i in range (len(list(marine_data.columns))):
    marine_data_stats[i]=pd.to_numeric(marine_data.iloc[:,i]).describe(percentiles=percent)
marine_data_stats = marine_data_stats.T
marine_data_stats.index = marine_data_stats.index*-1



Nie=pd.read_csv(glodir+'INP_spectra_danny_m3_Niemand.csv', delimiter =',', index_col='Temp')/1000
Nie=Nie.transpose()
Nie['date']=day
Nie_mask=  (Nie['date'] > start_day) & (Nie['date'] <=  end_day)
Nie_data=Nie.loc[Nie_mask]


Nie_data=Nie.loc[Nie_mask].T.reset_index()
Nie_data['T'] = Nie_data['Temp']*-1
Nie_data=Nie_data.T
Nie_data.columns=list(Nie_data.loc['T'])
Nie_data.drop('Temp', inplace = True)
Nie_data.set_index('', inplace =True)
Nie_data.drop('', inplace =True)


Nie_data_stats = pd.DataFrame()
for i in range (len(list(Nie_data.columns))):
    Nie_data_stats[i]=pd.to_numeric(Nie_data.iloc[:,i]).describe(percentiles=percent)

Nie_data_stats = Nie_data_stats.T
Nie_data_stats.index = Nie_data_stats.index*-1
Nie_data_stats.drop ([  0,  -1,  -2,  -3,  -4,  -5,  -6,  -7,  -8,  -9, -10, -11,-12], inplace = True)

#%%
#Setup fig
fig = plt.figure(figsize=(8, 4))
#ax2 =ORIGINAL DATA
#ax2 = fig.add_subplot(131)
#p2=ax2.plot(data2[:,0],data2[:,1], linewidth=0,marker="o", zorder =0 


#%%


'''*********************Feld with heat************************************************'''
ax1 = fig.add_subplot(1,2,1)
p2=ax1.contourf(x,y,z, levels = levels, extend = 'max', cmap ='jet', alpha =1 )
p2=plt.plot(feld_data_stats.index, feld_data_stats['20%'], linewidth =0.5, color = 'k')
p2=plt.plot(feld_data_stats.index, feld_data_stats['80%'], linewidth =0.5, color = 'k')



p2=plt.scatter(data_key2['T'], data_key2['INPs_perL'], color='red', zorder=1)
p2=plt.plot(marine_data_stats.index, marine_data_stats['20%'], linewidth =1, color = 'cyan')
p2=plt.plot(marine_data_stats.index, marine_data_stats['80%'], linewidth =1, color = 'cyan')
p2=plt.fill_between(feld_data_stats.index, feld_data_stats['20%'],feld_data_stats['80%'], alpha =0.4, 
                    color = 'black',
                    label = 'Feldspar')
p2=plt.fill_between(felds_int_stats.index, felds_int_stats['20%'],felds_int_stats['80%'], alpha =0.4, 
                    color = 'green',
                    label = 'Feldspar Internally Mixed')
p2=plt.fill_between(marine_data_stats.index, marine_data_stats['20%'],marine_data_stats['80%'],
                    label = 'Marine' , alpha = 0.7)

p2=plt.plot(felds_int_stats.index, felds_int_stats['20%'],linewidth =1.5, color = 'green')
p2=plt.plot(felds_int_stats.index, felds_int_stats['80%'], linewidth =1.5, color = 'green')
blue_patch = mpatches.Patch(alpha =0.85 , label='Marine', lw =1.5,edgecolor ='cyan' ,facecolor='blue')

gray_patch = mpatches.Patch(alpha =0.85 , label='Feldspar Ext.', lw =1,edgecolor ='k' ,facecolor='gray')
green_patch = mpatches.Patch(alpha =0.85 , label='Feldspar Int.', lw =1,edgecolor ='green' ,facecolor='green')
red_circle = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="red", label = 'heated')
plt.legend(handles=[blue_patch, gray_patch, green_patch, red_circle], prop={'size':8}, loc=3)


#################
#ax1 properties
ax1.set_yscale('log')
ax1.set_xlim(-34,-5)
ax1.set_ylim(0.005,90)
ax1.set_xlabel('T ('+degree_sign+'C)')
ax1.set_ylabel('[INPs] ($\mathregular{L^{-1}}$)')
ax1.get_yaxis().set_tick_params(which='both', direction='out')
ax1.get_xaxis().set_tick_params(which='both', direction='out')
#ax1.set_title("Feldspar + Marine", fontsize=14)
ttl1 = ax1.title
ttl1.set_position([.5, 1.05])
ax1.text(.9,.9,'(a)',
    horizontalalignment='right',
    transform=ax1.transAxes, fontsize =14)


'''*********************NIEMAND w/ heat************************************************'''
ax3 = fig.add_subplot(1,2,2)
p1=ax3.contourf(x,y,z, levels = levels, extend = 'max', cmap ='jet', alpha =1 )
p2=plt.plot(Nie_data_stats.index, Nie_data_stats['20%'], linewidth =0.5, color = 'k')
p2=plt.plot(Nie_data_stats.index, Nie_data_stats['80%'], linewidth =0.5, color = 'k')
p2=plt.scatter(data_key2['T'], data_key2['INPs_perL'], color='red', zorder=1)
p2=plt.fill_between(Nie_data_stats.index, Nie_data_stats['20%'],Nie_data_stats['80%'], alpha =0.4, color = 'black')
blue_patch = mpatches.Patch(  alpha =0.85 , label='Marine', lw =1.5,edgecolor ='cyan' ,facecolor='blue')
gray_patch = mpatches.Patch(  alpha =0.85 , label='Niemand', lw =1,edgecolor ='k' ,facecolor='gray')
#red_circle = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="red", label = 'heated')

plt.legend(handles=[ gray_patch, red_circle], prop={'size':8},loc=3)
ax3.set_yscale('log')
ax3.set_xlim(-34,-5)
ax3.set_ylim(0.005,90)
ax3.set_xlabel('T ('+degree_sign+'C)')

#ax0.set_ylabel('[INP] /L')
ax3.get_yaxis().set_tick_params(which='both', direction='out')
ax3.get_xaxis().set_tick_params(which='both', direction='out')
#ax0.set_title("Niemand", fontsize=14)
#ttl0 = ax0.title
#ttl0.set_position([.5, 1.05])
ax3.set_yticklabels([])

cmap = plt.get_cmap()
cmap.set_under('white')

cbaxes=fig.add_axes([1, 0.3, 0.02, 0.6]) 
cb = fig.colorbar(p1, cax = cbaxes, label='% of Total Observations', format ='%0.2f')
ticks =cb.locator()


ax3.text(.9,.9,'(b)',
    horizontalalignment='right',
    transform=ax3.transAxes, fontsize =14)
#p2 =ax2.scatter(x, y, c=z, s=40, edgecolor='', cmap='OrRd')

#ax2.scatter(DMT_T,DMT_I, marker="x", color = "red")
#ax0 properties




######################
#ax2 (original data) properties


#==============================================================================
# ax2.set_yscale('log')
# ax2.set_xlim(-34,-5)
# ax2.set_ylim(0.001,100)
# ax2.get_yaxis().set_tick_params(which='both', direction='out')
# ax2.get_xaxis().set_tick_params(which='both', direction='out')
# ax2.set_xlabel('T ('+degree_sign+'C)')
# ax2.set_ylabel('[INP] /L')
# ax2.set_title("Original Data", fontsize=14)
# ttl2 = ax2.title
# ttl2.set_position([.5, 1.05])
#==============================================================================

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
#==============================================================================
# xticks = ax1.xaxis.get_major_ticks()
# xticks[0].label1.set_visible(False)
# xticks[-1].label1.set_visible(False)
#==============================================================================
xticks = ax1.xaxis.get_major_ticks()
xticks[0].label1.set_visible(False)
xticks[-1].label1.set_visible(False)

yticks = ax3.yaxis.get_major_ticks()
yticks[0].label1.set_visible(False)
yticks[-1].label1.set_visible(False)

plt.tight_layout(h_pad=0, w_pad= 0)

fig.savefig('contour.png', dpi=100)
plt.show()

###################################################################
'''Figure 1 in paper. High Runs and Low Runs come from
'''


lowruns_heated_data = pd.read_csv(picdir+'lowruns_heated_data.csv',names = ['T', 'INPs_perL', 'F', 'K', 'INPs_perdrop', 
                             'INPerr_pos', 'INPerr_neg', 'delta_INP_pos',
                             'delta_INP_neg']).dropna(axis =0)
    
#FILTER   
lowruns_heated_data['neg_mag'] = lowruns_heated_data.loc[:,'INPerr_neg'].apply(np.log10)-lowruns_heated_data.loc[:,'INPs_perL'].apply(np.log10)
lowruns_heated_data['neg_mag'] = lowruns_heated_data.loc[:,'neg_mag'].apply(np.absolute)
lowruns_heated_data = lowruns_heated_data [lowruns_heated_data.loc[:,'neg_mag']<1]

####################################################################

highruns_heated_data = pd.read_csv(picdir+'highruns_heated_data.csv',names = ['T', 'INPs_perL', 'F', 'K', 'INPs_perdrop', 
                             'INPerr_pos', 'INPerr_neg', 'delta_INP_pos',
                             'delta_INP_neg']).dropna(axis =0)
highruns_heated_data['neg_mag'] = highruns_heated_data.loc[:,'INPerr_neg'].apply(np.log10)-highruns_heated_data.loc[:,'INPs_perL'].apply(np.log10)
highruns_heated_data['neg_mag'] = highruns_heated_data.loc[:,'neg_mag'].apply(np.absolute)
highruns_heated_data = highruns_heated_data [highruns_heated_data.loc[:,'neg_mag']<1]
  
    
####################################################################
lowruns_unheated_data = pd.read_csv(picdir+'lowruns_unheated_data.csv',names = ['T', 'INPs_perL', 'F', 'K', 'INPs_perdrop', 
                             'INPerr_pos', 'INPerr_neg', 'delta_INP_pos',
                             'delta_INP_neg']).dropna(axis =0)
    
    
lowruns_unheated_data['neg_mag'] = lowruns_unheated_data.loc[:,'INPerr_neg'].apply(np.log10)-lowruns_unheated_data.loc[:,'INPs_perL'].apply(np.log10)
lowruns_unheated_data['neg_mag'] = lowruns_unheated_data.loc[:,'neg_mag'].apply(np.absolute)
lowruns_unheated_data = lowruns_unheated_data [lowruns_unheated_data.loc[:,'neg_mag']<1]

####################################################################


highruns_unheated_data = pd.read_csv(picdir+'highruns_unheated_data.csv',names = ['T', 'INPs_perL', 'F', 'K', 'INPs_perdrop', 
                             'INPerr_pos', 'INPerr_neg', 'delta_INP_pos',
                             'delta_INP_neg']).dropna(axis =0)
    
    
highruns_unheated_data['neg_mag'] = highruns_unheated_data.loc[:,'INPerr_neg'].apply(np.log10)-highruns_unheated_data.loc[:,'INPs_perL'].apply(np.log10)
highruns_unheated_data['neg_mag'] = highruns_unheated_data.loc[:,'neg_mag'].apply(np.absolute)
highruns_unheated_data = highruns_unheated_data [highruns_unheated_data.loc[:,'neg_mag']<1]
#all_data=np.genfromtxt(indir+'all_data.csv',  delimiter=',')

fig1=plt.figure(figsize=(10,3))
#==============================================================================
# ax0=plt.subplot(141)
# plt.scatter(all_data[:,0], all_data[:,1], color ='grey')
# ax0.set_ylabel('[INP] /L'),ax0.set_xlabel('T ('+degree_sign+'C)')
# degree_sign= u'\N{DEGREE SIGN}'
# ax0.get_yaxis().set_tick_params(which='both', direction='out')
# ax0.get_xaxis().set_tick_params(which='both', direction='out')
# ax0.text(-29, 0.015, '(a)', fontsize = 12)
# plt.yscale('log'),plt.xlim(-30,-5), plt.ylim(0.01, 50)
# 
#==============================================================================



plt.gca().yaxis.get_major_ticks()[1].label1.set_visible(False)
#plt.gca().xaxis.get_major_ticks()[-1].label1.set_visible(False)
        

ax1=plt.subplot(141)
p1=ax1.contourf(x,y,z, levels = levels, extend = 'max', 
                cmap ='jet', alpha =1 )

plt.yscale('log'), plt.xlim(-30,-5), plt.ylim(0.01, 300)
#plt.gca().xaxis.get_major_ticks()[-1].label1.set_visible(False)
ax1.set_xlabel('T ('+degree_sign+'C)')
ax1.set_ylabel('[INPs] ($\mathregular{L^{-1}}$)')
#ax1.axes.get_yaxis().set_ticks([])

xticks = ax1.xaxis.get_major_ticks()
xticks[0].set_visible(False)
#xticks[-1].label1.set_visible(False)
plt.title('(a) All Data')
formatter = LogFormatterMathtext(10, labelOnlyBase=False) 
cbaxes=fig1.add_axes([0.085, -0.03, 0.2, 0.05]) 

ticks = [ 0.001 ,  0.1786346 ,   0.35626921,
          0.53390381,   0.71153841]
cb = fig1.colorbar(p1, cax = cbaxes,ticks=ticks, label='% of Total Observations',
                   orientation ='horizontal', format ='%0.1f')
#ax1.text(-29, 0.015, '(a)', fontsize = 12)


ax5=plt.subplot(142)
p1=ax5.contourf(x,y,z, levels = levels, extend = 'max', cmap ='jet', alpha =1 )
ax5.scatter(data_key2['T'], data_key2['INPs_perL'], s=14, color='red', zorder=1, label = 'Heated')
plt.yscale('log'), plt.xlim(-30,-5), plt.ylim(0.01, 300)
#plt.gca().xaxis.get_major_ticks()[-1].label1.set_visible(False)
ax5.axes.get_yaxis().set_ticks([])
ax5.set_xlabel('T ('+degree_sign+'C)')
xticks = ax5.xaxis.get_major_ticks()
xticks[0].set_visible(False)
plt.legend(fontsize =8)
plt.title('(b) Heated samples')

markersize ='4'
elinewidth = '0.3'
ax6=plt.subplot(143)
yerr = (lowruns_heated_data['delta_INP_neg'],lowruns_heated_data['delta_INP_pos'])
plt.errorbar(lowruns_heated_data['T'], lowruns_heated_data['INPs_perL'], yerr=yerr, fmt ='o',
             color ='red', elinewidth = elinewidth,markersize= markersize, label = 'Heated')

yerr = (lowruns_unheated_data['delta_INP_neg'],lowruns_unheated_data['delta_INP_pos'])
plt.errorbar(lowruns_unheated_data['T'], lowruns_unheated_data['INPs_perL'], yerr=yerr, 
             fmt ='o',elinewidth = elinewidth, markersize = markersize, label ='Unheated')

plt.yscale('log'), plt.xlim(-30,-5), plt.ylim(0.01, 300)
ax6.set_xlabel('T ('+degree_sign+'C)')

ax6.axes.get_yaxis().set_ticks([])
xticks = ax6.xaxis.get_major_ticks()
xticks[0].set_visible(False)


plt.axvline(-20, linestyle ='dashed', color ='k')
#ax3.text(-29, 0.015, '(c)', fontsize = 12)
plt.legend(fontsize =8)
plt.title('(c) Small effect')

ax7=plt.subplot(144)
#plt.scatter(highruns_heated_data[:,0], highruns_heated_data[:,1], s=14, color ='red', label = 'Heated')
#plt.scatter(highruns_unheated_data[:,0], highruns_unheated_data[:,1], s=14, color ='black', label ='Untreated')
yerr = (highruns_heated_data['delta_INP_neg'],highruns_heated_data['delta_INP_pos'])
plt.errorbar(highruns_heated_data['T'], highruns_heated_data['INPs_perL'], 
             elinewidth = elinewidth, yerr=yerr, fmt ='o', color = 'red',markersize=markersize, label ='Heated')

yerr = (highruns_unheated_data['delta_INP_neg'],highruns_unheated_data['delta_INP_pos'])
plt.errorbar(highruns_unheated_data['T'], highruns_unheated_data['INPs_perL'], yerr=yerr, fmt ='o',
             elinewidth = elinewidth,markersize=markersize, label ='Unheated')

plt.yscale('log'), plt.xlim(-30,-5), plt.ylim(0.01, 300)
ax7.set_xlabel('T ('+degree_sign+'C)')
ax7.axes.get_yaxis().set_ticks([])
xticks = ax7.xaxis.get_major_ticks()
xticks[0].set_visible(False)
plt.legend(fontsize =8)
plt.title('(d) Large effect')

plt.axvline(-20, linestyle ='dashed', color ='k')


subplots=[ax1, ax5, ax6, ax7]
for ax in subplots:
    ax.get_yaxis().set_tick_params(which='both', direction='out')
    ax.get_xaxis().set_tick_params(which='both', direction='out')
plt.tight_layout(h_pad=0, w_pad= 0)   


out = 'C:\\Users\\eardo\\Desktop\\To upload\\'
plt.savefig(out+'test.png')

