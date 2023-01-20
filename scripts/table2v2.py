
import pandas as pd
from collections import Counter


df1 = pd.read_csv(r"C:\Users\Sai_iluru\python\projects\chen\subset\u1.csv",usecols = ['item_id','user_answer'])
df1.dropna(subset=['user_answer'], inplace=True)
dic1 = df1['item_id'].value_counts().to_dict()
#print(dic1)

df2 = pd.read_csv(r"C:\Users\Sai_iluru\python\projects\chen\subset\u3.csv",usecols = ['item_id','user_answer'])
df2.dropna(subset=['user_answer'], inplace=True)
dic2 = df2['item_id'].value_counts().to_dict()
#print(dic2)

df3 = pd.read_csv(r"C:\Users\Sai_iluru\python\projects\chen\subset\u4.csv",usecols = ['item_id','user_answer'])
df3.dropna(subset=['user_answer'], inplace=True)
dic3 = df3['item_id'].value_counts().to_dict()
#print(dic3)

total_attemps_for_all_questions = dict(Counter(dic1)+Counter(dic2)+Counter(dic3))

df = pd.read_csv(r"C:\Users\Sai_iluru\python\projects\chen\contents\questions.csv",usecols = ['question_id','part'])
type = df['part'].tolist()

#add a column defining the number of times a question is answered and the number of times its answered correctly
############################      FOr user 1         ############################  
dfu1 = pd.read_csv(fr"C:\Users\Sai_iluru\python\projects\chen\subset\u1.csv",usecols = ['item_id','user_answer'])
dfq1 = pd.read_csv(r"C:\Users\Sai_iluru\python\projects\chen\contents\questions.csv",usecols = ['question_id','correct_answer'])
dfu1.dropna(subset=['user_answer'], inplace=True)
# dic1 is dictionary which reflects how many times a user has answered a question
dic1 = dfu1['item_id'].value_counts().to_dict()
dic1a = dict(dic1)
dic1a = dict.fromkeys(dic1a, 0)
dic1a_keys = list(dic1a.keys())


#print(dic1a)

# renaming the question_id with item_id to Merge both the data frames
dfq1.rename(columns = {'question_id':'item_id'}, inplace = True)
dfq1 = pd.merge(dfq1, dfu1, how="right", on="item_id")

#Checking correct answers
dfq1.loc[dfq1['correct_answer'] == dfq1['user_answer'], 'points'] = 'correct' 
for i in dic1a_keys:
    correct = len(dfq1[(dfq1['item_id'] == i) & (dfq1['points']=='correct')])
    dic1a.update({i:correct})

#print(dict(sorted(dic1a.items(), key=lambda item: item[1],reverse=True)))

########################## for u3 ###################################

#add a column defining the number of times a question is answered and the number of times its answered correctly
############################      FOr user 3        ############################  
dfu3 = pd.read_csv(fr"C:\Users\Sai_iluru\python\projects\chen\subset\u3.csv",usecols = ['item_id','user_answer'])
dfq3 = pd.read_csv(r"C:\Users\Sai_iluru\python\projects\chen\contents\questions.csv",usecols = ['question_id','correct_answer'])
dfu3.dropna(subset=['user_answer'], inplace=True)
# dic1 is dictionary which reflects how many times a user has answered a question
dic3 = dfu3['item_id'].value_counts().to_dict()
dic3a = dict(dic3)
dic3a = dict.fromkeys(dic3a, 0)
dic3a_keys = list(dic3a.keys())


#print(dic1a)

# renaming the question_id with item_id to Merge both the data frames
dfq3.rename(columns = {'question_id':'item_id'}, inplace = True)
dfq3 = pd.merge(dfq3, dfu3, how="right", on="item_id")

#Checking correct answers
dfq3.loc[dfq3['correct_answer'] == dfq3['user_answer'], 'points'] = 'correct' 
for i in dic3a_keys:
    correct = len(dfq3[(dfq3['item_id'] == i) & (dfq3['points']=='correct')])
    dic3a.update({i:correct})

#print(dict(sorted(dic3a.items(), key=lambda item: item[1],reverse=True)))


########################## for u4 ###################################

#add a column defining the number of times a question is answered and the number of times its answered correctly
############################      FOr user 4        ############################  
dfu4 = pd.read_csv(fr"C:\Users\Sai_iluru\python\projects\chen\subset\u4.csv",usecols = ['item_id','user_answer'])
dfq4 = pd.read_csv(r"C:\Users\Sai_iluru\python\projects\chen\contents\questions.csv",usecols = ['question_id','correct_answer'])
dfu4.dropna(subset=['user_answer'], inplace=True)
# dic1 is dictionary which reflects how many times a user has answered a question
dic4 = dfu4['item_id'].value_counts().to_dict()
dic4a = dict(dic4)
dic4a = dict.fromkeys(dic4a, 0)
dic4a_keys = list(dic4a.keys())


#print(dic1a)

# renaming the question_id with item_id to Merge both the data frames
dfq4.rename(columns = {'question_id':'item_id'}, inplace = True)
dfq4 = pd.merge(dfq4, dfu4, how="right", on="item_id")

#Checking correct answers
dfq4.loc[dfq4['correct_answer'] == dfq4['user_answer'], 'points'] = 'correct' 
for i in dic4a_keys:
    correct = len(dfq4[(dfq4['item_id'] == i) & (dfq4['points']=='correct')])
    dic4a.update({i:correct})

#print(dict(sorted(dic4a.items(), key=lambda item: item[1],reverse=True)))

################################### counter ####################

no_of_correct_attempts_for_each_question  = dict(Counter(dic1a)+Counter(dic3a)+Counter(dic4a))


with open('finaltable2V3.csv','w') as f:
    keys_union = set(total_attemps_for_all_questions.keys()).union(set(no_of_correct_attempts_for_each_question.keys())).union(set(dic1.keys())).union(set(dic1a.keys())).union(set(dic3.keys()).union(set(dic3a.keys())).union(set(dic4.keys()).union(set(dic4a.keys()))))
    f.write('Question_id,total_attempts,correct_attempts,total_attempts_by_u1,correct_attempts_by_u1,total_attempts_by_u3,correct_attempts_by_u3,total_attempts_by_u4,correct_attempts_by_u4\n')
    for k in sorted(keys_union):
        
        f.write("{0},{1},{2},{3},{4},{5},{6},{7},{8}\n".format( k,
                        [total_attemps_for_all_questions[k] if k in total_attemps_for_all_questions.keys() else "0"][0],
                        [no_of_correct_attempts_for_each_question[k] if k in no_of_correct_attempts_for_each_question.keys() else "0"][0],
                        [dic1[k] if k in dic1.keys() else "0"][0],
                        [dic1a[k] if k in dic1a.keys() else "0"][0],
                        [dic3[k] if k in dic3.keys() else "0"][0],
                        [dic3a[k] if k in dic3a.keys() else "0"][0],
                        [dic4[k] if k in dic4.keys() else "0"][0],
                        [dic4a[k] if k in dic4a.keys() else "0"][0]
                        ))