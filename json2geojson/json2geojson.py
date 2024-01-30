#%%
import pandas as pd
import numpy as np
import os
import json
import geopandas as gpd
from shapely import Polygon
#%%

# read json as a dataframe
data = pd.read_json('../data/map_basis/Tile-Grid-Map-Cleaned.json')

# spearate the column coordinates into two columns by comma
data[['coord_x', 'coord_y']] = pd.DataFrame(data['coordinates'].tolist(), index=data.index)

data['coord_y'] = data['coord_y'].max() - data['coord_y'] +1


# draw a square around the coordinates
data['coord_x_min'] = data['coord_x'] - 0.5
data['coord_x_max'] = data['coord_x'] + 0.5
data['coord_y_min'] = data['coord_y'] - 0.5
data['coord_y_max'] = data['coord_y'] + 0.5

# generate the polygon coordinates
data['geometry'] = data.apply(lambda x: [[x['coord_x_min'], x['coord_y_min']], [x['coord_x_min'], x['coord_y_max']], [x['coord_x_max'], x['coord_y_max']], [x['coord_x_max'], x['coord_y_min']], [x['coord_x_min'], x['coord_y_min']]], axis=1)

geodata = data[['name', 'alpha-2', 'alpha-3', 'region', 'sub-region', 'coord_x', 'coord_y', 'geometry']]

geodata['geometry'] = geodata['geometry'].apply(lambda x: Polygon(x))

geodata = gpd.GeoDataFrame(geodata, geometry='geometry')

geodata.to_file('../data/map_basis/Tile-Grid-Map-Cleaned.shp')
# %%

# Plot the geodataframe and display 'alpha-3' as labels
geodata.plot(column='alpha-3', legend=True, figsize=(15, 10))