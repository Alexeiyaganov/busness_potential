import osmnx as ox
import geopandas as gpd
import contextily as cx

import geopandas as gpd
import numpy as np
import json
import h3
import folium
import osmnx as ox
from shapely import wkt
from folium.plugins import HeatMap
from shapely.geometry import Polygon
from folium.plugins import MarkerCluster, HeatMap
import pandas as pd
from shapely.geometry import Polygon
from geojson import Feature, Point, FeatureCollection, Polygon
import plotly.express as px
from tqdm import tqdm

tqdm.pandas()


place_name = "Ступино, Московская область, RU"

area = ox.geocode_to_gdf(place_name)

tags = {'amenity': True, 'landuse': True, 'shop': True, 'office': True, 'tourism': True, 'building': True, 'railway': True} 

items = ox.geometries_from_place(place_name, tags)
items.to_crs(epsg=3857)

df1 = items

df1['geometry'] = df1['geometry'].centroid

interests_df = pd.read_csv("./data/stupino_interests.csv")
locs_df = pd.read_csv("./data/stupino_locs.csv")


H3_res = 9  # размер гексагона [1 .. 15] чем больше, тем меньше площадь


def geo_to_h3(row):
    return h3.geo_to_h3(lat=row.geometry.y, lng=row.geometry.x, resolution=H3_res)


df1['h3_cell'] = df1.apply(geo_to_h3, axis=1)



                      
                      
shops = {i: ix for ix, i  in enumerate(dict(items.shop.value_counts()[:]).keys())}
amenities = {i: ix for ix, i  in enumerate(dict(items.amenity.value_counts()[:]).keys())}
tourism = {i: ix for ix, i  in enumerate(dict(items.tourism.value_counts()[:]).keys())}
office = {i: ix for ix, i  in enumerate(dict(items.office.value_counts()[:]).keys())}
landuse = {i: ix for ix, i  in enumerate(dict(items.landuse.value_counts()[:]).keys())}
railway = {i: ix for ix, i  in enumerate(dict(items.railway.value_counts()[:]).keys())}
building = {i: ix for ix, i  in enumerate(dict(items.building.value_counts()[:]).keys())}


one_hot_shop = pd.get_dummies(items['shop'])
df_shops = one_hot_shop[list(shops.keys())]

one_hot_landuse = pd.get_dummies(items['landuse'])
df_landuse = one_hot_landuse[list(landuse.keys())]

one_hot_railway = pd.get_dummies(items['railway'])
df_railway = one_hot_railway[list(railway.keys())]

one_hot_building = pd.get_dummies(items['building'])
df_building = one_hot_building[list(building.keys())]

one_hot_amenity = pd.get_dummies(items['amenity'])
df_amenity = one_hot_amenity[list(amenities.keys())]


one_hot_tourism = pd.get_dummies(items['tourism'])
df_tourism = one_hot_tourism[list(tourism.keys())]

one_hot_office = pd.get_dummies(items['office'])
df_office = one_hot_office[list(office.keys())]




df_a = pd.merge(df_amenity, df_shops, left_on='osmid', right_on='osmid')
df_b = pd.merge(df_a, df_tourism, left_on='osmid', right_on='osmid')
df_c = pd.merge(df_b, df_office, left_on='osmid', right_on='osmid')
df_d = pd.merge(df_c, df_landuse, left_on='osmid', right_on='osmid')
df_e = pd.merge(df_d, df_building, left_on='osmid', right_on='osmid')
df_f = pd.merge(df_e, df_railway, left_on='osmid', right_on='osmid')

df1.to_frame("ids").reset_index()
print(df1)

df2 = df1[["osmid","h3_cell"]]

df3 = pd.merge(df1, df2, left_on='osmid', right_on='osmid')

df_emb = df.groupby('h3_cell').sum()

df_emb.drop('osmid', inplace=True, axis=1)

      
      
locs_df['h3_cell'] = locs_df.progress_apply(geo_to_h3, axis=1)

locs_df_g = (locs_df
             .groupby('h3_cell')
             .id
             .agg(list)
             .to_frame("ids")
             .reset_index())
# Let's count each points inside the hexagon
locs_df_g['interests_count'] = (locs_df_g['ids']
                      .progress_apply(lambda ignition_ids: len(ignition_ids)))                
                      
df4 = locs_df_g[['interests_count','h3_cell']]

df_emb.merge(df4, on='h3_cell')

df_emb.to_csv('./data/hex_emb.csv')
                      




