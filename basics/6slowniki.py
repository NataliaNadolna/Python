person = {"wiek": 20, "imie": "Ania"}

print(person)
print(type(person))

print(person["imie"])

print(person.get("wiek", "25"))
print(person.get("nazwisko", "Kowalska"))

print(person.keys())