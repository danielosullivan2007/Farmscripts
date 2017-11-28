# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:27:59 2017

@author: eardo
"""

import pandas as pd
from directories import farmdirs

met=pd.read_pickle(farmdirs['pickels']+'met.p')
cols = list(met)
met.drop(cols[0:5], axis =1, inplace =True)
met.drop(cols[-3], axis =1, inplace =True)
met.drop(cols[10:12], axis =1, inplace =True)