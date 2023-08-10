# Utwórz zbiór imion męskich i żeńskich. Poproś użytkownika o podanie imienia. Sprawdź czy imię jest męskie czy żeńskie i wyświetl na ten temat informację. Jeżeli imienia nie ma na liście wyświetl komunikat „Nie znamy tego imienia.” Następnie użytkownik poda informację czy imię jest męskie czy żeńskie. Dodaj imię do listy.

dict_names = { 
    "Marta" : "żeńskie",
    "Anna" : "żeńskie",
    "Zofia" : "żeńskie",
    "Maja" : "żeńskie",
    "Hanna" : "żeńskie",
    "Monika" : "żeńskie",
    "Magda" : "żeńskie",
    "Rafał" : "męskie",
    "Mateusz" : "męskie",
    "Jan" : "męskie",
    "Adam" : "męskie",
    "Piotr" : "męskie",
    "Paweł" : "męskie",
    "Antoni" : "męskie"
    }

name = input("Podaj jakieś imię: ")

if name in dict_names:
    print("To imię jest", dict_names[name])
else:
    print("Nie mamy tego imienia.")
    gender = input("To imię żeńskie czy męskie? Wpisz z lub m: ")
    if gender == "z":
        dict_names[name] = "żeńskie"
    else:
        dict_names[name] = "męskie"
    print (list(dict_names.keys()))