from difflib import SequenceMatcher, get_close_matches

import pandas as pd
import openpyxl


# in this step I can load excel file to read data in it.
df =pd.read_excel("sim_index.xlsx")


# now , I can create function that is used to compare set of predicted labels
def jaccard_similarity(a, b):
    a = set(a)
    b = set(b)


# formula to calculate jaccard similarity
    return float(len(a.intersection(b))) / len(a.union(b))



# then I can calculate the best match of column 1 which is available in column 2.
df['best_match'] = [x for x in df['RealName'].str.lower() for x in get_close_matches(x, df['Name'].str.lower())]


# now I can measure the similarity between two columns, with a range from 0% to 100%
df['similarity_index'] = df.apply(lambda x: SequenceMatcher(None, x['RealName'].lower(), x['best_match']).ratio()*100, axis=1)


# print the results 
print(df)


# output can be stored in new excel file
df.to_excel("saveindexsimilarity.xlsx")



