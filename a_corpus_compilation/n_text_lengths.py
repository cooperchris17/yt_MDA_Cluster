'''
For all txt files in the folder:
the texts are tokenized with NLTK word_tokenize (they'll -> 'they', "'ll" / can't -> 'ca', "n't" / possesive 's' counted as token)
then a csv file is produced with 2 columns: video_id, text_lengths
'''

from nltk.tokenize import word_tokenize
import glob, os
import pandas as pd

text_lengths = []
video_id = []
# read all the txt files in the directory (and in other directories in that path)
for file in glob.iglob('**', recursive=True):
    if os.path.isfile(file): # filter dirs
        if file.endswith('.txt'): # avoid editing .py files, etc
            f = open(file, "r")
            raw = f.read()
            tokens = word_tokenize(raw)
            text_lengths.append(len(tokens))
            # get the video id from the filename and append to list
            vid_id = os.path.splitext(os.path.basename(file))[0]
            video_id.append(vid_id)

# create a pandas df with the list of text lengths and video ids 
data = {'video_id': video_id, 'text_length': text_lengths}
df = pd.DataFrame(data)
print(df)
df.to_csv('text_lengths.csv', encoding='utf8', index=False)
