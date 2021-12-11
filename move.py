import os

path = "/Users/duytran/Downloads/Photos2021"
url = "/Users/duytran/Downloads/Photos2021/Video"
# toFile = "/Users/duytran/Desktop/text.txt"
# fromFile ="/Users/duytran/textcopy.txt/"

data = []

for filename in os.listdir(path):
    if filename.endswith(".jpg"):
        data.append(filename)
        for i in data:
            print(os.path.join(path, i))
            try:
                if os.path.exists(os.path.join(url, i)):
                    print("there is already a file there")
                else:
                    os.replace(os.path.join(path, i), os.path.join(url, i))
                    print(os.path.join(path, i) + " was moved")
            except FileNotFoundError:
                print(os.path.join(path, i) +" was not found")




