import pandas as pd


data = {
    'Name': ['Ali Hassan','Talha Malik','Usama Muzammil','Hamza Khan' ,'Mian Ahsan', 'Ahmad' ,'Sajid Ali','Syed Tayyab'],
    'RealName': ['Muhammad  Ali Hassan', 'Talha Malik', 'Usama Muzamil', 'Hamza Aslam', 'Ahsan Arif', 'Ahmad Butt', 'Sajid Ali', 'Syed Tayyab Malik']
}


df = pd.DataFrame(data)

def jaccard_similarity(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection / union)


new_df = pd.DataFrame(columns=['Name', 'RealName', 'Similarity'])

for index, row in df.iterrows():
    similarity = []
    # save all the similarity scores in a list
    for index2, row2 in df.iterrows():
        similarity.append(jaccard_similarity(row['RealName'].split(','), row2['RealName'].split(',')))
    # find the indexes of the rows that have similarity score bigger than 0.8
    indexes = [i for i, x in enumerate(similarity) if x >= 0.8]
    # if there is more than one row with similarity score bigger than 0.8
    if len(indexes) > 1:
        # add the row to the new data frame
        new_df = pd.concat([new_df, pd.DataFrame(
            [[row['Name'], row['RealName'], ','.join([str(df.iloc[i]['id']) for i in indexes])]],
            columns=['Name', 'RealName', 'Similarity'])], ignore_index=True)

# order the rows by name
new_df = new_df.sort_values(by=['Name'])

# order by similarity size
new_df = new_df.sort_values(by=['Similarity'], key=lambda x: x.str.len(), ascending=True)

# make sure there is only one row for each name
new_df = new_df.drop_duplicates(subset=['Similarity'])
print(new_df)

print(pd.DataFrame(data, columns=['Name', 'RealName', 'Similarity']))