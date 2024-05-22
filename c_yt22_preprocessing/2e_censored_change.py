'''
This script changes censored words '[ __ ]' to 'tamn'
Like the other scripts, it amends every file in the folder and subfolder
that the script is run from
'''

import re, os, glob
import time

# Grab Currrent Time Before Running the Code
start = time.time()

for file in glob.iglob('**', recursive=False):
    if os.path.isfile(file): # filter dirs
        if file.endswith('.txt'): # avoid editing .py files, etc
            with open(file, 'r') as input:
                filedata = input.read()
                # re.sub follows this format
                filedata = re.sub('\[ __ \]', 'tamn', filedata)

                with open('temp.txt', 'w') as output:
                    output.write(filedata)

            # replace file with original name
            os.replace('temp.txt', file)

# Grab Currrent Time After Running the Code
end = time.time()

total_time = end - start
print('It took this amount of time in seconds: '+str(total_time))

'''
It was 68 seconds for 37k transcripts
'''
