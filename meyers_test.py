# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 20:02:56 2017

@author: useradmin
"""

T_list=[]
meyers_list=[]
def meyers(Tcelcius):
    A=-0.639
    B=0.1296
    T=Tcelcius+273.15
    p_water = np.exp(54.842763-6763.22/T - 4.21*np.log(T) + 0.000367*T + np.tanh(0.0415*(T - 218.8))*(53.878- 1331.22/T - 9.44523*np.log(T) + 0.014025*T))
    p_ice = np.exp(9.550426 - 5723.265/T + 3.53068*np.log(T) - 0.00728332*T )
    ice_ss = (p_water/p_ice)-1
    meyers_inp = np.exp(A+100*B*(ice_ss))
    
    return meyers_inp


for T in range(-25,-5,1):
    meyers_list.append(meyers(T))
    T_list.append(T)
    
fig2,ax2=plt.subplots()
ax2.plot(T_list, meyers_list)
ax2.set_yscale('log')
