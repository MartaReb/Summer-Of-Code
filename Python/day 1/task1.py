# kalkulator BMI
# - na podstawie wzoru BMI w konsolu oblicz swoje BMI
height = int(input("Podaj wzrost w cm: "))/100
weight = int(input("podaj wagę: "))
BMI = weight / (height ** 2)

# - spróbuj napisać rozwiązanie w jednej linii
print("Twoje BMI wynosi ", weight / (height ** 2))