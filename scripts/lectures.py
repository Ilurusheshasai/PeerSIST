import pandas as pd
import os

path = 'C:\\Users\\Sai_iluru\\python\\projects\\chen\\KT4\\'

files = []
# r=root, d=directories, f = files 
# this code is used to get the names of CSV files in a directory or folder.
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            file = file[:-4]
            files.append(file)

sublist = files[1:10]
print(sublist)

# here I have employed two different ways to find find lectures and explanations attended by a student.  
for user in sublist:
    df3 = pd.read_csv(fr"C:\Users\Sai_iluru\python\projects\chen\KT4\{user}.csv",usecols = ['cursor_time','item_id','action_type'])
    df4 = pd.read_csv(r"C:\Users\Sai_iluru\python\projects\chen\contents\lectures.csv",usecols = ['lecture_id','video_length'])

    df3.rename(columns = {'item_id':'lecture_id'}, inplace = True)
    df3 = pd.merge(df3, df4, on="lecture_id")
    df3 = df3[(df3.action_type == 'pause_video')]

    le_at = [] 
    le_at.append(df3['lecture_id'].unique())
    print("Lectures attended by "+ user + " " + str(len(le_at[0])))
    #print(le_at[0])
    
    #Using regax to find expalnations
    df4 = pd.read_csv(fr"C:\Users\Sai_iluru\python\projects\chen\KT4\{user}.csv",usecols = ['item_id'])
    regex = 'e.*'
    df4 = df4[df4.item_id.str.match(regex)]
    le_at = [] 
    le_at.append(df4['item_id'].unique())
    print("explanations attended by "+ user + " " + str(len(le_at[0]))+ "\n")
    #print(le_at[0])

    
