
import os

path = 'C:\\Users\\Sai_iluru\\python\\projects\\chen\\KT4\\'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            file = file[:-4]
            files.append(file)

sublist = files[1:10]
print(sublist)

#print(sublist)
