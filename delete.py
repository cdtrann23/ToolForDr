import os
import glob

path = ""

a = glob.glob("*.mp4")
print(a)

for f in a:
    print(os.path.join(path, f))
    os.remove(os.path.join(path, f))
    