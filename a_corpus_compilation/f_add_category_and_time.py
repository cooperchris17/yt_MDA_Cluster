'''
This script adds 2 new columns to the stats dataframe

'category' - adds a category label from the number e.g. 'Education' from 27
- the vid_cat_tups.py file must be in the same folder when running this script

'time_in_seconds' - converts the video length to seconds 
'''

import pandas as pd
import isodate
from vid_cat_tups import vid_cats

df = pd.read_csv('yt_main_corpus_stats.csv')

category = []
time_in_seconds = []

for id in df['category_id']:
    for item in vid_cats:
        if id == item[0]:
            category.append(item[1])

df.insert(6, 'category', category)

for time in df['video_length']:
    dur = isodate.parse_duration(time)
    time_in_seconds.append(dur.total_seconds())

df.insert(2, 'time_in_seconds', time_in_seconds)

print(df)

df.to_csv('yt_main_corpus_all_stats.csv', index=False)
