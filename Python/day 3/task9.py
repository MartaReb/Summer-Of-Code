# Rozszerz grę z punktu powyżej. Gracz powinen otrzymać informację czy jego liczba jest za duża czy za mała.

import random

random_number = random.randrange(1, 31)
user_number = int(input("Podaj liczbę naturalną z przedziału 1-30: "))

while True:
    if user_number == random_number:
        print("Zgadłeś! To ta liczba!")
        break
    elif user_number > random_number:
        user_number = int(input("Podałeś za dużą liczbę! Próbuj dalej! "))
    else:
        user_number = int(input("Podałeś za małą liczbę! Zgaduj dalej! "))