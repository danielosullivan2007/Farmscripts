# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 14:04:45 2017

@author: eardo
"""
import os as os
import numpy as np
import matplotlib.pyplot as plt
from itertools import repeat

saveloc= "C:/Users/useradmin/Desktop/Farmscripts/"
indir="Z:\shared\Farm-Leeds\pyoutput"
os.chdir(indir)
degree_sign= u'\N{DEGREE SIGN}'
glo=np.genfromtxt("Niemand_1.csv", delimiter=",",skip_header=1,)
leeds=np.genfromtxt("INPleeds.csv", delimiter=",",skip_header=1,)



Dayg=glo[:,0]
Day15l=leeds[:,0]
Day20l=leeds[:,2]
Day25l=leeds[:,4]
INP15g=glo[:,1]/1000
INP20g=glo[:,2]/1000
INP25g=glo[:,3]/1000
Gloday=[]
lday15=[]
lday20=[]
lday25=[]
T15l=[]
T20l=[]
T25l=[]
T15g=[]
T20g=[]
T25g=[]

for x in range (0,30):
    z= Dayg[x]-160900
    Gloday.append(z)
for x in range (30,61):
    z= Dayg[x]-161000+30
    Gloday.append(z)
for x in range (0,len(Day15l)):
    if Day15l[x]<161000:
        z= Day15l[x]-160900
        lday15.append(z)
    
    else:
        z= Day15l[x]-161000+30     
        lday15.append(z)
    
        
for x in range (0,len(Day20l)):
    if Day20l[x]<161000:
        z= Day20l[x]-160900
        lday20.append(z)
    elif Day20l[x]<161100:
        z= Day20l[x]-161000+30
        lday20.append(z)
    elif Day20l[x]<161200:     
        z= Day20l[x]-161100+61
        lday20.append(z)
    else:
        z= 'NaN'
        lday20.append(z)
        
for x in range (0,len(Day25l)):
    if Day25l[x]<161000:
        z= Day25l[x]-160900
        lday25.append(z)
    elif Day25l[x]<161100:
        z= Day25l[x]-161000+30
        lday25.append(z)
    elif Day25l[x]<161200:     
        z= Day25l[x]-161100+61
        lday25.append(z)
    else:
        z= 'NaN'
        lday25.append(z)

###############################################
INP15l=np.power(10,leeds[:,1])
INP20l=np.power(10,leeds[:,3])
INP25l=np.power(10,leeds[:,5])
#################################################################

fig=plt.figure()
ax1=plt.axes()
ax2=plt.axes()
ax1.plot( Gloday, INP15g,linewidth=0, marker="o")
ax2.plot(lday15,INP15l, linewidth=0, marker="o", c='r' )

ax1.set_yscale('log')
plt.title('Glomap v observed at -15'+degree_sign+'C', fontsize=14)
plt.xlabel('Day')
plt.ylabel('[INP] $L^{-1}$')

plt.show()

###################################################################

fig=plt.figure()
ax1=plt.axes()
ax2=plt.axes()
ax1.plot( Gloday, INP20g,linewidth=0, marker="o")
ax2.plot(lday20,INP20l, linewidth=0, marker="o", c='r' )

ax1.set_yscale('log')
plt.title('Glomap v observed at -20'+degree_sign+'C', fontsize=14)
plt.xlabel('Day')
plt.ylabel('[INP] $L^{-1}$')

#plt.show()


##################################################################
fig=plt.figure()
ax1=plt.axes()
ax2=plt.axes()
ax1.plot( Gloday, INP25g,linewidth=0, marker="o")
ax2.plot(lday25,INP25l, linewidth=0, marker="o", c='r' )

ax1.set_yscale('log')
plt.title('Glomap v observed at -25'+degree_sign+'C', fontsize=14)
plt.xlabel('Day')
plt.ylabel('[INP] $L^{-1}$')

#plt.show()
##################################################################
All15=np.append(INP15g, INP15l)
Gbin15= np.logspace(min(All15), max(All15))
freqINP15=np.histogram(INP15g,bins=(Gbin15))

T15l=T15l+ list(repeat(15, len(INP15l)))
T20l=T20l+ list(repeat(20, len(INP20l)))
T25l=T25l+ list(repeat(25, len(INP25l)))

T15g=T15g+ list(repeat(15, len(INP15g)))
T20g=T20g+ list(repeat(20, len(INP20g)))
T25g=T25g+ list(repeat(25, len(INP25g)))
######################################################################
fig=plt.figure()
ax1=plt.axes()
ax2=plt.axes()
ax3=plt.axes()
ax4=plt.axes()
ax5=plt.axes()
ax6=plt.axes()
ax1.plot( T25g, INP25g,linewidth=0, marker="o",c='b')
ax2.plot(T25l,INP25l, linewidth=0, marker="o", c='r' )

ax3.plot( T20g, INP20g,linewidth=0, marker="o",c='b')
ax4.plot(T20l,INP20l, linewidth=0, marker="o", c='r' )

ax6.plot(T15l,INP15l, linewidth=0, marker="o", c='r' )
ax5.plot( T15g, INP15g,linewidth=0, marker="o", c='b')


ax1.set_yscale('log')
plt.title('Glomap v observed', fontsize=14)
plt.xlabel('T'+degree_sign+'C')
plt.ylabel('[INP] /L')
plt.savefig(saveloc+'N12compare.png')
plt.show()
##########################################################################
loginp15l=np.log10(INP15l)
loginp15g=np.log10(INP15g)
INP15l= INP15l[np.logical_not(np.isnan(INP15l))]
INP15g= INP15g[np.logical_not(np.isnan(INP15g))]
                     
data_to_plot=[INP15l,INP15g]
fig=plt.figure()
ax1=fig.add_subplot(111)
ax2=fig.add_subplot(111)
bp = ax1.boxplot(data_to_plot)
plt.title('Measured v GLOMAP at -15'+degree_sign+'C', fontsize=14)
ax1.set_xticklabels(['Measured', 'GLOMAP'"\n"'(VT17)'])
plt.ylabel('Log$_{10}$ [INP]')
ax1.set_yscale('log')
plt.savefig(saveloc+'N12_Boxplot15.png')




############################################################################
loginp20l=np.log10(INP20l)
loginp20g=np.log10(INP20g)
INP20l= INP20l[np.logical_not(np.isnan(INP20l))]
INP20g= INP20g[np.logical_not(np.isnan(INP20g))]
                     
data_to_plot=[INP20l,INP20g]
fig=plt.figure()
ax1=fig.add_subplot(111)
ax2=fig.add_subplot(111)
bp = ax1.boxplot(data_to_plot)
plt.title('Measured v GLOMAP at -20'+degree_sign+'C', fontsize=14)
ax1.set_xticklabels(['Measured', 'GLOMAP'"\n"'(VT17)'])
plt.ylabel('Log$_{10}$ [INP]')
ax1.set_yscale('log')
plt.savefig(saveloc+'N_12Boxplot20.png')
###########################################################################

#NP25l=np.genfromtxt('loginp25l.csv',delimiter=',')
#INP25g=np.log10(INP25g)I

INP25l= INP25l[np.logical_not(np.isnan(INP25l))]
INP25g= INP25g[np.logical_not(np.isnan(INP25g))]


data_to_plot=[INP25l,INP25g]
fig=plt.figure()
ax1=fig.add_subplot(111)
ax2=fig.add_subplot(111)
bp = ax1.boxplot(data_to_plot)
plt.title('Measured v GLOMAP at -25'+degree_sign+'C', fontsize=14)
ax1.set_xticklabels(['Measured', 'GLOMAP'"\n"'(VT17)'])
plt.ylabel('Log$_{10}$ [INP]')
ax1.set_yscale('log')

plt.savefig(saveloc+'N_12Boxplot25.png')



#############################################################################


from pylab import plot, show, savefig, xlim, figure, \
                hold, ylim, legend, boxplot, setp, axes

# function for setting the colors of the box plots pairs
def setBoxColors(bp):
    setp(bp['boxes'][0], color='blue')
    setp(bp['caps'][0], color='blue')
    setp(bp['caps'][1], color='blue')
    setp(bp['whiskers'][0], color='blue')
    setp(bp['whiskers'][1], color='blue')
    setp(bp['fliers'][0], color='blue')
    setp(bp['fliers'][1], color='blue')
    setp(bp['medians'][0], color='blue')

    setp(bp['boxes'][1], color='red')
    setp(bp['caps'][2], color='red')
    setp(bp['caps'][3], color='red')
    setp(bp['whiskers'][2], color='red')
    setp(bp['whiskers'][3], color='red')
    #setp(bp['fliers'][2], color='red')
    #setp(bp['fliers'][3], color='red')
    #setp(bp['medians'][1], color='red')

# data to plot
A= [[INP15l],[INP15g]]
B = [[INP20l],[INP20g]]
C = [[INP25l],[INP25g]]

fig = figure()
ax = axes()
hold(True)

# first boxplot pair
bp = boxplot(A, positions = [2, 3], widths = 0.6)
setBoxColors(bp)

# second boxplot pair
bp = boxplot(B, positions = [5, 6], widths = 0.6)
setBoxColors(bp)

# thrid boxplot pair
bp = boxplot(C, positions = [8, 9], widths = 0.6)
setBoxColors(bp)

# set axes limits and labels

ax.set_xticklabels(['','-15'+degree_sign+'C', '-20'+degree_sign+'C', '-25' +degree_sign+'C'])
ax.set_xticks([1.5,2.5, 5.5, 8.5])
plt.ylabel('[INP] $L^{-1}$')
ax.set_yscale('log')
plt.title('Measured v GLOMAP (N12)', fontsize=14)

# draw temporary red and blue lines and use them to create a legend
hB, = plot([1,1],'b-')
hR, = plot([1,1],'r-')
legend((hB, hR),('Measured', 'Modelled'), loc = 'upper left')
plt.legend(loc = 'upper left')
hB.set_visible(False)
hR.set_visible(False)

savefig(saveloc+'N12.png')
show()







