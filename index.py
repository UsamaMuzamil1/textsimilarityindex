from difflib import get_close_matches, SequenceMatcher
from math import sqrt, pow, exp
import embeddings as embeddings
import nlp as nlp
import numpy as np
import pandas as pd
import openpyxl


# in this step I can load excel file to read data in it.
df =pd.read_excel("sim_index.xlsx")


# then I can calculate the best match of column 1 which is available in column 2.
df['best_match'] = [x for x in df['RealName'].str.lower() for x in get_close_matches(x, df['Name'].str.lower())]


# now I can measure the similarity between two columns, with a range from 0% to 100%
df['similarity_index'] = df.apply(lambda x: SequenceMatcher(None, x['RealName'].lower(), x['best_match']).ratio()*100, axis=1)


# apply function
# df['Similarity'] = df.apply(lambda x: x['Name'] if x['Name'] <= x['RealName']  else np.nan, axis=1)

# printing the dataframe
print(df)