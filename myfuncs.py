# -*- coding: utf-8 -*-
"""
Created on Mon Sep 04 10:51:43 2017

@author: eardo
"""
#gets the average of values in a data index (e.g. datetimeindex)
#which fall between a range

import pandas as pd


num2words={-15:'minus15',-16:'minus16',-17:'minus17',-18:'minus18',
           -19:'minus19',-20:'minus20',-21:'minus21',
           -22:'minus22', -23:'minus23', -24:'minus24',-25: 'minus25'}


def av_between(start_search, end_search, data, data_index):

    
    mask=  (data_index > start_search) & (data_index <=  end_search)
    located = data.loc[mask]
    return located


#EXAMPLE of applying a multiargument function to dataframe 
#test = df.Datestr.astype(str).apply(datetime.strptime, args=('%y%m%d',))
def get_dates_in_column(dataframe_column, fmt):

    dataframe_column.apply(datetime.datetime.strptime(fmt))