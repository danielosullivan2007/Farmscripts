# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:08:10 2017

@author: eardo
"""
import numpy as np
import pandas as pd

a=-0.639
b=0.1296

vp_water=[]
vp_ice=[]
T_list=[]
for i in range(243, 273, 1):
    T=i
    p_water = np.exp(54.842763-6763.22/T - 4.21*np.log(T) + 0.000367*T + np.tanh(0.0415*(T - 218.8))*(53.878- 1331.22/T - 9.44523*np.log(T) + 0.014025*T))
    p_ice = np.exp(9.550426 - 5723.265/T + 3.53068*np.log(T) - 0.00728332*T )
    vp_water.append(p_water)
    vp_ice.append(p_ice)
    T_list.append(T)
    
data = zip(T_list,vp_water, vp_ice)
data=pd.DataFrame(data, columns = ['Temp', 'p_water', 'p_ice'])
data['ice_ss']=(data.p_water/data.p_ice)-1
data['meyers_INP']=np.exp(a+100*b*(data.ice_ss))
meyers = data