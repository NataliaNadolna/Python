

class Calculator():

    # metody magiczne
    def __init__(self): # wykona się kiedy tworzymy instancję klasy
        print("init")

    def __del__(self):
        print("del")

    def __str__(self): # int()
        return "Hello"
    
    def __len__(self):
        return 5

    def dodaj(self, a, b):
        wynik = a + b
        print(wynik)

    def odejmij(self, a, b):
        wynik = a - b
        print(wynik)

calc = Calculator()
calc2 = Calculator()

calc.odejmij(2, 4)
calc2.dodaj(4,5)

print(calc)
print(len(calc))
