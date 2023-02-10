'''
This script creates a new metadata csv file only containing metadata for videos that had a transcript
As the video ids for videos that had a transcript were used to create the yt_stats file,
the yt_stats file is used to show which files had a transcript
'''

import pandas as pd

# no need to amend these variables (unless they don't match your input files)
metadata_file = 'yt_main_corpus_metadata.csv'
stats_file = 'yt_main_corpus_all_stats.csv'
out_csv = 'yt_main_corpus_metadata_has_video.csv'
# read in the original metadata file as a df
metadata_df = pd.read_csv(metadata_file)
# read in the list of video ids that had transcripts as a df - I am taking this from the stats file
tranId_df = pd.read_csv(stats_file)
# search for ids in the metadata file that actually had a transcript
search = metadata_df.video_id.isin(tranId_df.video_id)
# output new df to csv containing metadata for files that had a transcript
df_out = metadata_df[search]
print(df_out)
# the output will retain initial index values, but this will be realigned when all channels' metadata is combined in one file
df_out.to_csv(out_csv, encoding='utf8', index=False)
