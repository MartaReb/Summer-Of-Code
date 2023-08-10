# Wyobraź sobie, że jesteś bioinformatykiem i otrzymujesz kod genetyczny do analizy.
DNA = "ACTGTGCTGACTCCCGGTGCTGCCGCTGCCATAGCTAAAGCCCGGGTCCTGGTAGGCAGGCGGGAAGCAGGGTGGGGGTCCCGGGTACTGGTAGGGGTAGCCCTGACCCAGAGGCGGGGGGGCAGCCGGGTGGGGCAGCGGGGCCAGCGTGTCCTGAA-CGAAGTCCCACTGGAGCCACTGTTGAGTCAGGGTGGCGAGATCTGGCGGNNNAGGGTAGGTGAGGGCCGCGGAGGGGCCTCCGGCGTTCCCCTCCCCCCCGCCCTGAAACCCGAAGCCCCCACTCACTGCTGCAGAGATCCCCTGAAAACGTAGTAGCACTGCTCgagacAGGTGATCTGTTGACCTGAAACCGCAGGAAGCCGTGCTTCAGCAAGCTGCTGGCGTACTTCCGGGCCT---GCCGCTCCTTGAAGCCCTCCACGTGTGTGTACAGCCAGTCCACCACGTCCGCCCCTGGCCGGCACCAGCGGTCAGCCCGCAGCCTCGAGGCAAGCAGCCCTGCCNNTGGCACTATCCGC-CGCGGGGACGGCCACTCACCGATGACGGCATNNGCGATGGTGATCTTGAGCCACATGCGGTCGCGGATCTCCAGTCCCGAG---GGCAGCTGCATGACCCGGACGACGGCGCTCATGTCACtcaccgtcagcggcgcctcttccagCCAGCTCTGCAAAGCACAGACAGCCCCGCTTCGCCCCAGCATCTGAAAGCGGGGGACTCggcAcgCTGCACCCCCAGGGGAGCCTCTGGGCAGAGCCTGCGCCAGGGCGCAAGCTGGACGGTGCGTGACAGCAGGGCCCCGGCCCACTGCAGGATGCACCCCCGTGAGGCTGGGGCGTGAGCAGGGGGGTTGGACAtttAGTCTCCCACTTCTACAGACACTTTTCATCAGGATCCTAGGCACAAACTGGGCTGAAACCCCACCCTGCAGACCAGGAAGTAATGAGAACAGGGCAGGCCCCTTCCCCTCNNCGCATGCC-CACCCGAGAGCGCAGGCTGTTAGTCGTGTTAATGGCAGGAAGCAGAATGGAGACCTGGCCCCTGCCTCTGAA-CCGTGGGTGCTCaactggctaGCCCTACGTACATCCCCTGTTCcggCCAACACACAGACATGAGCAGGATGGGCTGCACAAGGTGGGCACGGGTGCCTGTGCACACGTCTGTGCAGGGAGTTGGGGACAGGCAACACACACGTGTCACAGCCCCATGACGGggcaattgcGCCATGCTGGCTGAATGGCAGAGACGCCCCTCCAAGCCTCGGTTTCTGCTGGGGCCCTCAGGAGCTGCCACTTACGTGGAGCACCAGGCACGGAGCTGGTTAGTGAGGAGGAGCTGGTGCGCGTGACGGCGCTGGAGCAGGGACTCGTACCGTAGCGGGGCAGGGCNNNTGTCAGTGCCGCCGTGTGGtcagcggcgatCGGCG-GGTCGATGGGCCGCACCGGGTCAGCTGGGTGNAGACACGTGGCGATGACAGGCGGACAGATGGACAGGGTGGGAGGGCAGGGTGCAGGGCACAGAGGAGAGAGGCCTTCAGGCTAGGTAGGCGCCCCCTCCCCATCCCGccccGTGTGCCCCGAGGGCCACTCACCCCGTGGGACGGTGAAGTAGCTTCG-GGCGTTGGGTCCAGCACTTGGCCACAGTGAGGCTGNAAATGGCTGCAGGAACGGTGGTCCCCCCGCAAGGCCCCCATGGTCCCACCTCCCTGCCTGGCCCCTCCCGCTCCAGCGCCNCCAGCC"
# Policz ile razy występuje w kodzie każda zasada azotowa – adenina, cytozyna, guanina, tymina.
DNA = DNA.upper()
A = DNA.count("A")
C = DNA.count("C")
G = DNA.count("G")
T = DNA.count("T")
print(f"Adenina: {A}, Cytozyna: {C}, Guanina: {G}, Tymina: {T}")
# Policz wystąpienia sekwencji GAGA i zamień je na AGAG
GAGA = DNA.count("GAGA")
print("Liczba wystąpień sekw. GAGA: ", GAGA)
DNA = DNA.replace("GAGA","AGAG")
# Znajdź miejsce (indeks) w łańcuchu, gdzie występuje 7 guanin z rzędu
Gx7 = DNA.find("G"*7)
print(f"Miejsce gdzie występuje 7 guanin z rzędu: {Gx7} indeks")
# Znajdź miejsce (indeks) , gdzie od końca łańcucha występuje 6 cytozyn
Cx6 = DNA.rfind("C"*6)
print(f"Miejsce gdzie występuje 6 cytozyn z rzędu: {Cx6} indeks")
# Policz ile razy w kodzie pojawiła się sekwencja CTGAAA
CTGAAA = DNA.count("CTGAAA")
print("Liczba wystąpień sekw. CTGAAA: ", CTGAAA)
# W sekwencji CTGAAA czasem mutuje ostania litera A, wówczas jakość ostatniej litery może być wątpliwa. Ile sekwencji znajdziesz, jeśli weźmiesz pod uwagę wątpliwą, ostatnią adeninę?
incorrectA = DNA.count("CTGAA")- DNA.count("CTGAAA")
print("Wątpliwa ilość sekwencji: ", incorrectA)
# Oczyść DNA z wszystkich błędów. Na podstawie czystej nici utwórz odpowiadającą jej nić RNA (nić RNA w miejscu tyminy będzie mieć uracyl (U))
DNA = DNA.replace("-","").replace("N","")
RNA = DNA.replace("T","U")
print(RNA)