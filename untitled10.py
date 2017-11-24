# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:43:25 2017

@author: eardo
"""

list=[]
for i in range(len(data)):
    for j range(len(times)):
        if (data['index']>times[j,0]) and (data['index']<times[j,1]):
            list.append('exp'+j)
        else:
            list.append(np.nan)

data['expansion']=list