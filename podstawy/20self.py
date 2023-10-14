
class Calculator:
    def __init__(self):
        self.ostatni_wynik = 0
        print("Init")

    def dodaj(self, a, b):
        wynik = a + b
        self.ostatni_wynik = wynik
        print(wynik)

    def odejmij(self, a, b):
        wynik = a - b
        self.ostatni_wynik = wynik
        print(wynik)

calc = Calculator()
calc.dodaj(3,5)
print("Ostatni wynik: {}".format(calc.ostatni_wynik))

calc2 = Calculator()
