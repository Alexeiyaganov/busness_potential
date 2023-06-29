import pandas as pd
import numpy as np

import os 
os.system('python yandex_maps_parser/link_parser.py')
os.system('python yandex_maps_parser/info_parser.py')

df_clusters = pd.DataFrame({'h3_cell': ['h333', 'f333', 'g343', 'g333'], 'n_cluster': [0, 1, 0, 1]})
df_caffe = pd.DataFrame({'h3_cell': ['h333', 'f333', 'g343', 'g333', 'gt333'], 'n_caffe': [5, 4, 3, 2, 1]})

medians_df = df_caffe.merge(df_clusters, left_on='h3_cell', right_on='h3_cell', how='inner')
medians = medians_df.groupby('n_cluster').median('n_caffe').reset_index()#.rename({'n_caffe': 'median'})

compare_df = medians_df.merge(medians, how='left', left_on='n_cluster', right_on='n_cluster')
compare_df['verdict'] = compare_df['n_caffe_x']<compare_df['n_caffe_y']