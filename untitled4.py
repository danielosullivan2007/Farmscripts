# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 11:02:30 2017

@author: eardo
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
np.random.seed(1974)

from itertools import cycle

# Generate Data
num = 20
x, y = np.random.random((2, num))
labels = np.random.choice(['a', 'b', 'c'], num)
df = pd.DataFrame(dict(x=x, y=y, label=labels))

groups = df.groupby('label')

markers = ['x', 'o', '^']

# Plot
fig, ax = plt.subplots()
ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
for (name, group), marker in zip(groups, cycle(markers)):
    ax.plot(group.x, group.y, marker=marker, linestyle='', ms=12, label=name)
ax.legend()

plt.show()