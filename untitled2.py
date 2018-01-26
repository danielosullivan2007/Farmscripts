# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 11:42:03 2018

@author: eardo
"""

import pandas as pd
from directories import farmdirs
import numpy as np


aps = pd.read_pickle(farmdirs['pickels']+'aps.p')


chi=1.2
rho0=1
rho=2.4

#DpAPS=(((chi*rho0)/rho)**0.5)*APSsize

aps_sizes = pd.to_numeric(list(aps.columns)[0:50])


DpAPS=(((chi*rho0)/rho)**0.5)*aps_sizes


aps_sizes = [str(aps_sizes[i]) for i in range(len(aps_sizes))]
DpAPS=[str(DpAPS[i]) for i in range(len(DpAPS))]
shift = dict(zip(aps_sizes,DpAPS))

aps.rename(columns=shift, inplace =True)

aps.to_pickle(farmdirs['pickels']+'aps_corrected.p')


smps = pd.read_pickle(farmdirs['pickels']+'smps.p')
smps.rename(columns=lambda x: x.strip(), inplace =True)
smps_sizes = pd.to_numeric(list(smps.columns)[1:111])
DpSMPS=(1/chi)*smps_sizes

smps_sizes=[str(smps_sizes[i]) for i in range(len(smps_sizes))]
DpSMPS = [str(DpSMPS[i]) for i in range (len(DpSMPS))]

shift_smps = dict(zip(smps_sizes, DpSMPS))

smps.rename(columns = shift_smps, inplace =True)


smps.to_pickle(farmdirs['pickels']+'smps_corrected.p')





