import pandas as pd

# https://pandas.pydata.org/docs/user_guide/merging.html
# This section: Brief primer on merge methods (relational algebra)

df1 = pd.read_csv('metadata_stats_more_than_1k.csv')

df2 = pd.read_csv('text_lengths.csv')

df3 = pd.merge(df1, df2, on='video_id', how='inner')

print(df3)

df3.to_csv('metadata_stats_1k_plus_lengths.csv', index=False)
