import os

path = "pliki/01/dane.txt"
dir_path = os.path.dirname(path)
# open("test.txt", "w").close()

print(os.path.dirname(path))
print(os.path.basename(path))
print(os.path.abspath(path))

os.makedirs(dir_path)
open(path, "w").close()
