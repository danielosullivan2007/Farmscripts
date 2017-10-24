# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 18:08:32 2017

@author: useradmin
"""

"""
=============================================
Basic Trajectory Plotting and Using MapDesign
=============================================
How to quickly initialize a matplotlib Basemap with the ``MapDesign``
class and plot ``Trajectory`` paths.
For this example we'll initialize only the January trajectories created in
``bulk_trajgen_example.py``.
"""
import pysplit


trajgroup_N = pysplit.make_trajectorygroup(r'C:\\hysplit4\\working\\Test\\N\\*fdump*')
trajgroup_S = pysplit.make_trajectorygroup(r'C:\\hysplit4\\working\\Test\\S\\*fdump*')

"""
Basemaps and MapDesign
----------------------
PySPLIT's ``MapDesign`` class uses the matplotlib Basemap toolkit to quickly
set up attractive maps.  The user is not restricted to using maps
produced from ``MapDesign``, however- any Basemap will serve in the section
below entitled 'Plotting ``Trajectory`` Paths.
Creating a basic cylindrical map using ``MapDesign``  only requires
``mapcorners``, a list of the lower-left longitude, lower-left latitude,
upper-right longitude, and upper-right latitude values.
The ``standard_pm``, a list of standard parallels and meridians,
may be passed as ``None``.
"""
mapcorners =  [-150, 15, -50, 65]
standard_pm = None


bmap_params = pysplit.MapDesign(mapcorners, standard_pm)

"""
Once the ``MapDesign`` is initialized it can be used to draw a map:
"""
#bmap = bmap_params.make_basemap()
#bmap = Basemap(llcrnrlon=30.,llcrnrlat=-20.,urcrnrlon=80.,urcrnrlat=80.,
    #        projection='lcc',lat_1=-20,lon_0=90.,rsphere=(6378137.00,6356752.3142),
     #       resolution ='l',area_thresh=1000.)
#bmap = Basemap(projection='ortho',lon_0=-20,lat_0=60,resolution='l')

bmap = Basemap(llcrnrlon=-50.,llcrnrlat=30.,urcrnrlon=40.,urcrnrlat=70.,\
            rsphere=(6378137.00,6356752.3142),\
            resolution='l',projection='merc',\
            lat_0=40.,lon_0=-20.,lat_ts=20.)    
"""
Plotting ``Trajectory`` Paths
-----------------------------
For this example, we will color-code by initialization (t=0) altitude,
(500, 1000, or 1500 m), which can be accessed via ``Trajectory.data.geometry``,
 a ``GeoSeries`` of Shapely ``Point`` objects.
We can store the trajectory color in ``Trajectory.trajcolor`` for convenience.
"""
color_dict_N = {100.0 : 'blue',
              1000.0 : 'orange',
              1500.0 : 'black'}

for traj in trajgroup_N:
    altitude0 = traj.data.geometry.apply(lambda p: p.z)[0]
    traj.trajcolor = color_dict_N[altitude0]

color_dict_S = {100.0 : 'red',
              1000.0 : 'orange',
              1500.0 : 'black'}

for traj in trajgroup_S:
    altitude0 = traj.data.geometry.apply(lambda p: p.z)[0]
    traj.trajcolor = color_dict_S[altitude0]



"""
For display purposes, let's plot only every fifth ``Trajectory``.  The lats,
lons are obtained by unpacking the ``Trajectory.Path``
(Shapely ``LineString``) xy coordinates.
"""

#%%
for traj in trajgroup_N[::1]:
    bmap.plot(*traj.path.xy, c=traj.trajcolor, latlon=True, zorder=20)
    
for traj in trajgroup_S[::1]:
    bmap.plot(*traj.path.xy, c=traj.trajcolor, latlon=True, zorder=20)  

bmap.drawmapboundary(fill_color='black', zorder =0) # fill to edge
bmap.drawcountries()

bmap.drawcoastlines()
#bmap.drawcontinents(fill_color ='green')
bmap.fillcontinents(color='white',lake_color='black',zorder=20)

