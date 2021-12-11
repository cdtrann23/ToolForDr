import os

path = os.chdir("/Users/duytran/Desktop/QuocKy")

i = 0

for file in os.listdir(path):
    newName = "pic{}.jpg".format(i)
    os.rename(file, newName)

    i += 1