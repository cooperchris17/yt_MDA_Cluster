# https://stackoverflow.com/questions/41857659/python-pandas-add-filename-column-csv

'''
This script merges all csv files in the folder together
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
    data.append(frame)

bigframe = pd.concat(data, ignore_index=True) #dont want pandas to try an align row indexes
bigframe.to_csv("yt_main_corpus_stats.csv", encoding='utf8', index=False)
