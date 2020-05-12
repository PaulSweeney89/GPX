# gpx.csv  file calculations & plots. 
# https://towardsdatascience.com/how-tracking-apps-analyse-your-gps-data-a-hands-on-tutorial-in-python-756d4db6715d

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import haversine								# haversine for calculating the distance between coordinates

df = pd.read_csv("data/gps.csv")


# Calculating Distance & Elevation between Coordinates

n = 0
dist=[]
alt = []

for n in range(len(df)):

	if n == 0:
		d = 0								# starting point distance / elevation = 0
		dist.append(d)							# append starting distance
		alt.append(d)							# append elevation 	
		pass
	else:
		coord1 = (df.loc[n-1]['Latitude'], df.loc[n-1]['Longitude'])
		coord2 = (df.loc[n]['Latitude'], df.loc[n]['Longitude'])
		d = haversine.haversine(coord1, coord2)
		dist.append(d)

		e = df.loc[n-1]['Elevation'] - df.loc[n]['Elevation']		# Calculating elevation change
		alt.append(e)

distance = np.cumsum(dist)							# cumulative distance

df['Distance'] = distance							# adding new distance column to csv file

df.to_csv('data/gps.csv')

# Calculating total Elevation Gain

def positive_only(x):
    if x > 0:
        return x
    else:
        return 0
pos_only = list(map(positive_only, alt))
gain = round(sum(pos_only))

# Calculating total Elevation Loss

def negative_only(x):
    if x < 0:
        return x
    else:
        return 0
neg_only = list(map(negative_only, alt))
loss = round(abs(sum(neg_only)))

# Plot Distance vs Elevation

fig, (ax) = plt.subplots(1,1)
ax.plot(df['Distance'], df['Elevation'], color='black')
ax.fill_between(df['Distance'], df['Elevation'], facecolor='blue')
ax.set_xlabel('Distance (km)')
ax.set_ylabel('Elevation (m)')
ax.text(0, 700, 'Elevation Gain = %s'%(gain))
ax.text(0, 670, 'Elevation Loss = %s'%(loss))
plt.show()
