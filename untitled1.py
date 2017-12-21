# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 15:54:33 2017

@author: eardo
"""

import datetime
import os, os.path
from glob import glob
import numpy as np
from os import listdir
os.chdir('C:\\Users\\eardo\\Desktop\\farmscripts\\')
import numpy as np
import matplotlib.pyplot as plt
import pylab
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import matplotlib.patches as mpatches
import socket
from directories import farmdirs


keyword='MFC'
os.chdir('P:\\')
files = glob('*Data*')
errors=[]
#run_date=[31:35]
#run_date=range(5,11)

out=pd.DataFrame()


for i in range(len(files)):
    try:
        if keyword in files[i]:
            print 'key found'
        else:
            print 'key not in {}'.format(files[i])
        frame = pd.read_csv(files[i])
        frame['run_date'] = datetime.datetime.strptime(files[i][30:36],'%y%m%d')
        frame['sample_date'] = datetime.datetime.strptime(files[i][5:11],'%y%m%d')
        out=out.append(frame)
    
    except ValueError:
            errors.append(files[i])
            print 'error in {}'.format(files[i])
            continue
                
    
    
out.to_csv(farmdirs['pickels']+'MFC2_MFC3.csv')

