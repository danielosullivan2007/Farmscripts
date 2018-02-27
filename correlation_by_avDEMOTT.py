
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

cols = ['Log10 INPs',
 'Wind speed',
 'Max gust direction',
 'Max gust speed',
 ' Max Gust Ctime',
 'Dry Bulb T',
 'Dew Point T',
 'Grass T',
 'Concrete T',
 'Soil T',
 'Rainfall Total',
 'Radiation Total',
 u'Humidity',
 'rain_past_hour', 
 'smps_total_over500',
 'smps_total_sub500',
 'aps_1um',
 'aps_sub_1um',
 'APS Total',
 'SMPS Total',
 3L,
 4L,
 'log aps_1um',
 'log aps',
 'demott',
 'meyers']
a= float(0.0000594)
b=float(3.33)
c=float(0.0264)
d=float(0.0033)

min_T=-25
max_T=-14

outdata=pd.DataFrame()
step =1

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
aps_list = [i for i in enumerate(aps)]
aps_num =[float(aps_list[i][1]) for i in range(50)]

aps_orig = [(aps_list[i][1]) for i in range(50)]
aps_correct=[(((chi*rho0)/rho)**0.5)*aps_num[i] for i in range(len(aps_num))]
aps_zip= zip(aps_orig, aps_correct)

aps_names = dict(aps_zip)
aps = aps.rename(columns = aps_names)

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
smps_list = [i for i in enumerate(smps)]
smps_num =[float(smps_list[i][1]) for i in range(1, len(smps_list))]

smps_orig = [(smps_list[i][1]) for i in range(1, len(smps_list))]
smps_correct  = [(1/chi)*(smps_num[i]) for i in range(len(smps_num))]
smps_zip= zip(smps_orig, smps_correct)
smps_names = dict(smps_zip)
smps = smps.rename(columns = smps_names)


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
ax1.text(0.025, 40, '(b) Meyers et al. \'92', fontsize=10)


ax.plot(q,r, color = 'b')
ax.plot(q_half,r_half, color = 'b', linestyle = 'dashed')
ax.plot(q_double,r_double, color = 'b', linestyle = 'dashed')
ax.text(0.025, 40, '(a) DeMott et al. \'10', fontsize=10)


T_list=[]
meyers_list=[]
for T in range (min_T,max_T, step):

    df_INP = INPs.loc[INPs['T'] == T]
    #df_INP['timedelta']= df_INP['end_datetime']-df_INP['start_datetime']

    
    df_INPtidy = df_INP.drop([ u'T'], axis =1).reset_index()
    
    df_INPtidy = df_INPtidy.drop('index', axis=1)
    
###############################################################################################################################
#MET AVERAGING 

    dataset_start_t=pd.Series()
    dataset_end_t=pd.Series()
    timediff_end=pd.Series()
    timediff_start=pd.Series()
    t_stamp_INP_start=pd.Series()
    t_stamp_INP_end=pd.Series()
    
    metavs=pd.DataFrame(columns=[u'level_0', u'index',
       u'Dry Bulb Temperature', u'Dew Point Temperature', u'Grass Temperature',
       u'Concrete Temperature', u'10cm Soil Temperature',
       u'Rainfall Total since 0900', u'Radiation Total since 0900',
       u'Humidity'])
    
    
    windavs =pd.DataFrame(columns=['MEAN_WIND_DIR', 'MEAN_WIND_SPEED', 
                                   'MAX_GUST_DIR', 'MAX_GUST_SPEED', 'MAX_GUST_CTIME'])

    apsavs= pd.DataFrame()
    apsavs_1um=pd.DataFrame()
    apsavs_sub_1um=pd.DataFrame()
    
    smps_avs = pd.DataFrame()
    smpsavs_sub500= pd.DataFrame()
    smpsavs_over500= pd.DataFrame()
    aps_sum_down=pd.DataFrame(data={'APS Total':[]})
    aps_sum_accross=pd.DataFrame()
    smps_sum_down=pd.DataFrame(data={'SMPS Total':[]})
    smps_sum_accross=pd.DataFrame()
    
    for i in range (len(df_INPtidy)):
        #print i
        met_mask=(met['datetimes'] > df_INPtidy['start_datetime'][i]) & (met['datetimes'] <=  df_INPtidy['end_datetime'][i])
        if met.loc[met_mask]['datetimes'].empty:
            #print 'pass'
            continue
        else:
            
            metavs = metavs.append(met.loc[met_mask].mean(axis=0), ignore_index=True)
            
# =============================================================================
#             INP_start, INP_end, last_data, first_data, diff_to_end, diff_from_start = get_t_diffs(met, met_mask)
#             timediffs_met = compile_t_diffs(INP_start, INP_end, last_data, first_data, diff_to_end, diff_from_start)
# =============================================================================
        
        
    metavs.drop([u'index',u'level_0'], axis=1)
    
