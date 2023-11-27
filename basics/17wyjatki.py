
try:
    plik = open("test.txt", "r")
    plik.write("Hello") # read
    plik.close()

except FileNotFoundError as e:
    print("Plik nie istnieje")
    print(e)

except TypeError as e:
    print("Błąd typu danych")
    print(e)

except Exception as e:
    print("Nieznany błąd")
    print(e)