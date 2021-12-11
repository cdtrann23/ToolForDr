import os

path = "/Users/duytran/Downloads/Photos2021"



print("_"*15)
i = 0

for filename in os.listdir(path):
    if filename.endswith(".jpeg"): 
        # Your code comes here such as 
        print(filename)
        newName = "{}.jpg".format(i)
        os.rename(filename, newName)

        i += 1



