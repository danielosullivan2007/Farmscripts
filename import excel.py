# -*- coding: utf-8 -*-
"""
Created on Sun May  7 18:57:44 2017

@author: Daniel
"""

import os 
import pandas as pd

indir = ('/Users/Daniel/Desktop/farmscripts/')
os.chdir(indir)
df_out = pd.DataFrame(columns = ['T', 'inp_air'])
x1=pd.ExcelFile('ice-d.xlsx')
x2 = x1.sheet_names  # see all sheet names


for i in range(5, 30):
    df = x1.parse(x2[i], skiprows = 6)
    df=df[["T", "inp_air"]]
    df.to_csv(indir+x2[i]+".csv")
    df_out = df_out.append(df)
    
df_out.to_csv(indir+"iced_compiled.csv")
    