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
