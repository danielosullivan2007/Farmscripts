# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 16:09:44 2017

@author: eardo
"""

for i in range (len(INPT)):
        APS_mask=(APS['datetime'] > INPT['start'][i]) & (APS['datetime'] <=  INPT['end'][i])
        if APS.loc[APS_mask]['datetime'].empty:
            aps_sum.append(np.nan)
            print 'empty'
            continue
        else:
            print'added'
            aps_sum.append(APS.loc[APS_mask]['Total'].sum(axis=0))