###############################################################################################################################
#SMPS AVERAGING'''        
    dataset_start_t=pd.Series()
    dataset_end_t=pd.Series()
    timediff_end=pd.Series()
    timediff_start=pd.Series()
    t_stamp_INP_start=pd.Series()
    t_stamp_INP_end=pd.Series()
    
    for i in range (len(df_INPtidy)):
        
        smps_mask = (smps['datetimes'] > df_INPtidy['start_datetime'][i]) & (smps['datetimes']  <=  df_INPtidy['end_datetime'][i])
        if smps.loc[smps_mask]['datetimes'].empty:
            
                
            continue
        else:
            
            smps_avs=smps_avs.append(smps.loc[smps_mask].mean(axis=0, skipna = True), ignore_index=True)
            smpsavs_sub500=smpsavs_sub500.append((smps.loc[smps_mask].iloc[:,1:86]).sum(axis=0), ignore_index=True)
            smpsavs_over500=smpsavs_over500.append((smps.loc[smps_mask].iloc[:,86:111]).sum(axis=0), ignore_index=True)
        
        smps_total = smps_avs.sum(axis=1)
        smps_total_over500 = smpsavs_over500.sum(axis=1)
        smps_total_sub500  = smpsavs_sub500.sum(axis=1)
            
        
        smps_total.columns='SMPS_total'
        smps_total_over500.columns='SMPS_total_over500'
        smps_total_sub500.columns='SMPS_total_sub'
        
    #sum accross average down
        smps_mask2=  (smps['datetimes'] > df_INPtidy['start_datetime'][i]) & (smps['datetimes'] <=  df_INPtidy['end_datetime'][i])
        
        smps_mask2 = smps_mask2.reset_index(drop=True)
        if smps.loc[smps_mask2]['datetimes'].empty:
            
            continue
        
        else:
            
            smps_sum_accross=smps.loc[smps_mask2].sum(axis=1)
            
        smps_sum_down.loc[i,:]= [smps_sum_accross.sum(axis=0)]

############################################################################################################################### 
#%% #APS AVERAGING''' 
    dataset_start_t=pd.Series()
    dataset_end_t=pd.Series()
    timediff_end=pd.Series()
    timediff_start=pd.Series()
    t_stamp_INP_start=pd.Series()
    t_stamp_INP_end=pd.Series()
#%%    

    
    cycle=0
    for i in range(len(df_INPtidy)):
        cycle+=1
        aps_mask=  (aps['datetime'] > df_INPtidy['start_datetime'][i]) & (aps['datetime'] <=  df_INPtidy['end_datetime'][i])
        if aps.loc[aps_mask]['datetimes'].empty:
            
            continue
        
        else:
            
            apsavs=apsavs.append(aps.loc[aps_mask].iloc[:, 0:50].sum(axis=0), ignore_index=True)
            apsavs_1um=apsavs_1um.append((aps.loc[aps_mask].iloc[:,13:50]).sum(axis=0), ignore_index=True)
            apsavs_sub_1um=apsavs_sub_1um.append((aps.loc[aps_mask].iloc[:,0:13]).sum(axis=0), ignore_index=True)
        
        aps_total= apsavs.sum(axis=1)
        aps_total_1um = apsavs_1um.sum(axis=1)
        aps_total_sub1um  = apsavs_sub_1um.sum(axis=1)
        
#sum accross average down
        aps_mask2=  (aps['datetime'] > df_INPtidy['start_datetime'][i]) & (aps['datetime'] <=  df_INPtidy['end_datetime'][i])
        aps_mask2 = aps_mask2.reset_index(drop=True)
        check = aps.loc[aps_mask2]['datetimes']
        if aps.loc[aps_mask2]['datetimes'].empty:
            
            continue
        
        else:
            
            aps_sum_accross=aps.loc[aps_mask2].iloc[:,0:50].sum(axis=1)
            
        aps_sum_down.loc[i,:]= [aps_sum_accross.sum(axis=0)]
       # aps_av_down.reset_index(drop=True, inplace = True)
       # aps_av_down.rename(columns={0:'apsm2'}, inplace = True)
