# Utwórz skrypt, który zapyta użytkownika o imię, nazwisko i numer telefonu, a następnie:
firstName = input("Napisz imię: ")
lastName = input("Napisz nazwiasko: ")
phoneNumber = input("Napisz nr telefonu: ")
# Sprawdź czy imię i nazwisko składają się tylko z liter, a nr tel składa się wyłącznie z cyfr (wyświetl tę informację jako true/false)
print("Czy imię składa się tylko z liter? ", firstName.isalpha())
print("Czy nazwisko składa się tylko z liter? ", lastName.isalpha())
print("Czy numer telefonu składa się z cyfr? ",phoneNumber.isdigit())
# Użytkownicy bywają leniwi. Nie zawsze zapisują imię czy nazwisko z dużej litery – popraw ich
firstName = firstName.capitalize()
lastName = lastName.capitalize()
# Niektórzy podają numer telefonu z myślnikami lub z spacjami, usuń zbędne znaki z numeru
phoneNumber.replace(" ", "").replace("-", "")
# Zakładając, że twoi użytkownicy noszą polskie imiona, sprawdź czy użytkownik jest kobietą
print("Czy imię jest kobiece: ", firstName.endswith("a"))
# Połącz dane w jeden ciąg personal za pomocą spacji
personal = firstName + " " + lastName + " " + phoneNumber
print(personal)
# Policz liczbę wszystkich znaków w napisie personal
print(len(personal))
# Podaj liczbę tylko liter w napisie personal
personal = personal[:-9]
print(len(personal.replace(" ", "")))