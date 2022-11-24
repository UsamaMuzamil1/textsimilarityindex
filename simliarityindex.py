from difflib import SequenceMatcher, get_close_matches

import pandas as pd
import openpyxl



df =pd.read_excel("sim_index.xlsx")

def jaccard_similarity(a, b):
    a = set(a)
    b = set(b)
    # calucate jaccard similarity
    return float(len(a.intersection(b))) / len(a.union(b))

df['best_match'] = [x for x in df['RealName'].str.lower() for x in get_close_matches(x, df['Name'].str.lower())]
df['similarity_index'] = df.apply(lambda x: SequenceMatcher(None, x['RealName'].lower(), x['best_match']).ratio()*100, axis=1)
print(df)

df.to_excel("saveindexsimilarity.xlsx")



