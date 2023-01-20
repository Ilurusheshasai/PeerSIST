import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

######################### Question_id vs total_attempts ########################
df = pd.read_csv(r"C:\Users\Sai_iluru\python\projects\chen\accuracy.csv")
scatter = df.plot(x = 'Question_id', y = 'total_attempts', kind='scatter', c= 'green');
scatter.set_title('Question_id vs total_attempts');
plt.show()

######################## accuracy of user 1,3,5 #######################

data = {'user': ["u1", "u3", "u4"],
        'accuracy': [0.631849315,0.375,0.679830748]
       }
df1 = pd.DataFrame(data)
#print(df1)
plot1 = df1.plot(x = 'user', y = 'accuracy',kind = 'bar')
plt.axhline(y=0.65641814, color='r', linestyle='-')
plot1.set_title('user vs accuracy');
plt.show()

######################### plot of Question_id vs overall_accuracy ######################################
plot = df.plot(x = 'Question_id', y = 'overall_accuracy', kind='scatter', c= 'green')
plot.set_title('Question_id vs overall_accuracy');
plt.show()

################################# plot ###################################
###################### this data was gathered from code of table1.py #########################
################################## Histogram ##############################################
user =  ["u1", "u3", "u4","u10", "u100", "u1000", "u10004", "u100043", "u10005", "u1001", "u10010", "u10011"]
accuracy = [63.1849315,37.5,67.9830748,100,46.42857142857143,44.45694991558807,64.76282671829622,39.11671924290221,65.86538461538461,13.333333333333334,50.80213903743316,66.3594470046083]
correctly_answered = [369,3,482,1,13,790,1338,372, 411,2,95,288]
total_answered = [584,8,709,1,28,1777,2066,951,624,15,187,434]
plt.plot(user,accuracy,'b')
plt.axhline(y=65.641814, color='r', linestyle='-')
plt.title('user vs accuracy')
plt.show()

 
# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
 
# Set position of bar on X axis
br1 = np.arange(len(user))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
 
# Make the plot
plt.bar(br1, correctly_answered, color ='r', width = barWidth,
        edgecolor ='grey', label ='correctly_answered')
plt.bar(br2, total_answered, color ='g', width = barWidth,
        edgecolor ='grey', label ='total_answered')
 
# Adding Xticks
plt.xlabel('users', fontweight ='bold', fontsize = 15)
plt.ylabel('Answered', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(user))],
        ["u1", "u3", "u4","u10", "u100", "u1000", "u10004", "u100043", "u10005", "u1001", "u10010", "u10011"])
 
plt.legend()
plt.show()

######################################### Each question accuracy ##################################
df = pd.read_csv(r"C:\Users\Sai_iluru\python\projects\chen\accuracy.csv")
scatter = df.plot(x = 'Question_id', y = 'individual_q_accuracy', kind='scatter', c= 'green');
scatter.set_title('Question_id vs individual_q_accuracy');
plt.show()

##################