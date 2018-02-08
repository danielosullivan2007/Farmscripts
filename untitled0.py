# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:55:55 2018

@author: eardo
"""

import pandas as pd
from directories import bardirs, farmdirs


data = pd.read_pickle('C:\Users\eardo\Desktop\Barbados data\Barbados Data\Pickles\APS')
data.to_csv('C://Users//eardo//Desktop//APS_BAR')
