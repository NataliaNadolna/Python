
class Person():
    def __init__(self, name):
        self.name = name
        self.surname = "Kwiatkowski"
        self.age = 25

class Employee(Person):
    def __init__(self, position):
        super().__init__("Tomek")
        self.posotion = position
        self.specialization = "Python"

class Client(Person):
    def __init(self, name):
        super().__init__(name)
        self.ordered = "Website"

p = Person("Kamil")
print(p.name)

pracownik = Employee("Designer")
print(pracownik.name)

klient = Client("Kuba")
print(klient.name)