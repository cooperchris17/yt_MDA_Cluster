'''
This script checks for and deletes duplicated rows, creating a new csv file
Need to run this twice -  for the stats file and the metadata file
'''

import pandas as pd

# read in the csv file
# df = pd.read_csv('yt_main_corpus_all_stats.csv')
df = pd.read_csv('yt_main_corpus_metadata_has_video.csv')
# check if the csv file has any duplicate rows, if not, 'no duplicated rows' is printed'
if df.duplicated(['video_id']).sum() == 0:
    print('')
    print('No duplicate rows')
    print('')
# if there are duplicate rows, create a new metadata file with the duplicates deleted
# manually delete the old file and rename the new file if necessary
else:
    no_duplicates_df = df.drop_duplicates(['video_id'])
    print(no_duplicates_df)
    # no_duplicates_df.to_csv('yt_main_corpus_all_stats_NO_DUPLICATES.csv', encoding='utf8', index=False)
    no_duplicates_df.to_csv('yt_main_corpus_metadata_has_video_NO_DUPLICATES.csv', encoding='utf8', index=False)
