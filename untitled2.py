# -*- coding: utf-8 -*-
"""
Created on Tue Jul 04 14:21:17 2017

@author: useradmin
"""

a= glob.glob('Y:/'+'*/')
for i in range(len(a)):
    dayfolder=a[i]
    b =glob.glob(dayfolder)
    print dayfolder