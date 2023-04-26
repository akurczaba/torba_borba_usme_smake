print("Podaj nazwę użytkownika:")
nazwa = input()
print("Podaj hasło:")
haslo = "dupa"
haslo = input()
if haslo == "dupa":
    print("Dobrze! Wpisz hasło po raz drugi:")
    haslo = input()
else:
    print("Złe hasło. Wpisz ponownie:")
    haslo = input()  
if haslo != "dupa":
    print("Hasła niezgodne")
if haslo == "dupa":
    print("Czy masz 18 lat?")
    potwierdzenie = input()
    if potwierdzenie == "tak":
        print("Możesz założyć konto")
    elif potwierdzenie == "nie":
        print("Masz zgodę rodziców?")
        zgoda = input()
        if zgoda == "tak":
            print("Możesz założyć konto")
        elif potwierdzenie == "nie":
            print("Nie możesz założyć konta")
else:
    print("bledne haslo")

