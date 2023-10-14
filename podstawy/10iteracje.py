fruits = ["apple", "orange", "pear", "banana", "apple"]

print("Start")

for fruit in fruits:
    if fruit == "pear": continue
    if fruit == "banana": break
    print(fruit)


print("Stop")