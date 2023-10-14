import os

lista = os.listdir(".") # . .. C:/Windows katalog
# print(lista)

for item in lista:
    if os.path.isfile(item):
        print("{} jest plikiem".format(item))
    if os.path.isdir(item):
        print(item + " jest folderem")
    else:
        print(item + " nie jest plikiem, ani folderem")