# Skrypt zapyta użytkownika o wiek. Jeżeli użytkownik jest przed 18 wyświetli informację „Użytkownik niepełnoletni” oraz zwróci ile lat zostało użytkownikowi do pełnoletności. Użytkownikom pełnoletnim wyświetli informację „Użytkownik pełnoletni”. Sprawdź czy wiek użytkownika nie przekracza 100 lat i wyświetl komunikat „200 lat ♫”.

age = int(input("Ile masz lat? "))

if age < 18:
    print(f"Użytkownik niepełnoletni. Zostało Ci jeszcze {18 - age} lat do pełnoteności.")
elif age > 100:
    print("200 lat ♫")
else:
    print("Użytkownik pełnoletni.")  


    
