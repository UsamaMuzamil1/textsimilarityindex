import pandas as pd



df =pd.read_excel("sim_index.xlsx")

def indexsimilarity(x, y):
    intersection = len(list(set(x).intersection(y)))
    union = (len(x) + len(y)) - intersection
    return float(intersection / union)


new_df = pd.DataFrame(columns=['Name', 'RealName', 'Similarity'])

# order the rows by name
new_df = new_df.sort_values(by=['Name'])

# order by similarity size
new_df = new_df.sort_values(by=['Similarity'], key=lambda x: x.str.len(), ascending=True)

# make sure there is only one row for each name
new_df = new_df.drop_duplicates(subset=['Similarity'])
print(new_df)

print(pd.DataFrame(df, columns=['Name', 'RealName', 'Similarity']))























'''def jaccard_set(list1, list2):
    intersection = len(list(set(list1)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union
a = [0, 1, 2, 5, 6]
b = [0, 14, 5, 6, 7, 2, 77, 8]
jaccard_set(a, b)
print(jaccard_set(list1=a, list2=b))
percenatge = jaccard_set(list1=a, list2=b) * 100
print(percenatge)'''








