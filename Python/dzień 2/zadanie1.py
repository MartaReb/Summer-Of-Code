# Do zmiennej sentence przypisz zdanie: „Kurs Pythona jest prosty i przyjemny.”, a następnie:
sentence = "Kurs Pythona jest prosty i przyjemny."

# 1.Policz wszystkie znaki w napisie
print(len(sentence))

# 2.Nie modyfikując zmiennej sentence wyświetl słowo „prosty”
print(sentence[18:24])

# 3. Wyświetl znak o indeksie (czy za każdym razem rozumiesz co się dzieje?):7, 12, -4, 37
print(sentence[7])
print(sentence[12])
print(sentence[-4])
print(sentence[37])

# 4.Wprowadź do zdania 2 błędy ortograficzne
sentence = sentence[0]+"ó"+sentence[2:8]+"t"+sentence[9:]
print(sentence)
