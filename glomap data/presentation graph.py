# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:14:03 2017

@author: useradmin
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os as os
import scipy.ndimage as ndimage
from matplotlib.gridspec import GridSpec
import datetime
import matplotlib.cm as cm
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from matplotlib.ticker import LogFormatter 
from matplotlib.ticker import LogFormatterMathtext 


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os as os
import scipy.ndimage as ndimage
from matplotlib.gridspec import GridSpec
import datetime
import matplotlib.cm as cm
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from matplotlib.ticker import LogFormatter 
from matplotlib.ticker import LogFormatterMathtext 

'''DATA MUST BE IN LOG BINS BY INP NUMBER'''

import numpy as np
import os as os
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import socket
host = socket.gethostname()


##############################################################################
'''Changes to required directory'''
if host == 'see4-234':
    #pickdir = ('C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\')
    indir = ('C:\\Users\\eardo\\Desktop\\Farmscripts\\')
    picdir='C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\'
    glodir = ('C:\\Users\eardo\\Desktop\\Farmscripts\\glomap data\\')
elif host == 'Daniels-Air.home':
    pickdir = ('//Users//Daniel//Desktop//farmscripts//Pickels//')
    indir = ('//Users//Daniel//Desktop//farmscripts//')
    
elif host == 'SEE-L10840':
    indir = ('C:\\Users\\useradmin\\Desktop\\Farmscripts\\')
    glodir = ('C:\\Users//useradmin//Desktop//Farmscripts//glomap data//160509//')    
    picdir = ('C:\\Users\\useradmin\\Desktop\\Farmscripts\\Pickels\\')
    #glodir = ('//Users//Daniel//Desktop//farmscripts//glomap data//160509//')

elif host =='Feynman':
    indir = ('C:\\Users\\Danny\\Desktop\\farmscripts\\')
    glodir = ('C:\\Users\\Danny\\Desktop\\farmscripts\\glomap data\\')
    picdir = ('C:\\Users\\Danny\\Desktop\\farmscripts\\Pickels\\')
    
percent = [0.2, 0.5, 0.8]



os.chdir(indir)


######################################