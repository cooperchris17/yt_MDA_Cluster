'''
This script finds the videos that have more than 1,000 view
and saves them in a csv file
'''

import pandas as pd

df = pd.read_csv('yt_main_corpus_metadata_stats.csv')
# deleting the index column from the df that I read in 
df2 = df.drop(df.columns[0],axis=1)

df3 = df2.loc[df2['view_count'] > 1000]

df3.to_csv('metadata_stats_more_than_1k.csv', index=False)
