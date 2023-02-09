'''
This script merges the metadata file and the stats file together 
by merging on the video id
- run after deleting duplicte rows in each file
'''

import pandas as pd

# https://pandas.pydata.org/docs/user_guide/merging.html
# This section: Brief primer on merge methods (relational algebra)

df1 = pd.read_csv('yt_main_corpus_metadata_has_video_NO_DUPLICATES.csv')
df2 = pd.read_csv('yt_main_corpus_all_stats_NO_DUPLICATES.csv')

df3 = pd.merge(df1, df2, on='video_id', how='inner')

print(df3)

df3.to_csv('metadata_stats_together.csv', index=False)
