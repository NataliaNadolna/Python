fruits = ["apple", "orange", "pear", "banana", "apple"]

print("Start")
for i, fruit in enumerate(fruits):
    print("Sprawdzam {} {}".format(i, fruits[i]))
    if i==3:
        print("Nie jest ok")
        break
    print("Jest ok")

print("Stop")