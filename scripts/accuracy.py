import pandas as pd
import numpy as np

df1 = pd.read_csv(r"C:\Users\Sai_iluru\python\projects\chen\finaltable2V2.csv")
x = df1.correct_attempts_by_u1/df1.total_attempts_by_u1
df1.insert(9, "accuracy_of_u1", x)

y = df1.correct_attempts_by_u3/df1.total_attempts_by_u3
df1.insert(10, "accuracy_of_u3", y)

z = df1.correct_attempts_by_u4/df1.total_attempts_by_u4
df1.insert(11, "accuracy_of_u4", z)


df1.to_csv('accuracy.csv')
