# Kalkulator BMR - Basal metabolic rate
# - na podstawie wzoru BMR dostępnego np. na wikipedii w konsoli oblicz BMR

height = int(input("Wzrost w cm: "))
weight = int(input("Waga: "))
age = int(input("Wiek: "))
gender = input ("Płeć (z/m): ")
activity = input("Określ swoją aktywność poprzez wpisanie odp liczby:\n - Praca siedząca, brak dodatkowej aktywności fizycznej (1)\n - Praca niefizyczna, mało aktywny tryb życia (2)\n - Lekka praca fizyczna, regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu (3)\n - Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu (4)\n - Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu 2,0) (5): ")

if gender == "z":
    S = -161
if gender == "m":
    S = 5
PPM = 10 * weight + 6.25 * height - 5 * age + S

match activity:
    case "1":
        activity = 1.2
    case "2":
        activity = 1.4
    case "3":
        activity = 1.6
    case "4":
        activity = 1.8
    case "5":
        activity = 2.0    

print("Dzienne zapotrzebowanie kaloryczne wynosi:", PPM * activity, "kcal")