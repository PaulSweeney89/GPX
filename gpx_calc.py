# gpx.csv  file calculations & plots. 
# https://towardsdatascience.com/how-tracking-apps-analyse-your-gps-data-a-hands-on-tutorial-in-python-756d4db6715d

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import haversine								# haversine for calculating the distance between coordinates
import os

csv_file = os.path.abspath(os.path.expanduser('Desktop/GPX/data/gps.csv'))
df = pd.read_csv(csv_file)
print(csv_file)

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

df.to_csv(csv_file, index=False)

total_distance = round(df['Distance'].max(),1)
print(total_distance)

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

textstr = '\n'.join((
    r'Elevation Gain = %sm' % (gain),
    r'Elevation Loss = %sm' % (loss),
    r'Total Distance = %skm' % (total_distance)))

ax.text(0, 725, textstr, fontsize=14, verticalalignment='top', bbox=dict(facecolor='white', edgecolor='black', pad=5))

ax.minorticks_on()
ax.grid(which='major', linestyle='-', linewidth='1', color='black')
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

plt.show()
