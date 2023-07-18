# Utwórz skrypt, który zapyta użytkownika o imię, nazwisko i numer telefonu, a następnie:
question = input("Napisz imię, nazwisko i numer telefonu: ")
firstName,lastName,phoneNumber = question.split(" ")
# Sprawdź czy imię i nazwisko składają się tylko z liter, a nr tel składa się wyłącznie z cyfr (wyświetl tę informację jako true/false)
print(firstName.isalpha())
print(lastName.isalpha())
print(phoneNumber.isdigit())
# Użytkownicy bywają leniwi. Nie zawsze zapisują imię czy nazwisko z dużej litery – popraw ich
print(firstName.title())
print(lastName.title())
# Niektórzy podają numer telefonu z myślnikami lub z spacjami, usuń zbędne znaki z numeru
phoneNumber.replace(" ", "")
phoneNumber.replace("-", "")
# Zakładając, że twoi użytkownicy noszą polskie imiona, sprawdź czy użytkownik jest kobietą
print(firstName.endswith("a"))
# Połącz dane w jeden ciąg personal za pomocą spacji
personal = " ".join(question)
print(personal)
# Policz liczbę wszystkich znaków w napisie personal
print(len(personal))
# Podaj liczbę tylko liter w napisie personal
personal = personal[:-18]
print(len(personal.replace(" ", "")))