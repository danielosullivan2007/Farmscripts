# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 12:39:46 2017

@author: useradmin
"""

T_kelvin = T+273.16
T=273.16-T_kelvin

a= 0.0000594
b=3.33
c=0.0264
d=0.0033

INP_demott = a*(T)**b*N**(c*(T)+d)