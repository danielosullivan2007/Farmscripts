# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:26:23 2017

@author: eardo
"""

import socket
host=socket.gethostname()

if host == 'see4-234': 
    farmdirs = {'pickels':'C:\\Users\\eardo\\Desktop\\farmscripts\\Pickels\\',
                   'figures':'C:\\Users\\eardo\\Desktop\\farmscripts\\Figures\\',
                   'home':'C:\\Users\\eardo\\Desktop\\farmscripts\\',
                   'glodir': 'C:\\Users\eardo\\Desktop\\Farmscripts\\glomap data\\160509\\',
                   'glodir1': 'C:\\Users\eardo\\Desktop\\Farmscripts\\glomap data\\',
                   'iced': 'C:\\Users\\eardo\\Desktop\\Farmscripts\\IceD\\'}
    bardirs = {'source': 'V:\\Data Dump\\', 'Organized':'V:\\Barbados_Data\\',
               'figures' : 'V:\\Figures\\',
               'pickels':'V:\\Pickels\\' }
elif host == 'SEE-L10840':
    farmdirs = {'pickels':'C:\\Users\\useradmin\\Desktop\\Farmscripts\\Pickels\\',
                   'figures':'C:\\Users\\useradmin\\Desktop\\Farmscripts\\Figures\\',
                   'home':'C:\\Users\\useradmin\\Desktop\\Farmscripts\\',
                   'glodir': 'C:\\Users\\useradmin\\Desktop\\Farmscripts\\glomap data\\',
                   'glodir1': 'C:\\Users\\useradmin\\Desktop\\Farmscripts\\glomap data\\160509\\',
                   'iced': 'C:\\Users\\useradmin\\Desktop\\Farmscripts\\IceD\\'}

