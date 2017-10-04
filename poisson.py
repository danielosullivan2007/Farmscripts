# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 17:28:19 2017

@author: eardo
"""

import pandas as pd
import os
import numpy as np

os.chdir('C:\\Users\\eardo\\Desktop\\Farmscripts\\')
data =pd.read_excel('poisson.xlsx',sheetname = 'Sheet2',
                    header =0)
n_drops=data.events.iloc[-1]

data['fraction'] = data['events']/n_drops 

def poisson_CI(fraction, n_drops):
    err_plus = fraction + (1.96)**2/(4*n_drops) + 1.96 * (fraction/ n_drops)**0.5
    err_minus = fraction + (1.96)**2/(4*n_drops) - 1.96 * (fraction/ n_drops)**0.5
    return err_plus, err_minus

errs = data['fraction'].apply(poisson_CI, n_drops =n_drops)
data['Fpos']=zip(*errs)[0]
data['Fneg']=zip(*errs)[1]

def ns(fraction):
    ns = -np.log(1-fraction)
    return ns

ns_df = pd.DataFrame()
ns_df['Temp']=data['T']
ns_df['ns'] = data['fraction'].apply(ns)
ns_df['ns_plus'] =  data['Fpos'].apply(ns)-ns_df.ns
ns_df['ns_neg'] = ns_df.ns - data['Fneg'].apply(ns)
ns_df.drop(ns_df.index[len(ns_df) - 1], inplace =True)
import matplotlib.pyplot as plt
figr = plt.figure()
ax= plt.scatter(ns_df.Temp, ns_df.ns)
plt.yscale('log')


assymetric_error = (ns_df.ns_plus, ns_df.ns_neg)
plt.errorbar(ns_df.Temp, ns_df.ns, yerr=assymetric_error)