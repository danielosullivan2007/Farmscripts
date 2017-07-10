
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 18:57:49 2017

@author: eardo
"""

from glob import glob
import os
import matplotlib.pyplot as plt
import numpy as np
import numpy.ma as ma
import datetime as datetime
import pandas as pd
#Create Keylist for globbing
data = pd.DataFrame()
key = ["heat"]
degree_sign= u'\N{DEGREE SIGN}'

figfold='C:\\Users\\eardo\\Desktop\\Farmscripts\\Figures\\'

#==============================================================================
# '''Changes to required directory'''
# if host == 'see4-234':
#     #pickdir = ('C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\')
#     indir = ('C:\\Users\\eardo\\Desktop\\Farmscripts\\')
#     glodir = ('C:\\Users\eardo\\Desktop\\Farmscripts\\glomap data\\160509\\')
# elif host == 'Daniels-Air.home':
#     pickdir = ('//Users//Daniel//Desktop//farmscripts//Pickels//')
#     indir = ('//Users//Daniel//Desktop//farmscripts//')
#     #glodir = ('//Users//Daniel//Desktop//farmscripts//glomap data//160509//')
#==============================================================================

#Glob each subfolder
def globber(topfolder, key_terms):
    found_files=[]
    
    os.chdir(topfolder)
    a=glob('*\\')
    for ifolder in range(len(a)):
        os.chdir(topfolder+ a[ifolder])
        
        #search for files containing keywords       
        files_in_folder=glob('*.csv')
        #print "found " +str(len(filelist))+" files"
        
        for s in range(len(files_in_folder)):
            if key_terms[0] in files_in_folder[s]:
                
                #print "looking for phrase "+str(key_terms[0])+" in: "+files_in_folder[s]
                found_files.append(files_in_folder[s])
                
    return found_files, a
            #frame_in=np.genfromtxt(filelist[s], delimiter = ",", usecols=(0,1))

def get_datetimes(filelist):
    start_key=[]
    end_key=[]
    start =[]
    end=[]
    for s in range(len(filelist)):
            x= np.datetime64("20"+filelist[s][5:7] + "-"+filelist[s][7:9]+"-"+filelist[s][9:11]+"T"+
                                           filelist[s][17:19]+":"+filelist[s][19:21])
            start_key.append(x)
            
            y = np.datetime64("20"+filelist[s][5:7] + "-"+filelist[s][7:9]+"-"+filelist[s][9:11]+"T"+
                                           filelist[s][22:24]+":"+filelist[s][24:26])
            end_key.append(y)
            '''the below line generates a list of datetimes as long as the input data'''
            #for i in range (len(frame_in)):
                #end.append(x)
                #start.append(y)
                
    return start_key, end_key

   
#Glob top folder
topfolder='X:\\'
os.chdir(topfolder)
folders=glob('*\\')
filelist=[]
out1=np.empty(shape=(1,2))
out2=np.empty(shape=(1,2))
out3=np.empty(shape=(1,2))
all_data_corresp=np.empty(shape=(1,4))
highruns_unheated_data=np.empty(shape=(1,4))
highruns_heated_data=np.empty(shape=(1,4))

out1[:] = np.NAN
out2[:] = np.NAN
out3[:] = np.NAN
all_data_corresp[:] = np.NAN
files_analyzed=[]
files_key1=[]
files_key2=[]
found_files=[]



start_key1=[]
end_key1=[]
start_key2=[]
end_key2=[]
end_1=[]
start_1=[]
end2=[]
start2=[]
filesloc_key2=[]
folderloc_key2=[]
pulled_from_bulk=[]
#Glob each subfolder
n=0
############################################################
#This section Searches for a keyword both in and not in files
for ifolder in range(len(folders)):
    
    os.chdir(topfolder+ folders[ifolder])
    #search for files containing keywords
    filelist=glob('*.csv')
    #print "found " +str(len(filelist))+" files"
    #print filelist
    for s in range(len(filelist)):
        n+=1

        files_analyzed.append(filelist[s])
        #print n
        if "heat" not in filelist[s]:
               #print "looking for phrase "+str(key[0])+" in: "+filelist[s]
            files_key1.append(filelist[s])
            frame_in1=np.genfromtxt(filelist[s], delimiter = ",", usecols=(0,1))
            
            filename_in1 = filelist[s]
            

            
            x= np.datetime64("20"+filelist[s][5:7] + "-"+filelist[s][7:9]+"-"+filelist[s][9:11]+"T"+
                                           filelist[s][17:19]+":"+filelist[s][19:21])
            
            start_key1.append(x)
            
            #print start_key2
            #print len(start_key2)
            y = np.datetime64("20"+filelist[s][5:7] + "-"+filelist[s][7:9]+"-"+filelist[s][9:11]+"T"+
                                           filelist[s][22:24]+":"+filelist[s][24:26])
            end_key1.append(y)
            
            for i in range (len(frame_in1)):
                end_1.append(x)
                start_1.append(y)
            out1=np.concatenate((out1,frame_in1))
            
            
        elif "heat" in filelist[s]:
            
            
            filesloc_key2.append(filelist[s])
            
            folderloc_key2.append(os.getcwd()+'\\')
            frame_in2=np.genfromtxt(filelist[s], delimiter = ",", usecols=(0,1))
            
            filename_in2 = filelist[s]
            
            
            x= np.datetime64("20"+filelist[s][5:7] + "-"+filelist[s][7:9]+"-"+filelist[s][9:11]+"T"+
                                           filelist[s][17:19]+":"+filelist[s][19:21])
            
            start_key2.append(x)
            

            y = np.datetime64("20"+filelist[s][5:7] + "-"+filelist[s][7:9]+"-"+filelist[s][9:11]+"T"+
                                           filelist[s][22:24]+":"+filelist[s][24:26])
            end_key2.append(y)
            
            for i in range (len(frame_in2)):
                end2.append(x)
                start2.append(y)
            out2=np.concatenate((out2,frame_in2))

            
out1=pd.DataFrame(out1, columns =['T', 'INP']).drop(0) #for non heated files
dfstart1 = pd.DataFrame(start_1, columns = ['start'])
dfstart1.index +=1          
dfend1 = pd.DataFrame(end_1, columns = ['end'])                
dfend1.index +=1
data_key1=pd.concat([out1, dfstart1, dfend1], axis =1)
            
out2=pd.DataFrame(out2, columns =['T', 'INP']).drop(0) #for heated files
dfstart2 = pd.DataFrame(start2, columns = ['start'])
dfstart2.index +=1          
dfend2 = pd.DataFrame(end2, columns = ['end'])                
dfend2.index +=1

data_key2=pd.concat([out2, dfstart2, dfend2], axis =1)
del frame_in1, frame_in2, filelist,   n, s, x, y, out1, out2, out3, 
del i, end2, end_1, end_key1, end_key2, dfstart1, dfstart2, filename_in1, filename_in2, 
del data, dfend1, dfend2


################################################################
#   THIS SECTION 1) GETS DATETIMES FROM ALL THE BULK FILES, 
#                2) GETS DATETIMES FOR FILES WHICH MATCHED WITH 
#                3) CREATES A MASK TO SELECT DATA FILES IN THE BULK DATABASE, 
#                 WHICH MATCH WITH THOSE IDENTIFIED IN THE KEYWORD FOLDER (IN THIS CASE 'HEATED')
#                4)PLOTS OUTPUT DATA, SAVES FIGURES
#
#                
bulk_indir= "W:\\"
#os.chdir(bulk_indir)
out_bulk=np.empty(shape=(1,4))

out_bulk[:] = np.NAN
bulk_files, bulk_folders = globber(bulk_indir, 'Data' )
bulk_start_i, bulk_end_i = get_datetimes(bulk_files)
bulk_elements_starttimes=[]
bulk_elements_endtimes=[]
files_to_pull=[]
bulk_run_start=[]
bulk_run_end=[]
bulk_run_folderloc=[]
bulk_run_fileloc=[]
bulk_run_loc=[]
match_word2_run_start=[]


#1) GETS DATETIMES FROM ALL THE BULK FILES,
#HERE, RUN REFERS TO THE START AND END TIME POINTS ON THE FILE, 
#ELEMENT REFERS TO THE TIMESTAMP FOR EACH DATA POINT"" 
for i in range(len(bulk_folders)):
    os.chdir(bulk_indir+bulk_folders[i])
    
    bulk_data_list= glob('*.csv')
    
    for csv in range(len(bulk_data_list)):
        if 'Data' in bulk_data_list[csv]:
            file_info=[bulk_data_list[csv]]
            q, r = get_datetimes([bulk_data_list[csv]])
            bulk_run_folderloc.append(os.getcwd()+'\\')
            bulk_run_fileloc.append(bulk_data_list[csv])
            a= (q - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 's')
            b=(r - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 's')
            bulk_run_start.append(datetime.datetime.utcfromtimestamp(a)), bulk_run_end.append(datetime.datetime.utcfromtimestamp(b))
            frame=np.genfromtxt(bulk_data_list[csv], delimiter=',')
            for i in range (len(frame)):
                x,y, =get_datetimes(file_info)
                
                bulk_elements_starttimes.append(x)
                bulk_elements_endtimes.append(y)
                
            #print bulk_data_list[csv]
            out_bulk = np.concatenate([out_bulk, frame], axis =0)
    else:
        continue
bulk_run_loc=[(i + j) for i, j in zip(bulk_run_folderloc, bulk_run_fileloc)]       
bulk_dataframe= pd.DataFrame(out_bulk)
bulk_elements_starttimes.insert(0, np.nan)
bulk_elements_endtimes.insert(0, np.nan)
bulk_dataframe['start']=bulk_elements_starttimes
bulk_dataframe['end']=bulk_elements_endtimes


core=pd.DataFrame({'start':bulk_run_start,'locations':bulk_run_loc,'end': bulk_run_end})

# 
del bulk_data_list, bulk_end_i, bulk_start_i, csv, file_info
del found_files, frame, i,  start_1, start_key1,start_key2, x, y
del files_to_pull, bulk_run_start

'''#2) GETS DATETIMES FOR FILES WHICH MATCHED WITH'''
match1_run_start, match1_run_end = get_datetimes(files_key1)

match1=pd.DataFrame(zip(match1_run_start, match1_run_end), columns=['start', 'end'])
del match1_run_start, match1_run_end
match_word2_run_start, match_word2_run_end = get_datetimes(filesloc_key2)
match_word2=pd.DataFrame(zip(match_word2_run_start, match_word2_run_end), columns=['start', 'end'])
match_word2['locations']=[(i + j) for i, j in zip(folderloc_key2, filesloc_key2)]




'''#3) CREATES A MASK TO SELECT DATA FILES IN THE BULK DATABASE, 
#                 WHICH MATCH WITH THOSE IDENTIFIED IN THE KEYWORD FOLDER (IN THIS CASE 'HEATED')'''

n=0
counter =0
for i in range(len(match_word2.locations)):
    
    core_mask = (core['start'] == match_word2['start'][i]) & (core['end']  ==  match_word2['end'][i])
    if core.loc[core_mask]['start'].empty:
        print '{} not matched'.format( match_word2['locations'][i])
        continue
    else: 
        counter +=1
        
        data_heat=np.genfromtxt(match_word2['locations'][i], delimiter =',')
        #print core.loc[core_mask]['locations']
        data_corresp=np.genfromtxt(core.loc[core_mask]['locations'].iloc[0],delimiter =',')
        
        pulled_from_bulk.append(core.loc[core_mask]['locations'].iloc[0])
        
        
        #print core.loc[core_mask]['locations'].iloc[0]  
        all_data_corresp=np.concatenate([ all_data_corresp, data_corresp])
        
        
        fig2=plt.figure()
        
        ax1=plt.scatter(data_heat[:,0], data_heat[:,1], label =str(match_word2['locations'][i]), color='red')
        ax2=plt.scatter(data_corresp[:,0], data_corresp[:,1],
                     label =core.loc[core_mask]['locations'].iloc[0])
        plt.yscale('log')
        plt.legend()
        plt.savefig(figfold+str([i])+'.jpg')
print 'matched {} runs'.format(counter)        
#     4)PLOTS OUTPUT DATA, SAVES FIGURES   
        
fig1=plt.figure()
ax_a= plt.scatter(data_key2['T'], data_key2['INP'],color='red',zorder=0)
ax_b=plt.scatter(data_key1['T'], data_key1['INP'], color='blue')
plt.yscale('log')
plt.title('initial runs')
plt.savefig(figfold+str('initial runs')+'.jpg')
    
fig3=plt.figure()
ax_c= plt.scatter(data_key2['T'], data_key2['INP'], color='red', zorder=0)
ax_d=plt.scatter( all_data_corresp[:,0],  all_data_corresp[:,1], color ='blue',zorder=1)
plt.yscale('log')
plt.title('')
plt.savefig(figfold+str('with updated runs')+'.jpg')

del bulk_run_fileloc, bulk_run_folderloc, i, j, match_word2_run_start,match_word2_run_end, q, r, key
del a, b, bulk_elements_endtimes, bulk_elements_starttimes, bulk_folders,  bulk_indir
bulk_dataframe.to_csv('C:\\Users\\eardo\\Desktop\\Farmscripts\\alldata_withdates.csv')
data_key2.to_csv('C:\\Users\\eardo\\Desktop\\Farmscripts\\heatdata.csv')
match_word2_locations = match_word2.locations
match_word2_locations = match_word2.as_matrix()


#%% LOWRUNS UNHEATED

lowruns_unheated_data=np.empty(shape=(1,4))
indices=[]
lowruns = ['161020_MFC3_1345_1600','161013_MFC2_1041_1442','161031_MFC3_1017_1730']
for i in range(len(lowruns)):
	#print indices
	loc_lowruns_unheated = [j for j, s in enumerate (pulled_from_bulk) if lowruns[i] in s]
	indices.extend(loc_lowruns_unheated)


lowruns_unheated_list = [pulled_from_bulk[i] for i in indices]

for i in range(len(lowruns_unheated_list)):
    x= np.genfromtxt(lowruns_unheated_list[i], delimiter =',')
    lowruns_unheated_data = np.concatenate ([lowruns_unheated_data, x])
    
    
#%% LOWRUNS HEATED

lowruns_heated_data=np.empty(shape=(1,4))
indices=[]
for i in range(len(lowruns)):
	print indices
	loc_lowruns_heated = [j for j, s in enumerate (match_word2_locations[:,2]) if lowruns[i] in s]
	indices.extend(loc_lowruns_heated)
 
lowruns_heated_list = [match_word2_locations[i,2] for i in indices]

for i in range(len( lowruns_heated_list)):
    x= np.genfromtxt(lowruns_heated_list[i], delimiter =',')
    lowruns_heated_data = np.concatenate ([lowruns_heated_data, x])
    
    
    
  #### ####
#%% MidRUNS UNHEATED

midruns_unheated_data=np.empty(shape=(1,4))
indices=[]
midruns = ['161014_MFC2_1039_1219', '161007_MFC2_1041_1241', '161005_MFC2_1339_1439']
for i in range(len(midruns)):
	#print indices
	loc_midruns_unheated = [j for j, s in enumerate (pulled_from_bulk) if midruns[i] in s]
	indices.extend(loc_midruns_unheated)


midruns_unheated_list = [pulled_from_bulk[i] for i in indices]

for i in range(len(midruns_unheated_list)):
    x= np.genfromtxt(midruns_unheated_list[i], delimiter =',')
    midruns_unheated_data = np.concatenate ([midruns_unheated_data, x])
    
    
#%% LOWRUNS HEATED

midruns_heated_data=np.empty(shape=(1,4))
indices=[]
for i in range(len(lowruns)):
	print indices
	loc_midruns_heated = [j for j, s in enumerate (match_word2_locations[:,2]) if midruns[i] in s]
	indices.extend(loc_midruns_heated)
 
midruns_heated_list = [match_word2_locations[i,2] for i in indices]

for i in range(len( midruns_heated_list)):
    x= np.genfromtxt(midruns_heated_list[i], delimiter =',')
    midruns_heated_data = np.concatenate ([lowruns_heated_data, x])
    
    #### ####  
    
#==============================================================================
# #%%
# highruns_unheated_data=np.empty(shape=(1,4))
# indices=[]
# highruns = ['161018_Port_1045_1352','160928_Port_1334_1540','161011_MFC2_1410_1624']

highruns_unheated_data=np.empty(shape=(1,4))
indices=[]
highruns = ['160928_Port_1334_1540','161011_MFC2_1410_1624', '161021_MFC3_1442_1636']
for i in range(len(highruns)):
	#print indices
	loc_highruns_unheated = [j for j, s in enumerate (pulled_from_bulk) if highruns[i] in s]
	indices.extend(loc_highruns_unheated)


highruns_unheated_list = [pulled_from_bulk[i] for i in indices]

for i in range(len(highruns_unheated_list)):
    x= np.genfromtxt(highruns_unheated_list[i], delimiter =',')
    highruns_unheated_data = np.concatenate ([highruns_unheated_data, x])
    
    
#%% 

highruns_heated_data=np.empty(shape=(1,4))
indices=[]
for i in range(len(highruns)):
    #print highruns[i]
    
    loc_highruns_heated = [j for j, s in enumerate (match_word2_locations[:,2]) if highruns[i] in s]
      
    indices.extend(loc_highruns_heated)
    #print loc_highruns_heated

highruns_heated_list = [match_word2_locations[i,2] for i in indices]

for i in range(len(highruns_heated_list)):
    x= np.genfromtxt(highruns_heated_list[i], delimiter =',')
    highruns_heated_data = np.concatenate ([highruns_heated_data, x])


#%%

all_data=np.genfromtxt('C:\\Users\\eardo\\Desktop\\Farmscripts\\all data_1.csv',  delimiter=',')

fig1=plt.figure(figsize=(10,3))
ax0=plt.subplot(141)
plt.scatter(all_data[:,0], all_data[:,1], color ='k')
ax0.set_ylabel('[INP] /L')
degree_sign= u'\N{DEGREE SIGN}'
ax0.set_xlabel('T ('+degree_sign+'C)')


plt.yscale('log')
plt.xlim(-30,-5)
plt.ylim(0.01, 50)

ax1=plt.subplot(142)
plt.scatter(lowruns_heated_data[:,0], lowruns_heated_data[:,1], color ='red')
plt.scatter(lowruns_unheated_data[:,0], lowruns_unheated_data[:,1], color ='k')

plt.yscale('log')
plt.xlim(-30,-5)
plt.ylim(0.01, 50)
ax1.axes.get_yaxis().set_ticks([])
ax1.set_xlabel('T ('+degree_sign+'C)')

ax2=plt.subplot(143)
plt.scatter(highruns_heated_data[:,0], highruns_heated_data[:,1], color ='red')
plt.scatter(highruns_unheated_data[:,0], highruns_unheated_data[:,1], color ='k')


plt.yscale('log')
plt.xlim(-30,-5)
plt.ylim(0.01, 50)
ax2.axes.get_yaxis().set_ticks([])
ax2.set_xlabel('T ('+degree_sign+'C)')

ax0.get_yaxis().set_tick_params(which='both', direction='out')
ax0.get_xaxis().set_tick_params(which='both', direction='out')

np.savetxt('C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\lowruns_heated_data.csv',
           lowruns_heated_data, delimiter=',')

np.savetxt('C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\highruns_heated_data.csv',
           highruns_heated_data, delimiter=',')

np.savetxt('C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\lowruns_unheated_data.csv',
           lowruns_unheated_data, delimiter=',')

np.savetxt('C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\highruns_unheated_data.csv',
           highruns_unheated_data, delimiter=',')



np.savetxt('C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\midruns_heated_data.csv',
           midruns_heated_data, delimiter=',')

np.savetxt('C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\midruns_unheated_data.csv',
           midruns_unheated_data, delimiter=',')









