'''
This script downloads extra metadata from the YouTube API:
video length, view count, like count, comment count, category id, video tags
'stats date' is added to show when the stats were retrieved from the YouTube API
need to create a folder called stats in the folder running the script for the data to be saved into
'''

from apiclient.discovery import build
from datetime import datetime
import pandas as pd
import pprint
import winsound

# https://jingwen-z.github.io/how-to-get-a-youtube-video-information-with-youtube-data-api-by-python/
# the video ids were read from csv files containing videos that had transcripts
# they were output from the yt_txt.py script e.g. TranIds_weren't_she's_ourselves
# only inputting the search term made it easier for naming later
search_term = "weren't_she's_ourselves"

df = pd.read_csv('TranIds_'+search_term+'.csv')

api_key = 'INPUT_YOUTUBE_API_KEY'

youtube = build('youtube', 'v3', developerKey=api_key)

stats = []

for v_id in df['HasTranscript']:
    res = youtube.videos().list(
            part=['snippet', 'contentDetails', 'statistics'],
            id=v_id
    ).execute()

    stats += res['items']

now = datetime.now()

video_id = []
video_length = []
view_count = []
like_count = []
comment_count = []
category_id = []
video_tags = []
stats_date = []

for i in range(len(stats)):
    video_id.append((stats[i])['id'])
    video_length.append((stats[i])['contentDetails']['duration'])
    # adding .get() only gets stats for videos with data, it skips ones that don't have data
    view_count.append((stats[i])['statistics'].get('viewCount'))
    like_count.append((stats[i])['statistics'].get('likeCount'))
    comment_count.append((stats[i])['statistics'].get('commentCount'))
    category_id.append((stats[i])['snippet']['categoryId'])
    video_tags.append((stats[i])['snippet'].get('tags'))
    # add date that stats were downloaded in ISO 8601 -> same as YouTube API
    stats_date.append(now.isoformat())

data = {'video_id': video_id, 'video_length': video_length,'view_count': view_count, 'like_count': like_count,
        'comment_count': comment_count, 'category_id': category_id, 'video_tags': video_tags, 'stats_date': stats_date}

df2 = pd.DataFrame(data)
# remove the square brackets from the video_tags column (a list has been added for each video)
# from experience, this might cause trouble if I want to use this data later, removing apostrophes might also be beneficial
df2['video_tags'] = df2['video_tags'].apply(lambda x: str(x).replace('[','').replace(']',''))
print(df2)

df2.to_csv('stats//'+search_term+'_stats.csv', encoding='utf8', index=False)

# I added this beep to let me know when the script finished because it sometimes takes a few minutes
winsound.Beep(5000, 500)

