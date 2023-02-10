'''
IMPORTANT: before running this script, create a new folder called '1k_views'
in the directory that you run this script from, otherwise the files will be lost
This script should be run from the folder containing the transcripts downloaded from youtube-transcript-api
'''

import os, shutil, glob
import pandas as pd

# create a subfolder called '1k_views' in the directory you are running the script from
destination = './1k_views'

# read the filenames from df, save as list to variable
# df = pd.read_csv('informal_youtube_filenames.csv')
df = pd.read_csv('metadata_stats_more_than_1k.csv')

# create a list of the filenames from the video id column in the df
filenames = []
for id in df['video_id']:
    filenames.append(id+'.txt')

# iterate through the directory and move files from the list to the new directory '/short_texts'
for file in glob.iglob('**', recursive=True):
    if os.path.isfile(file): # filter dirs
        if file.endswith('.txt'): # avoid editing .py files, etc
            if file in filenames:
                shutil.move(file, destination)
