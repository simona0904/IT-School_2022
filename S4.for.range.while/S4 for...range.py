# LOOPS = ITERATION = BUCLE
# este repetitia unui set de instructiuni

# ITERABLE este obiectul folosit intr-un iteration
# python poate itera doar printr-o colectie (string, lists), separata prin virgula.
# cu for putem executa o serie de instructiuni pt fiecare elem dintr-un obiect iterabil sau interva.
# sintaxa: for variable in iterable
# variabila  for loop va prelua PE RAND valoarea fiecarui elem din obiectul iterabil.

# lista_cumparaturi = [
#      "oua",
#     "paine",
#     "lapte",
#      "kiwi"
#  ]

# vrem sa afisam PE RAND elem din aceasta lista:

# print(lista_cumparaturi)      # rez: ["oua", "lapte", "paine", "kiwi"] adica lista
# print(lista_cumparaturi[0])   # rez: oua
# print(lista_cumparaturi[1])   #      paine
# print(lista_cumparaturi[2])   #      lapte
# print(lista_cumparaturi[3])   #      kiwi

# deci ca sa aceesam fiecare elem ar trebui sa folosim
# indexul, dar se paote mai usor cu ITERATION:

# for element in lista_cumparaturi:   # element va prelua pe rand valoarea fiecarui obiect: oua...
#     print(element)

# deci cu un singur cod am obtinut acelasi rez ca mai sus.


# Alt exemplu:lista cu liste in care avem aceeasi lista cump dar si pretul aferent.


# lista_cumparaturi = [
#     ["oua", 2],
#     ["paine", 5],
#     ["lapte", 3],
#     ["kiwi", 10]
#]

# noi trebuie sa iteram acum si sa spunem produsul x costa y bani.

# for element in lista_cumparaturi:           #element acum va fi o lista (['paine], 2)
#     print("Produsul " + element[0] + " are pretul de " + str(element[1]))

# rez: Prosudul oua are pretul de 2 ron
#      Produsul paine are pretul de 3 ron. etc..  
# 
#   

# EXECUTIA IN BUCLA FOR
# FUNCTIA RANGE() -INTERVALE

# START -> NR DE ITERATII ESTE MAI MIC DECAT NR DE ELEMENTE? -> DA -> AFISEAZA NR ITERATIEI.
#                                                            -> NU -> CONTINUA EXECUTIA.



# FOR LOOPS: permite executia unui bloc de cod de mai multe ori atat timp cat nr de ordine 
# este mai mic decat lungimea multimii date.( o multime poate fi si o lista de cumparaturi, de item-uri)
# primul nr de ordine este 0.
# for parcurge colectii de date   

 
# range() sintaxa:

# for i in range(10):                    # 10 este nr de iteratii:
                                         
# for i in range(3):                     # adica nr pana la 3, incepand cu 0 si fara a include pe 3.
#     print("Iteratia", i + 1)
#     print("i =", i)

# range(10) produce intervalul [0, 10] -nu il include pe 10
# 1.  i = 0  la prima iteratie i = 1
# 2.  i = 1
# 3.  i = 2
# i ne da primul element din multime
# in loc de i putem pune orice nume de variabila

# avem 3 tipuri de range():

# range(10) -> [0, 10] 0...9
# range(3, 10) -> [3, 10] -> 3...9
# range(3, 10, 2)-> de la 3 la 10 din 2 in 2


# for i in range(0, 11, 2):               # adica de la 0 la 10 din 2 in 2 ( 2 de la final reprezinta din cat in cat)
#     print("i =", i)                     # 0 = start   11 = stop    2 = step 
                                          # step is how much we add to i every time.




# range(11, 0)                            # nu returneaza nimic si ca mearga descrescator facem:


# for i in range(10, -1, -1):             # adica nr descrescatoare de la 10 in jos fara a include pe 10 si sa-l includa pe 0 
#     print("i =", i)                     # punem -1. -> 10...0.



# Exercitiu: program care afiseaza nr impare in interv [0 , 100]

# for i in range(1, 1001, 2):
#     print(i)

# # sau:

# for i in range(1001):
#     if i % 2 == 1:          # % modulo aflam care sunt nr pare sau impare
#         print(i)    



# nr prim este acela care se imparte la 1 si la el insusi.
# Scrieti un program care citeste de la tastatura un nr natural "n", 
# si afiseaza suma primelor n numere multiple de 5 si 3.


# n = int(input("n= "))
# suma = 0

# for i in range(3, n, 3):                     # pas="" se pune ca sa nu apara spatiu intre 
#     if i % 5 == 0:
#         suma = suma + i
# print(suma) 

# PT TEMA:
# n! = n * (n - 1) * (n - 2)          # n!= n factorial/ de cautat formula
# chr() functie care ne converteste nr in caractere, de vazut tabelul ASCII
       

# 3 cuvinte noi, keyword in python:

# pass     = omite urm linii de cod dupa el
# continue = omite iteratia curenta
# break    = opreste iteratia

# sa cautam cel mai mic multiplu comun la 2 nr:

# 15 % 3 = 0    # 15 impartit cu rest este 0
# 30 % 3 = 0
# 15; 30

# for i in range(2, 15):
#     if 15 % i == 0 and 30 % i == 0: # vrem sa-l afisam pe primul
#         print(i)
#         break    # ca sa-l afiseze numai pe 3


# for i in range(10):
#     if i % 2 == 0:
#         continue    
#     print(i)






