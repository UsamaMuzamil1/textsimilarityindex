import pandas as pd
from difflib import SequenceMatcher, get_close_matches
import difflib


# in this step I can load excel file to read data in it.
df =pd.read_excel("sim_index.xlsx")


def indexsimilarity(df):

 [(len(difflib.get_close_matches(x, df['Name'], cutoff=0.6))>1)*1
 for x in df['RealName']]


# then I can calculate the best match of column 1 which is available in column 2.
df['best_match'] = [x for x in df['RealName'].str.lower() for x in get_close_matches(x, df['Name'].str.lower())]


# now I can measure the similarity between two columns, with a range from 0% to 100%
df['similarity_score'] = df.apply(lambda x: SequenceMatcher(None, x['RealName'].lower(), x['best_match']).ratio()*100, axis=1)


# print the results
print(df)


# output can be stored in new excel file.
# df.to_excel("indexsimilarity.xlsx")
