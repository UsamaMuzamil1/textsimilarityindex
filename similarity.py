import pandas as pd


data = {
    'Name': ['Ali Hassan','Talha Malik','Usama Muzammil','Hamza Khan' ,'Mian Ahsan', 'Ahmad' ,'Sajid Ali','Syed Tayyab'],
    'RealName': ['Muhammad  Ali Hassan', 'Talha Malik', 'Usama Muzamil', 'Hamza Aslam', 'Ahsan Arif', 'Ahmad Butt', 'Sajid Ali', 'Syed Tayyab Malik']
}



df = pd.DataFrame(data)

import difflib
[(len(difflib.get_close_matches(x, df['Name'], cutoff=0.6))>1)*1
 for x in df['RealName']]

from difflib import SequenceMatcher, get_close_matches
df['best_match'] = [x for x in df['RealName'].str.lower() for x in get_close_matches(x, df['Name'].str.lower())]
df['similarity_score'] = df.apply(lambda x: SequenceMatcher(None, x['RealName'].lower(), x['best_match']).ratio(), axis=1)
df = df.assign(similarity_flag = df['similarity_score'].gt(0.6).astype(int)).drop(columns=['best_match'])
print(df)