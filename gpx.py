# Convert gps files to csv
# Code from https://www.ryanbaumann.com/blog/2015/7/18/strava-heat-maps-part-2

import gpxpy
import os
import pandas as pd

INDIR = r'C:\Users\plswe\Documents\Maps\GPX\New folder'
OUTDIR = r'C:\Users\plswe\Documents\Maps\GPX\New folder'

#Set the working directory to the INDI variable
os.chdir(HOME)

def parsegpx(f):

    points2 = []
    with open(f, 'r') as gpxfile:
        gpx = gpxpy.parse(gpxfile)
        for track in gpx.tracks:
            for segment in tracak.segments:
                for point in segment.points:
                    dict = {'Timestamp' : point.time.
                            'Latitude' : point.latitude,
                            'Longitude' : point.longitude,
                            'Elevation' : point.elevation
                            }
                    points2.append(dict)
        return points2

files = os.listdir(INDIR)
df2 = pd.concat([pd.DataFrame(parsegpx(f)) for f in files], keys=files)
df2.head(5)

os.chdir(OUTDIR)
df2.to_csv('hike.csv')