
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
topfolder='W:\\'
key_terms= ["Data"]



a= float(0.0000594)
b=float(3.33)
c=float(0.0264)
d=float(0.0033)
import seaborn as sns

sns.set_context("paper", rc={"font.size":12,"axes.titlesize":12,"axes.labelsize":12}) 
degree_sign= u'\N{DEGREE SIGN}'
import socket
host = socket.gethostname()
if host == "Daniels-Air.home":
    indir ="//Users//Daniel//Desktop//farmscripts//pickels//"
elif host == 'see4-234':
    indir = 'C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\'
    indir2 = 'C:\\Users\\eardo\\Desktop\\Farmscripts\\'
elif host ==  'SEE-L10840':
    indir = ('C:\\Users\\useradmin\\Desktop\\Farmscripts\\Pickels\\')
    indir2 = ('C:\\Users\\useradmin\\Desktop\\Farmscripts\\')


def get_t_diffs(dataset, mask):

                INP_start = df_INPtidy['start_datetime'][i]
                INP_end = df_INPtidy['end_datetime'][i]
                
                first_data = dataset.loc[mask]['datetimes'].iloc[0]
                last_data = dataset.loc[mask]['datetimes'].iloc[-1]
                
                diff_from_start = dataset.loc[mask]['datetimes'].iloc[0] - df_INPtidy['start_datetime'][i]
                diff_to_end= dataset.loc[mask]['datetimes'].iloc[-1] - df_INPtidy['end_datetime'][i] 
                
                return INP_start, INP_end, last_data, first_data, diff_to_end, diff_from_start

                

def compile_t_diffs(INP_start, INP_end, last_data, first_Data, diff_to_end, diff_from_start):

    t_stamp_INP_end.set_value(i, INP_end)
    t_stamp_INP_start.set_value(i, INP_start)
    
    dataset_start_t.set_value(i, first_data)
    dataset_end_t.set_value(i, last_data)
    
    timediff_start.set_value(i, diff_from_start)
    timediff_end.set_value(i, diff_to_end)
    timediffs = pd.concat([ t_stamp_INP_start, dataset_start_t, timediff_start, t_stamp_INP_end , dataset_end_t, timediff_end ], axis=1)
    timediffs.columns =['t_stamp_INP_start', 'dataset_start_t', 'timediff_start', 't_stamp_INP_end' , 'dataset_end_t', 'timediff_end' ]
    return timediffs


#timediffs=pd.DataFrame( columns= ['timediff_start', 't_stamp_INP_start', 'timediff_end', 't_stamp_INP_end'])

num2words={-15:'minus15',-16:'minus16',-17:'minus17',-18:'minus18',
           -19:'minus19',-20:'minus20',-21:'minus21',
           -22:'minus22', -23:'minus23', -24:'minus24',-25: 'minus25'}
           


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

for T in range (-25,-14, 1):
    len_T=len(range(-25,-14, 1))
    

    df_INP = INPs.loc[INPs['T'] == T]
    print T
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

    apsavs= pd.DataFrame(columns =[u'0.542', u'0.583', u'0.626', u'0.673', u'0.723', u'0.777', u'0.835',
           u'0.898', u'0.965', u'1.037', u'1.114', u'1.197', u'1.286', u'1.382',
           u'1.486', u'1.596', u'1.715', u'1.843', u'1.981', u'10.37', u'11.14',
           u'11.97', u'12.86', u'13.82', u'14.86', u'15.96', u'17.15', u'18.43',
           u'19.81', u'2.129', u'2.288', u'2.458', u'2.642', u'2.839', u'3.051',
           u'3.278', u'3.523', u'3.786', u'4.068', u'4.371', u'4.698', u'5.048',
           u'5.425', u'5.829', u'6.264', u'6.732', u'7.234', u'7.774', u'8.354',
           u'8.977', u'9.647', u'<0.523', u'Aerodynamic Diameter', u'Date',
           u'Start Time', u'datetime'])

    smps_avs = pd.DataFrame(columns = [u'datetime',    u' 14.1',    u' 14.6',    u' 15.1',    u' 15.7',
              u' 16.3',    u' 16.8',    u' 17.5',    u' 18.1',    u' 18.8',
              u'358.7',    u'371.8',    u'385.4',    u'399.5',    u'414.2',
              u'429.4',    u'445.1',    u'461.4',    u'478.3',    u'495.8'])
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
            
            INP_start, INP_end, last_data, first_data, diff_to_end, diff_from_start = get_t_diffs(met, met_mask)
            timediffs_met = compile_t_diffs(INP_start, INP_end, last_data, first_data, diff_to_end, diff_from_start)
        
        
    metavs.drop([u'index', u'Unnamed: 0',u'level_0'], axis=1)
    
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
            INP_start, INP_end, last_data, first_data, diff_to_end, diff_from_start = get_t_diffs(smps, smps_mask)
            timediffs_smps = compile_t_diffs(INP_start, INP_end, last_data, first_data, diff_to_end, diff_from_start)
        
        smps_total = smps_avs.sum(axis=1)
        smps_total.columns='SMPS_total'
        
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
   
    cycle=0
    for i in range(len(df_INPtidy)):
        cycle+=1
        aps_mask=  (aps['datetime'] > df_INPtidy['start_datetime'][i]) & (aps['datetime'] <=  df_INPtidy['end_datetime'][i])
        if aps.loc[aps_mask]['datetimes'].empty:
            
            continue
        
        else:
            
            apsavs=apsavs.append(aps.loc[aps_mask].mean(axis=0), ignore_index=True)
            INP_start, INP_end, last_data, first_data, diff_to_end, diff_from_start = get_t_diffs(aps, aps_mask)
            timediffs_aps = compile_t_diffs(INP_start, INP_end, last_data, first_data, diff_to_end, diff_from_start)
        aps_total= apsavs.sum(axis=1)
        
