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


def mask(continuous, discrete):
    mask = []
    for i in range(len(continuous.index)):
        if (continuous.index[i] == discrete.datetime).any():
            mask.append(True)
        else:
            mask.append(False)
    masked = continuous[mask] 
    return masked

def av_between(start_search, end_search, data, data_index):

    
    mask=  (data_index > start_search) & (data_index <=  end_search)
    located = data.loc[mask]
    return located



#EXAMPLE of applying a multiargument function to dataframe 
#test = df.Datestr.astype(str).apply(datetime.strptime, args=('%y%m%d',))
def get_dates_in_column(dataframe_column, fmt):

    dataframe_column.apply(datetime.datetime.strptime(fmt))




def globber(topfolder, key_terms):
    import os 
    import glob as glob
    found_files=[]
    
    os.chdir(topfolder)
    a=glob.glob('*\\')
    for ifolder in range(len(a)):
        os.chdir(topfolder+ a[ifolder])
        
        #search for files containing keywords       
        files_in_folder=glob.glob('*key_terms*.csv')
       #print "found "+" files"
        
        for s in range(len(files_in_folder)):
            if key_terms[0] in files_in_folder[s]:
                
        #        print "looking for phrase "+str(key_terms[0])+" in: "+files_in_folder[s]
                found_files.append(files_in_folder[s])
                
    return found_files, a
def jd_to_date(jd):
    import math
    """
    Convert Julian Day to date.
    
    Algorithm from 'Practical Astronomy with your Calculator or Spreadsheet', 
        4th ed., Duffet-Smith and Zwart, 2011.
    
    Parameters
    ----------
    jd : float
        Julian Day
        
    Returns
    -------
    year : int
        Year as integer. Years preceding 1 A.D. should be 0 or negative.
        The year before 1 A.D. is 0, 10 B.C. is year -9.
        
    month : int
        Month as integer, Jan = 1, Feb. = 2, etc.
    
    day : float
        Day, may contain fractional part.
        
    Examples
    --------
    Convert Julian Day 2446113.75 to year, month, and day.
    
    >>> jd_to_date(2446113.75)
    (1985, 2, 17.25)
    
    """
    jd = jd + 0.5
    
    F, I = math.modf(jd)
    I = int(I)
    
    A = math.trunc((I - 1867216.25)/36524.25)
    
    if I > 2299160:
        B = I + 1 + A - math.trunc(A / 4.)
    else:
        B = I
        
    C = B + 1524
    
    D = math.trunc((C - 122.1) / 365.25)
    
    E = math.trunc(365.25 * D)
    
    G = math.trunc((C - E) / 30.6001)
    
    day = C - E + F - math.trunc(30.6001 * G)
    
    if G < 13.5:
        month = G - 1
    else:
        month = G - 13
        
    if month > 2.5:
        year = D - 4716
    else:
        year = D - 4715
        
    return year, month, day




def date_to_jd(year,month,day):
    """
    Convert a date to Julian Day.
    
    Algorithm from 'Practical Astronomy with your Calculator or Spreadsheet', 
        4th ed., Duffet-Smith and Zwart, 2011.
    
    Parameters
    ----------
    year : int
        Year as integer. Years preceding 1 A.D. should be 0 or negative.
        The year before 1 A.D. is 0, 10 B.C. is year -9.
        
    month : int
        Month as integer, Jan = 1, Feb. = 2, etc.
    
    day : float
        Day, may contain fractional part.
    
    Returns
    -------
    jd : float
        Julian Day
        
    Examples
    --------
    Convert 6 a.m., February 17, 1985 to Julian Day
    
    >>> date_to_jd(1985,2,17.25)
    2446113.75
    
    """
    if month == 1 or month == 2:
        yearp = year - 1
        monthp = month + 12
    else:
        yearp = year
        monthp = month
    
    # this checks where we are in relation to October 15, 1582, the beginning
    # of the Gregorian calendar.
    if ((year < 1582) or
        (year == 1582 and month < 10) or
        (year == 1582 and month == 10 and day < 15)):
        # before start of Gregorian calendar
        B = 0
    else:
        # after start of Gregorian calendar
        A = math.trunc(yearp / 100.)
        B = 2 - A + math.trunc(A / 4.)
        
    if yearp < 0:
        C = math.trunc((365.25 * yearp) - 0.75)
    else:
        C = math.trunc(365.25 * yearp)
        
    D = math.trunc(30.6001 * (monthp + 1))
    
    jd = B + C + D + day + 1720994.5
    
    return jd