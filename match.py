import pandas as pd

# in this step I can load excel file to read data in it.
df =pd.read_excel("match.xlsx")

# now , I can create function that is used to compare two string columns
def similarityfunc(x):
    len_col1 = len(x[0])
    count = 0
    for y in range (0, len_col1):
        try:
            if x[0][y] == x[1][y]:
                count += 1
            else:
                pass
        except:
            break
    return round(((count* 100)/len_col1),2)  #now, we can calculate the matching percentage out of 100 between two columns


# now create new column and measure the similarity between two columns, with a range from 0% to 100%
df['% of Similarity'] = df.apply(similarityfunc, axis = 1)

# print the results
print(df)

