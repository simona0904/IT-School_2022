# sa gasim suma multiplilor de 3 si 5 in intervalul 0 - 1000:

multipli_3 = list(range(3, 1001, 3))          # list = convertim la lista
multipli_5 = list(range(5, 1001, 5))

print(sum(set(multipli_3 + multipli_5)))  

# folosind set la rezolvarea problemei evitam duplicarea anumitor elemente.