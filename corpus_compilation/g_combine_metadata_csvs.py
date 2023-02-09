'''
This script merges all csv files in the folder together
- this is almost the same as merge_yt_stats.py
- but I added a line of code to add a column containing the search term for each video
- and another line to delete the original indexes
'''

import pandas as pd
import glob
import os

#creates a list of all csv files in the current folder
globbed_files = glob.glob("*.csv")

# pd.concat takes a list of dataframes as an argument
data = []

for csv in globbed_files:
    frame = pd.read_csv(csv)
    # https://stackoverflow.com/questions/46449408/removing-file-extension-from-filename-with-file-handle-as-input
    # add a column containing the search term (taken from the individual csv filenames)
    frame['search_term'] = os.path.splitext(os.path.basename(csv))[0]
    data.append(frame)

bigframe = pd.concat(data)
# I needed to add this to drop the indexes from the original dfs (ignore_index=True didn't work)
bigframe_2 = bigframe.drop(bigframe.columns[0], axis=1)
bigframe_2.to_csv("yt_main_corpus_metadata.csv", encoding='utf8', index=False)

# for reference
# https://stackoverflow.com/questions/41857659/python-pandas-add-filename-column-csv