############################################################################################################################### 
#%%
#WIND AVERAGING'''     
    dataset_start_t=pd.Series()
    dataset_end_t=pd.Series()
    timediff_end=pd.Series()
    timediff_start=pd.Series()
    t_stamp_INP_start=pd.Series()
    t_stamp_INP_end=pd.Series()
    
    for i in range (len(df_INPtidy)):
        wind_mask=(wind['OB_END_TIME'] > df_INPtidy['start_datetime'][i]) & (wind['OB_END_TIME'] <=  df_INPtidy['end_datetime'][i])
        if  wind.loc[wind_mask]['datetimes'].empty:
            
            continue
        else: 
            
            windavs = windavs.append(wind.loc[wind_mask].mean(axis=0), ignore_index= True)
            
            
    #windavs=windavs.drop(u'Unnamed: 0', axis=1)
    data=pd.concat([df_INPtidy, windavs, metavs, aps_total, aps_total_1um, aps_sum_down, smps_total,smps_sum_down, t_stamp_INP_start, t_stamp_INP_end], axis =1)
    data=data.drop([u'index', 'Datetime', u'level_0', u'MEAN_WIND_DIR', u'MEAN_WIND_DIR'], axis=1)
    data['log aps_1um'] = aps_total_1um.apply(np.log10)
    
    data['log aps'] = aps_total.apply(np.log10)
    
    data['aps_1um'] = aps_total_1um
    data['aps_sub_1um'] = aps_total_sub1um
    data['smps_total_over500'] = smps_total_over500
    data['smps_total_sub500'] = smps_total_sub500
    
    

    
############################################################    
    #DEMOTT Comparison
    data = data[data['Humidity']<RH].reset_index(drop=True)
    
    constant = a*T
    T_kelvin = T+273.16
    T_param=273.16-T_kelvin
    data['demott']=[(a*np.power(T_param,b)*np.power(data.loc[i,'APS Total']/1000,(c*T_param+d))) for i in range(len(data))]
    x=data['INP']
    y=data['demott']
    color = next(colors)
    ax.scatter(x,y,color=color)
    

    data['meyers']=[meyers(T) for i in range(len(data))]
    T_list.append(T)
    meyers_list.append(meyers(T))
    e=data['INP']
    f=data['meyers']
    ax1.scatter(e,f,color=color)
    
    sns.residplot(x,y, ax =ax2, color=color)
    sns.residplot(e,f, ax =ax3, color=color)
    ax2.set_xscale('log')
    ax2.set_xlim(0.02,100)
    ax3.set_xscale('log')

###################################################################################################
#DATA CORRELATION SECTION ####
    '''NOTE LOGGING OF INPS HERE!!!!!!!!!!!!!!'''
    
    data['INP']=data['INP'].apply(np.log10) 
    data.drop([0L, 1L, 2L], inplace=True, axis =1)
   
    
    
    
    corr=data.corr()
   
#==============================================================================
# corr.drop(['Logger Temperature',
#  'Sunshine total since 0900', 'Date', 'Time', ' '], axis = 1, inplace=True)
# 
# corr.drop([ 'Logger Temperature',
#  'Sunshine total since 0900', 'Date', 'Time', ' '], axis =0, inplace=True)
#==============================================================================

    corr.rename(columns = {'INP':'Log10 INPs',u'Dry Bulb Temperature':'Dry Bulb T', u'Dew Point Temperature': 'Dew Point T', u'Grass Temperature':'Grass T', 
    u'Concrete Temperature': 'Concrete T', u'10cm Soil Temperature': 'Soil T', u'Rainfall Total since 0900': 'Rainfall Total',
     u'Radiation Total since 0900': 'Radiation Total',  0L: 'APS Total Count' , 1L: 'SMPS Total Count', u'OB_END_TIME': 'Obs. end Time',  
        u'MEAN_WIND_DIR': 'Av. wind dir',
       u'MEAN_WIND_SPEED':'Wind speed', u'MAX_GUST_DIR':'Max gust direction', u'MAX_GUST_SPEED': 'Max gust speed',
       u'MAX_GUST_CTIME': ' Max Gust Ctime'}, inplace = True)
    
    corr.rename(index = {'INP':'Log10 INPs', u'Dry Bulb Temperature':'Dry Bulb T', u'Dew Point Temperature': 'Dew Point T', u'Grass Temperature':'Grass T', 
    u'Concrete Temperature': 'Concrete T', u'10cm Soil Temperature': 'Soil T', u'Rainfall Total since 0900': 'Rainfall Total',
     u'Radiation Total since 0900': 'Radiation Total',  0L: 'APS Total Count' , 1L: 'SMPS Total Count', u'OB_END_TIME': 'Obs. end Time',  
        u'MEAN_WIND_DIR': 'Av. wind dir',
       u'MEAN_WIND_SPEED':'Wind speed', u'MAX_GUST_DIR':'Max gust direction', u'MAX_GUST_SPEED': 'Max gust speed',
       u'MAX_GUST_CTIME': ' Max Gust Ctime'}, inplace = True)
    corr = corr[cols]
    corr.rename(index = {'aps_1um':'APS < 1 um', 'aps_sub_1um':'APS > 1 um',
                           'smps_total_over500':'SMPS <0.5 um ',  'smps_total_sub500': 'SMPS > 0.5 um',
                           'rain_past_hour':'Rainfall'}, inplace =True)
    
    
    
    data.to_csv(indir+"data at "+num2words[T]+".csv")
    

    
    corr = corr.drop(['APS Total','SMPS Total',3L,4L,'log aps_1um','log aps','demott','meyers'], axis=1)
    corr = corr.drop(['Log10 INPs','APS Total','SMPS Total',3L,4L,'log aps_1um','log aps','demott','meyers'], axis=0)
    corr.to_csv(indir+"corr at" + num2words[T]+".csv")
    data_Temp=data
    data_Temp['Temp']=T    
    outdata =outdata.append(data_Temp)

    print len(data)
    print ('finished adding data @ {}').format(str(T))
    print 'len is {}'.format(len(outdata))
    
    
