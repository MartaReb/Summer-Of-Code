# Skrypt:
# - zapyta o Twoje imię
# - powita Cię po imieniu
# - zapyta o Twój wiek
# - zapyta o peron z Harrego Potter’a
# - odpowie (dowolnie łącząc wiek i peron), np. czy jest sens jechać do Hogwartu

name = input("Jak masz na imię? ")
print("Cześć,", name)
age = input("Ile masz lat? ")
platform = input("Z jakiego peronu dostaniesz się do Hogwartu? ")
print(f"Czy jest sens jechać w wieku {age} lat na peron {platform} ?")