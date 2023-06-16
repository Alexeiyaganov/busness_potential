import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.metrics import pairwise_distances
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import DBSCAN, KMeans
from copy import deepcopy

import seaborn as sns
import folium
from tqdm.auto import tqdm
tqdm.pandas()
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
import h3
from shapely.geometry import Polygon
from geojson import Feature, Point, FeatureCollection, Polygon
import plotly.express as px
from tqdm import tqdm

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


df = pd.read_csv('.data/hex_emb.csv', index_col=False)

df_train = df[:]

hexagones = df_train.pop('h3_cell')

for n_clusters in [2,3,4,5,6,7, 8, 9]:
    clusterer = KMeans(n_clusters=n_clusters)
    preds = clusterer.fit_predict(df_train)
    centers = clusterer.cluster_centers_

    score = silhouette_score(df_train, preds)
    print("For n_clusters = {}, silhouette score is {})".format(n_clusters, score))
    
distortions = []

K = range(1,20)
for k in K:
    kmean = KMeans(n_clusters=k, random_state=0, n_init = 50, max_iter = 500)
    kmean.fit(df_train)
    distortions.append(kmean.inertia_)
    
    
