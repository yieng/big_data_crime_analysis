# README

The Reddit comments filtered by LSH were divided into two classes: UK-related and Chicago-related, and then fed through the programs cm.py and cm_original.py to produce JSON databases of the lower-case punctuation-free form of the comments and the original comments respectively.

The comments were then segmented into lists of words using split.py and split_uk.py for the Chicago and UK classes respectively. Next, the term frequency (TF) of each term in each comment was calculated using tf.py and tf_uk.py for the Chicago and UK classes respectively.

To calculate the inverse document frequency (IDF), distinct terms were first collected using term.py and dterm_uk.py for the Chicago and UK comment classes respectively. Then for every term, the number of comments containing it was counted using idf.py and idf_uk.py.

The output files from the TF and IDF programs, as well as the original comments, were the input files of tfidf.py and tfidf_uk.py. These two programs multiply the TF’s and IDF’s of each term in each comment, pick out the 5 terms with the highest TF.IDF scores, and then append them to the original comment.

Finally, relevant_chicago_illinois.py and relevant_uk.py go through the top 5 terms (in terms of TF.IDF scores) of each comment. If these 5 terms contain both location and crime type keywords, the corresponding comment is selected and written to a file named <crime type>_<location>.txt for the Chicago class of comments, or <crime type>_<location>_uk.txt for the UK class of comments.

Note that different sections in the programs were timed so that the programmer could better estimate the time needed to complete each procedure.
