# Napisz skrypt obliczający wartość silnii. Rozwiąż zadanie za pomocą pętli for oraz pętli while.
# Wejście: „Podaj dowolną liczbę całkowitą do 15:” 4
# Wyjście: 4! = 24

user_number = int(input("Podaj dowolną liczbę całkowitą do 15: "))
x = 1
z = 1
while x != user_number:
    x = x + 1
    z = z * x
print(f"Silnia z {user_number} to {z}")

