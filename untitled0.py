# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:53:46 2018

@author: eardo
"""

import pandas as pd
from directories import farmdirs


test1 = pd.read_pickle(farmdirs['pickels']+'INPs_witherrors_timestamps.p')