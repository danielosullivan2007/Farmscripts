# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 05:32:51 2017

@author: useradmin
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

indir = "C:\\Users\\useradmin\\Desktop\\Farmscripts\\Pickels\\"
data = pd.read_csv(indir+ 'data at minus20.csv').drop([u'Unnamed: 0',u'1', u'0',],
                  axis=1)
data.rename(columns = {u'2':'start', u'3':'end'}, inplace =True)
cols=data.columns.tolist()
reorder_cols = ['start', 'end','INP', 'MEAN_WIND_SPEED', 'MAX_GUST_DIR', 'MAX_GUST_SPEED',
                'MAX_GUST_CTIME', 'Dry Bulb Temperature', 'Dew Point Temperature',
                'Grass Temperature', 'Concrete Temperature',
                '10cm Soil Temperature', 'Rainfall Total since 0900',
                'Radiation Total since 0900',
                'Humidity', 'APS Total', 'SMPS Total',  'demott']
data=data[reorder_cols]
data['APS Total'] = data.drop(data[data['APS Total']>80000].index)


sns.distplot(data.INP, bins =40)
plt.xlabel('log10 [INP]')

sns.jointplot(x='INP', y ='APS Total', data =data)
sns.lmplot(x='INP', y ='MEAN_WIND_SPEED', data = data)
#fig4=plt.figure()
#sns.pairplot(data)

data.drop(['start','end',u'Dew Point Temperature',
       u'Grass Temperature', u'Concrete Temperature', u'10cm Soil Temperature'], inplace=True, axis =1)

corr=data.corr()

fig4=plt.figure()
sns.heatmap(corr)
data.fillna(value =93898, axis =1, inplace =True)
sns.heatmap(data.isnull())
#%%

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(data)

scaled_data=scaler.transform(data)

from sklearn.decomposition import PCA

pca = PCA(n_components = 3)

pca.fit(scaled_data)
x_pca =pca.transform(scaled_data)

plt.figure(figsize = (8,6))
plt.scatter(x_pca[:,0],x_pca[:,1], cmap ='plasma')
plt.xlabel('Component 1')
plt.ylabel('Component 2')

data_components=pd.DataFrame(pca.components_, columns = data.columns.tolist())

sns.heatmap(data_components, cmap ='plasma')
#%%

