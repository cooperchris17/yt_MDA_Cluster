# yt_MDA_Cluster

This is a companion repository for the PhD thesis "The identification and evaluation of informal YouTube videos as optimal resources for teaching conversational English" by Christopher R. Cooper

The process was piloted in the following paper:

Cooper, C. R. (2023). The identification of YouTube videos that feature the linguistic features of English informal speech. Applied Corpus Linguistics, 3(3), 100068. https://doi.org/10.1016/j.acorp.2023.100068



Here is a summary of what is available in each folder:

a_corpus_compilation


The Python code used to 
•	extract the video IDs from the YouTube Data API
•	Download transcripts of the videos
•	Clean the metadata



b_transcript_accuracy

The transcript for the 10 randomly sampled videos (gold standard, ASR, manual) and the Python code used to calculate the word error rate



c_yt22_preprocessing
The Python code used to pre-process the YouTube transcripts

d_MD_and_Cluster_Analysis
•	The dimension scores for the YT22 and Spoken BNC 2014 (yt22_bnc_dim_grey.csv)
•	the R code used for hierarchical cluster analysis and the Python code used for k-means clustering
•	The normalised frequency counts (“Statistics_…”) for the MD analysis linguistic features
e_topic_modelling
The .csv file containing the metadata that was used to make the topic modelling texts and the Python code to run the topic modelling. 

f_machine_learning_classification
The Python code and data for the different machine learning models that were trialled in the current study. This includes…
•	The 3 csv files containing the data used in the models
•	“get embeddings” notebooks for BERT and Open AI
•	The models that were built with linguistic features, BERT embeddings and Open AI embeddings (GPT)
•	The final model is available in “_Final_Model_and_YT22_Prediction.ipynb”
•	the CEFR Listening Corpus has not been made available for copyright reasons

g_supplementary_data
•	The Excel spreadsheets that were used for the qualitative coding in Section 4.6 and 
•	a .csv file including metadata, dimension scores, cluster information, topic information and the CEFR level for each video in the YT22
