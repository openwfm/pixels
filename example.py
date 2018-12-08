from utils import *
import numpy as np
import matplotlib.pyplot as plt
import saveload as sl

# Load data
g=sl.load('example')

# Size of the center of the pixels
size=200

# Ground pixels
lons=np.array(g.lon_nofire)
lats=np.array(g.lat_nofire)
color=(0,0.59765625,0)
plt.scatter(lons,lats,size,marker='.',color=color)

# Fire pixels
lons=np.array(g.lon_fire)
lats=np.array(g.lat_fire)
color=(0.59765625,0,0)
plt.scatter(lons,lats,size,marker='.',color=color)

plt.show()
