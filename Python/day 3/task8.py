# Stwórz prostą grę zgadywankę. Komputer losuje wartość z przedziału od 1-30. Poproś użytkownika o zgadnięcie liczby. Program pyta użytkownika o podanie liczby tak długo, dopóki gracz nie zgadnie.
import random

random_number = random.randrange(1, 31)
user_number = int(input("Podaj liczbę naturalną z przedziału 1-30: "))

while True:
    if user_number == random_number:
        print("Zgadłeś! To ta liczba!")
        break
    else:
        user_number = int(input("To nie ta liczba, zgaduj dalej! "))