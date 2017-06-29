# -*- coding: utf-8 -*-
"""
Created on Tue May 23 17:13:47 2017

@author: eardo
"""
import pandas as pd
df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
df.append(df2, ignore_index=True)