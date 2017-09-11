# -*- coding: utf-8 -*-
"""
Created on Mon Sep 04 10:51:43 2017

@author: eardo
"""
#gets the average of values in a data index (e.g. datetimeindex)
#which fall between a range

import pandas as pd

def av_between(start_search, end_search, data, data_index):

    
    mask=  (data_index > start_search) & (data_index <=  end_search)
    located = data.loc[mask]
    return located

def impute(cols):
    Age = 

