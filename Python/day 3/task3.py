# Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem). Następnie powitaj każdą osobę na liście.
names = input("Wpisz dowolną liczbę imion ciągiem oddzielając je spacją: ")

for name in names.split():
    print("Cześć",name)