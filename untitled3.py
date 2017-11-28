# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:37:18 2017

@author: eardo
"""

ax7.boxplot(INP_18_box, meanprops=meanlineprops,
            whis='range',medianprops=medianprops, whiskerprops =whiskerprops)
plt.yscale('log')