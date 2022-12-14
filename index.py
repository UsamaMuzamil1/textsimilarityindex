import pandas as pd
import numpy as np

# read excel file
similar = pd.read_excel('sim_index.xlsx')

# compare column1 and column2  (1 means similar and 0 means not similar)
similar_col = np.where(similar.Name == similar.RealName, 1,0)*100

# create new column and find similarity
similar['Similarity'] = similar_col

# print the result
print(similar)
