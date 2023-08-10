# Napisz program z wykorzystaniem pętli while, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
# Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
x = 0
z = 0
while x < 10:
    z = z + (x + 1)
    print(z)
    x += 1