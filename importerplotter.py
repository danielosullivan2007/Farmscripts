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

#Create Keylist for globbing

key = ["heat"]
#==============================================================================
# for i in range(0, 2):
#     print i
#     key.append(raw_input('add a keyword---->'))    
#     
#==============================================================================
   

#Glob top folder
topfolder='X:\\'
os.chdir(topfolder)
a=glob('*\\')
filelist=[]
out1=np.empty(shape=(1,2))
out2=np.empty(shape=(1,2))
out3=np.empty(shape=(1,2))
out1[:] = np.NAN
out2[:] = np.NAN
out3[:] = np.NAN
#Glob each subfolder
n=0
for ifolder in range(len(a)):
    
    os.chdir(topfolder+ a[ifolder])
    print ifolder
    #search for files containing keywords
    for i in range(len(key)):
        
       # print "Searching for "+key[i]+" in "+ a[ifolder]
        x=(key[i])
        
        filelist=glob('*.csv')
        #print "found " +str(len(filelist))+" files"
        #print filelist
        for s in range(len(filelist)):
            n+=1
            #print n
                
            if key[0] in filelist[s]:
                
                print "looking for phrase "+str(key[0])+" in: "+filelist[s]
                frame_in=np.genfromtxt(filelist[s], delimiter = ",", usecols=(0,1))
                out1=np.concatenate((out1,frame_in))
                filename_in = filelist[s]
#==============================================================================
#             if key[1] in filelist[s]:
#                 print "looking at: "+filelist[s]
#                 frame_notin=np.genfromtxt(filelist[s], delimiter = ",", usecols=(0,1))
#                 out2=np.concatenate((out2,frame_notin))
#==============================================================================
                
            if key[0] not in filelist[s]:
                    print "looking for key not in: "+filelist[s]
                    frame_notin=np.genfromtxt(filelist[s], delimiter = ",", usecols=(0,1))
                    out3=np.concatenate((out3,frame_notin))
                    filename_notin = filelist[s]
                    continue 

            
                
        fig=plt.figure(num = n)
        plt.scatter(frame_in[:,0], frame_in[:,1],20,'r',  label = filename_in,edgecolor = 'none')
        plt.scatter(frame_notin[:,0], frame_notin[:,1],20,'g',  label = filename_notin, edgecolor = 'none')
        plt.legend(fontsize = 'x-small')
        plt.ylabel('n$_s$'+ "$( cm^{-2}$)", fontsize = 12)
        plt.xlabel("Temperature ("+ degree_sign+ "C)", fontsize = 12)
        plt.yscale('log')
        plt.title(a[ifolder][0:6])
                
fig1=plt.figure()
plt.yscale('log') 
plt.scatter(out1[:,0], out1[:,1],20,'r', label = key[0] + "ed", edgecolor = 'none')
plt.scatter(out3[:,0], out3[:,1], 20,'g', label = "not " + key[0]+"ed", edgecolor = 'none')
plt.legend()
#plt.title (a[daynumber][4:6] + '-'+ a[daynumber][2:4]+ '-' + a[daynumber][0:2])
plt.ylabel('n$_s$'+ "$( cm^{-2}$)", fontsize = 12)
plt.xlabel("Temperature ("+ degree_sign+ "C)", fontsize = 12)
os.chdir('X:\\')
plt.savefig(a[ifolder][0:6]+".png")
    