cbaxes=fig.add_axes([0.95, 0.22, 0.02, 0.6]) 
cb = fig.colorbar(CS3, cax = cbaxes)
cb.ax.invert_yaxis()
cb.ax.set_title('T ('+degree_sign+'C)', fontsize =8)

stats = data.describe()
bins = [stats.loc['min']['INP'], stats.loc['25%']['INP'],stats.loc['50%']['INP'],stats.loc['75%']['INP'],stats.loc['max']['INP']]
groups = ['low', 'medium', ' high', 'v. high']
inp_binned =pd.cut(data['INP'], bins, labels =groups).rename("INP_cat")
data_cat = pd.concat([inp_binned,data], axis =1, join = 'inner').drop([u'INP'], axis =1)

################################################################################
#GRAPHING
fig= ax.get_figure()
fig.savefig(farmdirs['figures']+'demott_param_compare.png', dpi=100) 
            
minus15=pd.read_csv('corr atminus15.csv', index_col='Unnamed: 0')
minus20=pd.read_csv('corr atminus20.csv', index_col='Unnamed: 0')
minus25=pd.read_csv('corr atminus25.csv', index_col='Unnamed: 0')


minus15=pd.read_csv('corr atminus15.csv', index_col='Unnamed: 0')
minus20=pd.read_csv('corr atminus20.csv', index_col='Unnamed: 0')
minus25=pd.read_csv('corr atminus25.csv', index_col='Unnamed: 0')

minus15.drop([' Max Gust Ctime', 'Max gust direction'], axis =1, inplace =True)
minus20.drop([' Max Gust Ctime','Max gust direction'], axis =1, inplace =True)
minus25.drop([' Max Gust Ctime','Max gust direction'], axis =1, inplace =True)

minus15.drop([' Max Gust Ctime', 'Max gust direction'], axis =0, inplace =True)
minus20.drop([' Max Gust Ctime','Max gust direction'], axis =0, inplace =True)
minus25.drop([' Max Gust Ctime','Max gust direction'], axis =0, inplace =True)

x = np.square(minus15.loc['Wind speed':,['Log10 INPs']].values)
y = np.square(minus20.loc['Wind speed':,['Log10 INPs']].values)
z = np.square(minus25.loc['Wind speed':,['Log10 INPs']].values)


fig2, ax2 = plt.subplots(figsize=(6, 5))
ax2= plt.subplot(111)
# 
# 

index = minus15.index
y_pos = np.arange(len(index))

ax2.bar(y_pos-0.2, x, align = 'center', width=0.2, color = 'b', label ='-15 '+degree_sign+'C', edgecolor='black')
ax2.bar(y_pos, y, align = 'center',width=0.2, color = 'r', label ='-20 '+degree_sign+'C', edgecolor='black')
ax2.bar(y_pos+0.2, z, align = 'center',width=0.2, color = 'g', label ='-25 '+degree_sign+'C', edgecolor='black')
plt.xticks(y_pos,index, rotation = 90, fontsize =11)
plt.yticks(fontsize =11)
ax2.set_ylim(0,0.5)
ax2.yaxis.grid()
plt.xlim(-1,15)
plt.legend()
#plt.legend(loc=2, fontsize =10)
plt.ylabel('Coefficient of determination $\mathregular{R^2}$', fontsize =12)
#plt.xlabel()
#plt.title('Correlations between particle no. and meteorological variables')
plt.tight_layout()
plt.savefig(farmdirs['figures']+"\correlations")

#%%
#==============================================================================
# 
# index = corr.index[1:]
# y_pos = np.arange(len(index))
# fig, ax = plt.subplots()
# ax= plt.subplot(111)
# plt.legend(loc=2, fontsize =10)
# plt.ylabel('Pearson R Coefficient')
# plt.ylim(-1,1)
# plt.tight_layout()
# plt.xticks(y_pos,index, rotation = 90)
# ax.bar(y_pos, x)
#==============================================================================


#==============================================================================
# 


# =============================================================================
# import seaborn as sns
# 
# data.index = data[3]
# sns.jointplot('Humidity', 'INP', data = data)
# =============================================================================

os.chdir('C:\\Users\\eardo\\Desktop\\Farmscripts\\')














