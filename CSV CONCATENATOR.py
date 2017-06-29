# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 10:14:51 2017

@author: eardo
"""

import os
import glob
import pandas

###To run Type concatenate()
###Original files produced by searching in windows explorer, than concatenating "MFC2", MFC2 etc....

def concatenate (indir="C:\\Users\\eardo\\Desktop\\pyoutput\\Concatenated", outfile="C:\\Users\\eardo\\Desktop\\pyoutput\\\\Concatenated\\ConcatenatedAll.csv"):
    os.chdir(indir)
    fileList=glob.glob("*.csv")
    dfList=[]
    colnames=["Temp", "INP","FF","K"]
    for filename in fileList:
        print(filename)
        df=pandas.read_csv(filename, header=0)
        dfList.append(df)
    concatDf=pandas.concat(dfList, axis=0)
    concatDf.columns=colnames
    concatDf.to_csv(outfile, index=None)
    
concatenate()