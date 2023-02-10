'''
This script calculates the difference in days between the upload date 
and the date the statistics were downloaded from the YouTube API
Then the number of views per day is calculated
an new csv file is created with 2 new columns: 'days_since_upload' and 'views_per_day'
The script took a long time to run, about 2 1/2 hours for about 50k rows of data
'''

import pandas as pd
import isodate
from datetime import date

df = pd.read_csv('metadata_stats_together.csv')

days_since_upload = []

for ud in df['published_at']:
    for sd in df['stats_date']:
        upload_date = isodate.parse_date(ud)
        stats_date = isodate.parse_date(sd)
    delta = stats_date - upload_date
    days_since_upload.append(delta.days)

df['days_since_upload'] = days_since_upload

df['views_per_day'] = df['view_count'] / df['days_since_upload']
df['views_per_day'] = df['views_per_day'].round(2)

print(df)

df.to_csv('yt_main_corpus_metadata_stats.csv', encoding='utf8')
