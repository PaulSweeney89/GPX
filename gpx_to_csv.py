# Convert gps files to csv
# Code from https://www.ryanbaumann.com/blog/2015/7/18/strava-heat-maps-part-2

import gpxpy
import os
import pandas as pd

# Directory of gpx file to be converted to csv
INDIR = r'/home/paul/Desktop/GPX/Parse'

# Directory of output of csv file
OUTDIR = r'/home/paul/Desktop/GPX/data'

#Set the working directory to the INDIR variable
os.chdir(INDIR)

def parsegpx(f):

    points2 = []
    with open(f, 'r') as gpxfile:
        gpx = gpxpy.parse(gpxfile)
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    dict = {'Timestamp' : point.time,
                            'Latitude' : point.latitude,
                            'Longitude' : point.longitude,
                            'Elevation' : point.elevation
                            }
                    points2.append(dict)
        return points2

files = os.listdir(INDIR)
df2 = pd.concat([pd.DataFrame(parsegpx(f)) for f in files], keys=files)

# Output csv file
os.chdir(OUTDIR)
df2.to_csv('gps.csv')
