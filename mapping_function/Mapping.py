import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt 
import numpy as np


#import csv file
df = pd.read_csv('Fall migration of white storks in 2014-gps.csv')
longitude = df['location-long']
latitude = df['location-lat']
id = df['tag-local-identifier']


# import world map shp file
world_map = gpd.read_file('/Users/abestroka/Bio_Modeling_and_Simulation/02-712-Bird-Migration/mapping_function/ne_50m_land/ne_50m_land.shp')

#initialize coordinate system
crs = {'init':'epsg:4326'}


# make xy coordinates single feature
coordinates = [Point(xy) for xy in zip(df['location-long'], df['location-lat'])]

# create geo dataframe
geo_df = gpd.GeoDataFrame(df, crs = crs, geometry = coordinates)

# Create plot

fig, ax = plt.subplots(figsize=(15,15))

# Add map file
world_map.plot(ax=ax, alpha=0.4,color='grey')

geo_df.plot(column='tag-local-identifier', ax=ax, alpha=0.5, legend=True, markersize=10, categorical=True)

plt.title('Bird Migration Patterns')

# Lat/Long Map Boundaries
plt.xlim(min(longitude)-.5, max(longitude)+.5)
plt.ylim(min(latitude)-.5, max(latitude)+.5)

plt.show()
        

