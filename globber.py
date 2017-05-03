# -*- coding: utf-8 -*-
"""
Created on Wed May 03 11:31:39 2017

@author: eardo
"""
import os 
import glob as glob
import numpy as np
import datetime 

topfolder='W:\\'
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


def get_datetimes(found):
    dates=[found[i][5:11] for i in range(len(found_files))]
    start_times = [found[i][17:21] for i in range(len(found_files))]
    end_times = [found[i][22:26] for i in range(len(found_files))]
    
    dates_clean=[dates[i][0:2]+"/"+dates[i][2:4]+"/"+dates[i][4:6] for i in range(len(dates))]
    start_t=[start_time[0:2]+ ":" +start_time[2:] for start_time in start_times]
    end_t=[end_time[0:2]+ ":" +end_time[2:] for end_time in end_times]
    
    start_datetimes = [datetime.datetime(int(dates[i][0:2]), int(dates[i][2:4]), 
                        int(dates[i][4:6]), int(start_times[i][0:2]),int(start_times[i][2:])) 
    for i in range(len(start_times))]
    
    end_datetimes = [datetime.datetime(int(dates[i][0:2]), int(dates[i][2:4]), 
                        int(dates[i][4:6]), int(end_times[i][0:2]),int(end_times[i][2:])) 
    for i in range(len(start_times))]
    return start_datetimes, end_datetimes
    
start_datetimes, end_datetimes =get_datetimes(found_files)