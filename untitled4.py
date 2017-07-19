# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 01:19:08 2017

@author: useradmin
"""
import pandas as pd
import numpy as np
train = pd.read_csv('http://bit.ly/kaggletrain')



def get_elements(my_list, position):
    return my_list[position]

print train.Name.str.split(',').apply(get_elements, position =0).head()
print train.Name.str.split(',').apply(lambda x: x[0]).head()
drinks = pd.read_csv('http://bit.ly/drinksbycountry')

print drinks.loc[:, 'beer_servings':'wine_servings'].apply(max, axis =1).head()
print drinks.loc[:, 'beer_servings':'wine_servings'].applymap(float).head()


