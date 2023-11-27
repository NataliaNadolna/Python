file = open("plik.txt", "r")
# print(file.read(5))
# file.seek(2)

for line in file.readlines():
    print(line.rstrip())
    
# print(file.readline())


file.close

# \n nowa linia