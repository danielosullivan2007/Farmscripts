# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:33:06 2017

@author: eardo
"""
import numpy as np
import os
import matplotlib.pyplot as plt

os.chdir('C:\Users\eardo\Desktop\pyoutput')
degree_sign= u'\N{DEGREE SIGN}'
freqT=np.genfromtxt("freqT.csv", delimiter=",")
T=freqT[:,0]
freq=freqT[:,1]
fig=plt.plot(T,freq, linewidth=0, marker="o")
plt.title('Frequency of droplet freezing', fontsize=16)
plt.xlabel('T ('+degree_sign+'C)')
plt.ylabel('Instances observed')
plt.xlim(-30,-5)
plt.show()
