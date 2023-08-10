# Napisz prosty program, który wykona się zadaną przez użytkownika liczbę razy. Z każdym uruchomieniem pętli wyświetli informacje:
# – czy liczba jest wielokrotnością 3
# – czy liczba jest wielkorotnością 4
# – wyświtli „hurra” jeżeli liczba dzieli się zarówno przez 3 jak i 4
# – wyświetli gwiazdkę, jeśli żaden z powyższych warunków nie jest spełniony

number = int(input("Podaj liczbę: "))

for x in range(number):
    if number % 3 == 0:
        print("Podana liczba jest wielokrotnością 3")
    if number % 4 == 0:
        print("Podana liczba jest wielokrotnością 4")
    if number % 3 == 0 and number % 4 == 0:
        print("Hura")
    else:
        print("*")