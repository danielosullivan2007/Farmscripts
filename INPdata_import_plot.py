# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 18:57:49 2017

@author: eardo
"""

degree_sign= u'\N{DEGREE SIGN}'

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

def get_datetimes(filelist):
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
out1[:] = np.NAN
out2[:] = np.NAN
out3[:] = np.NAN
files_analyzed=[]
files_key1=[]
files_key2=[]

start_key2=[]
end_key2=[]
end=[]
start=[]
#Glob each subfolder
n=0

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
                files_key1.append(filelist[s])
                print "looking for key not in: "+filelist[s]
                frame_notin=np.genfromtxt(filelist[s], delimiter = ",", usecols=(0,1))
                out3=np.concatenate((out3,frame_notin))
                filename_notin = filelist[s]
                continue 
            
        elif "heat" in filelist[s]:
            
            #print "looking for phrase "+str(key[0])+" in: "+filelist[s]
            files_key2.append(filelist[s])
            frame_in=np.genfromtxt(filelist[s], delimiter = ",", usecols=(0,1))
            
            filename_in = filelist[s]
            print filelist[s]
            filelist[s][5:7]
            
            x= np.datetime64("20"+filelist[s][5:7] + "-"+filelist[s][7:9]+"-"+filelist[s][9:11]+"T"+
                                           filelist[s][17:19]+":"+filelist[s][19:21])
            start_key2.append(x)
            
            y = np.datetime64("20"+filelist[s][5:7] + "-"+filelist[s][7:9]+"-"+filelist[s][9:11]+"T"+
                                           filelist[s][22:24]+":"+filelist[s][24:26])
            end_key2.append(y)
            for i in range (len(frame_in)):
                end.append(x)
                start.append(y)
            out1=np.concatenate((out1,frame_in))

out1=pd.DataFrame(out1, columns =['T', 'INP']).drop(0)
start_key2 = pd.DataFrame(start, columns = ['start'])
start.index +=1          
end_key2 = pd.DataFrame(end, columns = ['end'])                
end.index +=1

data_key2=pd.concat([out1, end, start], axis =1)
del x, y      

#==============================================================================
#             if key[1] in filelist[s]:
#                 print "looking at: "+filelist[s]
#                 frame_notin=np.genfromtxt(filelist[s], delimiter = ",", usecols=(0,1))
#                 out2=np.concatenate((out2,frame_notin))
#==============================================================================
                
            

#==============================================================================
#         fig=plt.figure(num = n)
#         plt.scatter(frame_in[:,0], frame_in[:,1],20,'r',  label = filename_in,edgecolor = 'none')
#         plt.scatter(frame_notin[:,0], frame_notin[:,1],20,'g',  label = filename_notin, edgecolor = 'none')
#         plt.legend(fontsize = 'x-small')
#         plt.ylabel('# Ice nucleating particles'+ "$(L^{-1}$ air)", fontsize = 12)
#         plt.xlabel("Temperature ("+ degree_sign+ "C)", fontsize = 12)
#         plt.yscale('log')
#         plt.title(a[ifolder][0:6])
#==============================================================================
                
#==============================================================================
# fig1=plt.figure()
# plt.yscale('log') 
# plt.scatter(out1[:,0], out1[:,1],20,'r', label = "Inorganic INPs (after heat)" , edgecolor = 'none')
# plt.scatter(out3[:,0], out3[:,1], 20,'g', label = "Inorganic + Bio INPs (untreated)", edgecolor = 'none')
# plt.legend(fontsize=10)
# #plt.title (a[daynumber][4:6] + '-'+ a[daynumber][2:4]+ '-' + a[daynumber][0:2])
# plt.ylabel('# Ice Nucleating Particles'+ "$(L^{-1}$ air)", fontsize = 12)
# plt.xlabel("Temperature ("+ degree_sign+ "C)", fontsize = 12)
# os.chdir('X:\\')
# plt.savefig(folders[ifolder][0:6]+".png")
#==============================================================================