#sum accross average down
        aps_mask2=  (aps['datetime'] > df_INPtidy['start_datetime'][i]) & (aps['datetime'] <=  df_INPtidy['end_datetime'][i])
        aps_mask2 = aps_mask2.reset_index(drop=True)
        check = aps.loc[aps_mask2]['datetimes']
        if aps.loc[aps_mask2]['datetimes'].empty:
            
            continue
        
        else:
            
            aps_sum_accross=aps.loc[aps_mask2].iloc[:,0:52].sum(axis=1)
            
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
            INP_start, INP_end, last_data, first_data, diff_to_end, diff_from_start = get_t_diffs(wind, wind_mask)
            timediffs_wind = compile_t_diffs(INP_start, INP_end, last_data, first_data, diff_to_end, diff_from_start)
            
    windavs=windavs.drop(u'Unnamed: 0', axis=1)
    data=pd.concat([df_INPtidy, windavs, metavs, aps_total, aps_sum_down, smps_total,smps_sum_down, t_stamp_INP_start, t_stamp_INP_end], axis =1)
    data=data.drop([u'index', 'Datetime', u'Unnamed: 0', u'level_0',u'start_datetime',
                     u'end_datetime', u'MEAN_WIND_DIR', u'MEAN_WIND_DIR'], axis=1)
    
    
    
    colors = iter(cm.jet(np.linspace(0, 1, len_T)))
    constant = a*T
    T_kelvin = T+273.16
    T_param=273.16-T_kelvin
    data['demott']=[(a*np.power(T_param,b)*np.power(data[0][i],(c*T_param+d))) for i in range(len(data[0]))]
    print data['demott']
    fig =plt.plot()
    ax=plt.gca()
    x=data['INP']
    y=data['demott']
    ax.scatter(x,y,color=next(colors))
    
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Observed INP /L')
    ax.set_ylabel('Predicted INP /L')
    ax.set_xlim(0.1,100)
    ax.set_ylim(0.1,100)
    q=[0.001,100]
    r=[0.001,100]
    ax.plot(q,r)

    #del t_stamp_INP_end,t_stamp_INP_start, timediff_end, timediff_start, 
###################################################################################################
#DATA CORRELATION SECTION 
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
    
    
    data.to_csv(indir+"data at "+num2words[T]+".csv")
    corr.to_csv(indir+"corr at" + num2words[T]+".csv")


stats = data.describe()
bins = [stats.loc['min']['INP'], stats.loc['25%']['INP'],stats.loc['50%']['INP'],stats.loc['75%']['INP'],stats.loc['max']['INP']]
groups = ['low', 'medium', ' high', 'v. high']
inp_binned =pd.cut(data['INP'], bins, labels =groups).rename("INP_cat")
data_cat = pd.concat([inp_binned,data], axis =1, join = 'inner').drop([u'INP'], axis =1)

################################################################################
#GRAPHING
fig= ax.get_figure()
fig.savefig(indir2+'demott_param_compare.png', dpi=100) 
            
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

x = np.square(minus15.loc['Wind speed':'SMPS Total',['Log10 INPs']].values)
y = np.square(minus20.loc['Wind speed':'SMPS Total',['Log10 INPs']].values)
z = np.square(minus25.loc['Wind speed':'SMPS Total',['Log10 INPs']].values)

#%%
fig, ax = plt.subplots(figsize=(6, 5))
ax= plt.subplot(111)


indata= np.genfromtxt('all data_1.csv', delimiter = ',')

index = minus15.index
index = index[1:14]
y_pos = np.arange(len(index))
ax.bar(y_pos-0.2, x, align = 'center', width=0.2, color = 'b', label ='-15 '+degree_sign+'C', edgecolor='black')
ax.bar(y_pos, y, align = 'center',width=0.2, color = 'r', label ='-20 '+degree_sign+'C', edgecolor='black')
ax.bar(y_pos+0.2, z, align = 'center',width=0.2, color = 'g', label ='-25 '+degree_sign+'C', edgecolor='black')
plt.xticks(y_pos,index, rotation = 90, fontsize =11)
plt.yticks(fontsize =11)
ax.set_ylim(0,1)
ax.yaxis.grid()
plt.xlim(-1,14)
plt.legend()
#plt.legend(loc=2, fontsize =10)
plt.ylabel('Coefficient of determination $\mathregular{R^2}$', fontsize =12)
#plt.xlabel()
#plt.ylabel('Pearson R Coefficient')
#plt.title('Correlations between particle no. and meteorological variables')
plt.tight_layout()
plt.savefig(indir+"\correlations")

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
# INPs.to_csv('C:\\Users\\eardo\\Desktop\\Farmscripts\\alldata_withdates.csv')
# 
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# import graphviz
# 
# target, predictors = data_cat.loc[:,u'INP_cat'], data_cat.loc[:,'MEAN_WIND_SPEED':]
# predictors.fillna(value =0, inplace =True)
# X_train, X_test, y_train, y_test = train_test_split(
# predictors, target,  random_state=42)
# tree = DecisionTreeClassifier(max_depth =2, random_state=0)
# tree.fit(X_train, y_train)
# print("Accuracy on training set: {:.3f}".format(tree.score(X_train, y_train)))
# print("Accuracy on test set: {:.3f}".format(tree.score(X_test, y_test)))
# 
# from sklearn.tree import export_graphviz
# export_graphviz(tree, out_file="tree.dot", class_names = groups,
#  feature_names=predictors.columns, impurity=False, filled=True)
# 
# with open("tree.dot") as f:
#  dot_graph = f.read()
# graphviz.Source(dot_graph)
# 
# 
#==============================================================================



















