# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 10:48:41 2017

@author: eardo
"""

import os as os
import numpy as np

os.chdir('C:\\Users\\eardo\\Desktop\\Farmscripts\\INP_T\\')

    
    
INP, day =np.loadtxt('INP dataminus20.csv', delimiter=',', unpack = True, dtype = np.float64)

for i in range (len(day)):
    if day[i] == 1.0:
        print (i)
            #print (x)
        
            
            
    elif str(day[i]) == "inf":
        continue
            
    else:
        z = day[i]
        f =str('%8.0f' % z)
        saveLine = str(INP[i]) + ',' + str(int((day[i])))[0:6]+ ','+str(int((day[i])))[6:10]+','+ str(int((day[i])))[10:14]+'\n'
        saveFile = open('newCSV.csv', 'a')
        saveFile.write(saveLine)
        saveFile.close()
        print 'false'
            
            
            
            

