produkty = ["mleko", "ser", "parówki"]
wieciej_produktow = ["majonez", "keczup"]

print(produkty)
print(type(produkty))

print(produkty[0])
print(produkty[1:])

produkty.append("jajka")
print(produkty)
print(produkty.count("mleko"))

produkty.extend(wieciej_produktow)
print(produkty)

print(produkty.index("parówki"))

produkty.insert(1,"dżem")
print(produkty)

produkty.pop(-1)
print(produkty)

produkty.remove("mleko")
print(produkty)

produkty.clear()
print(produkty)

produkty = ("mleko", "ser", "parówki")
print(produkty)