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

key = []
for i in range(0, 2):
    print i
    key.append(raw_input('add a keyword---->'))    
    
   
daynumber= 5
#Glob top folder
folder='X:\\'
os.chdir(folder)
a=glob('*\\')
filelist=[]
out1=np.empty(shape=(1,2))
out2=np.empty(shape=(1,2))
out3=np.empty(shape=(1,2))
out1[:] = np.NAN
out2[:] = np.NAN
out3[:] = np.NAN
#Glob each subfolder
for ifolder in range(len(a)):
    os.chdir(folder+ a[daynumber])
    #search for files containing keywords
    for i in range(len(key)):
        #print "Searching for "+key[i]+" in "+ a[ifolder]
        x=(key[i])
        filelist=glob('*'+str(x)+'*.csv')
        #print "found " +str(len(filelist))+" files"
        #print filelist
        for s in range(len(filelist)):
            if key[0] in filelist[s]:
                print "looking at: "+filelist[s]
                frame=np.genfromtxt(filelist[s], delimiter = ",", usecols=(0,1))
                out1=np.concatenate((out1,frame))


            if key[1] in filelist[s]:
                print "looking at: "+filelist[s]
                frame=np.genfromtxt(filelist[s], delimiter = ",", usecols=(0,1))
                out2=np.concatenate((out2,frame))
                
            if key[0] not in filelist[s]:
                print "looking at: "+filelist[s]
                frame=np.genfromtxt(filelist[s], delimiter = ",", usecols=(0,1))
                out3=np.concatenate((out3,frame))      
                print(len(out3))
                print(len(frame))
                
                
fig1=plt.figure()
plt.yscale('log') 
plt.scatter(out1[:,0], out1[:,1],20,'r', label = key[0] + "ed", edgecolor = 'none')
plt.scatter(out3[:,0], out3[:,1], 20,'g', label = "not " + key[0]+"ed", edgecolor = 'none')
plt.legend()
plt.title (a[daynumber][4:6] + '-'+ a[daynumber][2:4]+ '-' + a[daynumber][0:2])
plt.ylabel('n$_s$'+ "$( cm^{-2}$)", fontsize = 12)
plt.xlabel("Temperature ("+ degree_sign+ "C)", fontsize = 12)
os.chdir('X:\\')
plt.savefig(a[daynumber][0:6]+".png")
    