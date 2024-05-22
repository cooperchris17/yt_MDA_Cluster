'''
This script tags a text with the Stanford Caseless tagger
then it converts the text from a list of tuples to a list of lists (so it can be edited)
then it capitalizes any word that has been identified as a proper noun
then prints the text with capitalized proper nouns
by printing the first item ([0]) in each list with a ' ' at the end of each word

One problem is words like 'us' (U.S. - for United States) are converted to 'Us'

As an indication, this took around 1 hour to process about 2,700 medium length YouTube transcripts
'''

import os, glob
from nltk import word_tokenize
from nltk.tag import StanfordPOSTagger
from logsnag import LogSnag

logsnag = LogSnag(token='INPUT_API_TOKEN', project='python_script_finished')

# https://github.com/Computational-Content-Analysis-2018/Content-Analysis/issues/6
# Add the jar and model via their path (instead of setting environment variables):
os.environ['JAVAHOME'] = 'C:/Program Files/Java/jre1.8.0_311/bin/java.exe'

# https://stackoverflow.com/questions/34726200/nltk-was-unable-to-find-stanford-postagger-jar-set-the-classpath-environment-va
# I used an older version of the Stanford tagger that I had downloaded
# I couldn't get it to work with the new version, there is no models folder
jar = 'C:/Users/coope/Documents/PHD/Corpora/Taggers/Stanford_Tagger/stanford-postagger-4.2.0.jar'
model = 'C:/Users/coope/Documents/PHD/Corpora/Taggers/Stanford_Tagger/models/english-caseless-left3words-distsim.tagger'
# specify the tagger (linking to previously specified models)
pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')

# iterate through every file in the folder that is a text file
for file in glob.iglob('**', recursive=False):
    if os.path.isfile(file): # filter dirs
        if file.endswith('.txt'): # avoid editing .py files, etc
            with open(file, 'r') as input:
                filedata = input.read()
                # tag the texts
                text = pos_tagger.tag(word_tokenize(filedata))
                # convert tagged text to a list of lists (so it can be edited)
                list_text = list(map(list, text))
                # capitalize any proper nouns
                for item in range(len(list_text)):
                    if list_text[item][1] == 'NNP':
                        list_text[item][0] = list_text[item][0].capitalize()
                    with open('temp.txt', 'a') as output:
                        print(list_text[item][0], end=' ', file=output)

            # replace file with original name
            os.replace('temp.txt', file)

logsnag.publish(
    channel='finished',
    event='Capitalisation is finished',
    icon='🐍',
    notify=True
    )
