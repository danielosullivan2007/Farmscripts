# -*- coding: utf-8 -*-
"""
Created on Fri May 05 16:32:56 2017

@author: eardo
"""
import os 
import glob as glob
import numpy as np
import datetime 

topfolder='W:\\SMPS'
key_terms= ["Data"]


#Glob each subfolder
def globber(topfolder, key_terms):
    found_files=[]
    n=0
    os.chdir(topfolder)
    a=glob.glob('*\\')
    for ifolder in range(len(a)):
        os.chdir(topfolder+ a[ifolder])
        
        #search for files containing keywords       
        files_in_folder=glob.glob('*.csv')
        #print "found " +str(len(filelist))+" files"
        
        for s in range(len(files_in_folder)):
            if key_terms[0] in files_in_folder[s]:
                
                #print "looking for phrase "+str(key_terms[0])+" in: "+files_in_folder[s]
                found_files.append(files_in_folder[s])
                
    return found_files, a
            #frame_in=np.genfromtxt(filelist[s], delimiter = ",", usecols=(0,1))
      
found_files,a=globber(topfolder, key_terms)

del key_terms
del a