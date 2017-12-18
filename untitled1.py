# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 15:54:33 2017

@author: eardo
"""

from datetime import datetime
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


keyword='Blan'
os.chdir('S:\\')
files = glob('*Data*')

out=pd.DataFrame()

for i in range(len(files)):
    frame = pd.read_csv(files[i])
    out=out.append(frame)
    
out.to_csv(farmdirs['pickels']+'blanks.csv')