'''
This script uses the youtube_ids extracted from the YouTube Data API
It downloads available transripts as .txt with the youtube-transcript-api
Only need to amend the 'metadata_file' variable (and output folder if you want to save the transcripts in different folders)
'''

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import pandas as pd

# input file to read the video_ids
metadata_file = "INPUT_NAME_OF_CSV_FILE.csv"
# specify folder to save transcripts in (create the folder manually first)
# I decided to save all transcripts in the same folder, as I can find specific video info from the metadata anyway
output_folder = 'transcripts//'

df = pd.read_csv(metadata_file)
# specify the text formatter from the YouTubeTranscriptApi, either txt or json
txt_formatter = TextFormatter()

# the column in the df containing video ids
id_col = df.iloc[:,1]

# create an open list to extract the video_ids that have a transcript
HasTranscript = [ ]

# this for loop reads the video_ids from the metadata_file and outputs transcript text files
i = 0
for vid_id in id_col:
    try:
        # generate a list of transcripts for each video id from the df
        transcript_list = YouTubeTranscriptApi.list_transcripts(id_col[i])
        # if the transcript file in the transcript_list is in English and auto-generated (not manually input by user) transcript will be returned
        for transcript in transcript_list:
            if transcript.language_code == 'en' and transcript.is_generated == True:
                en_transcript = transcript.fetch()
                # return txt file (only containng text - no timestamps)
                txt_formatted = txt_formatter.format_transcript(en_transcript)
                with open(output_folder+vid_id+'.txt', 'w', encoding='utf-8') as txt_file:
                    txt_file.write(txt_formatted)
                    # print file_name to see progress
                    print(vid_id)
                    HasTranscript.append(vid_id)
    # I added this to overcome a 'transcriptsDisabled' error message
    except:
        print("no transcript: ", vid_id)

    i = i + 1

# output video_ids that have a transcript to csv file
data = {'HasTranscript': HasTranscript}
df_out = pd.DataFrame(data)
append_file = 'TranIds_{0}'.format(metadata_file)
df_out.to_csv('TranIds//'+append_file, encoding='utf8')
