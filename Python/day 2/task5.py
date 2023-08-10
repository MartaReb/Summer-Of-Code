# Trzy dowolne liczby zapisz do trzech zmiennych.
x = int(input("x numer: "))
y = int(input("y numer: "))
z = int(input("z numer: "))

# Znajdź największą liczbę.
if (x > y) and (x > z):
    print("x is the graetest")
elif (y > x) and (y > z):
    print("y is the graetest")
else:
    print("z is the graetest")

# Wyświetl liczby od największej do najmniejszej.
if x < y:
    temp = x
    x = y
    y = temp
if x < z:
    temp = x
    x = z
    z = temp
if y < z:
    temp = y
    y = z 
    z = temp

print (x, y, z)

