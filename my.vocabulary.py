# IF...ELSE CONDITIONAL STATEMENTS:

# keywords= cuvinte rezervate in python, nu le putem folosi ca nume de variabile.

# Sintaxa if...else:

# if conditie:
#     bloc de cod
#     bloc de cod
# else:
#     cod
#     cod
#     cod    

# if True:                          # daca ce este dupa if este true at se executa True
#     print("Conditie adevarata.")  # bloc de cod inseamna tot ce are indentare
# else:
#     print("Conditie falsa.")      # daca nu, se executa else.
# 




# # sintaxa WHILE:
# 
# while conditie:
    # cod
    # cod
    # cod

# while True:
#     print("hello")    # se executa la infinit atat timp cat conditia este True

# n = 0
# while n < 3:
#     print("hello")
#     n = n + 1         # pt a opri bucla while trebuie incrementata, ii dam un reper la care sa se opresca.

# 1. n=0    
# 2. n=1
# 3. n=2
# 4. n=3 - nu se executa pt ca conditia nu mai este adevarata


# sintaxa FOR LOOP:

# for variable in iterable:
# for i in range(10):        # 10 este nr de iteratii:



# sep=""     =se pune pt a lipi 2 lucruri fara spatiu intre ele (variabile, stringuri, etc.)
 
# end= " "   =ne ajuta sa scriem pe aceeasi linie inspre dreapta cu spatiu: A B C...

# random.randit() =genereaza nr aleatorii intr-un anumit interval. (import random la inceputul programului)

# chr()    = functie care transforma cifrele in litere.

# pass     = omite urm linii de cod dupa el
# continue = omite iteratia curenta
# break    = opreste iteratia

# abs() = absolut, transforma orice nr negativ in nr pozitiv.

# sort() = aranjeaza cifrele dintr-o lista in ordine crescatoare.

# del = sterge un obict din memorie  

# len() = returneaza lungimea unei structuri de date

# del = sterge un obict din memorie



# RANGE:

# # range() sintaxa:

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

# for i in range(0, 11, 2):               # adica de la 0 la 10 din 2 in 2 ( 2 de la final reprezinta din cat in cat)
#     print("i =", i)                     # 0 = start   11 = stop    2 = step 
                                          # step is how much we add to i every time.



# WHILE:


# while loops:

# With the while loop we can execute a set of statements as long as a condition is true.

# Ex: 
# 
# i = 1                 #rez: 1
# while i < 6:                 #2
#     print(i)                 #3
#     i += 1                   #4
                             #5

# Note: remember to increment i, or else the loop will continue forever.


# The break Statement:

# With the break statement we can stop the loop even if the while condition is true:

# i = 1                rez: 1
# while i < 6:              2
#     print(i)              3 
#     if i == 3:
#         break
#     i += 1


# The continue Statement:

# With the continue statement we can stop the current iteration, and continue with the next:

# i = 0                  rez: 1
# while i < 6:                2
#     i += 1                  3
#     if i == 3:              4
#         continue            5
#     print(i)                6

# while permite executia unui bloc de cod atat timp cat este adevarata.

# sintaxa: 
# 
# while conditie:
    # cod
    # cod
    # cod



# FUNCTII:
 
 # DEFINIREA:

# cuvantul cheie def : def
# numele functiei : wellcome_message
# paranteze rotunde : ()
# corpul functiei : print("Bine ai venit

 
# # Functii cu parametrii:


# def wellcome_message(name, lucky_number):
#     print("welcome back", name, "!")        
#     print("Lucky number is", lucky_number)  

# wellcome_message("Simona", 19) 
# wellcome_message("Mihai", 33)  
# # wellcome_message("George")   

# o functie trebuie sa aiba atatea valori cati parametrii functionali intre() 


 
# Functii care retuneaza ceva:



# functia randint ->

# def produs(a, b):
#     # product of two numbers.
#     res = 0
#     for i in range(b):
#         res += a
#     return res 
#     #print("Done function")      # tot ce este sub return nu va mai executat

# print(produs(3, 4))  
# # print(12)   

# x_result = produs(30, 23)     # salvam rezultatul intr-o variabila
# print(x_result + 2)




# COLECTII DE DATE - LISTE:


# 1.Structuri de date built in:

# list = colectie ordonata de obiecte       IMUTABIL NU
# tuple = colectie ordonata de obiecte      IMUTABIL DA
# str = colectie ordonata de caractere      IMUTABIL DA
# set = colectie ordonata de obiecte unice  IMUTABIL NU
# dict = dictionar, colectie neordonata de obiecte
 #        accesibila printr-o cheie.        IMUTABIL NU

# IMUTABIL = structuri de date care nu isi pot schimba forma, 
#            care nu pot suferi modificari.

# toate structurile de date built in sunt iterabile

# declarare
call_id = []

# alocare:
call_id = [1, 2, 3, 4]

#accesare:
call_id[0] -> 1

# modificare element:
call_id[1] = 4

# stergerea unui element dintr-o lista:

del call_id[2] -> [1, 2, 4]



# List sliceing = ne permite sa obt o llista noua plecand de la o lista initiala 
#                 dar ne permite sa facem taieri din lista.

# primele 3 elemente din lista:

top_three_users = user_id[:3]      # de la index 0 la 3 fara al include pe 3

print("user_id", user_id)
print("top_three_users", top_three_users)

# ultimul element:

last_element = user_id[-1]
print(last_element)

# interval:

print(user_id[1:4])


# list copy:

colours1 = ["red", "blue"]
colours2 = colours1.copy()

print(colours1, colours2)

colours2[0] = "modified"



# OPERATIUNI PE LISTE:

# list.append(x) = adaugare element nou,lista se mareste cu 1 element.
# list.remove(x) =  eliminare element 
# list.count(x)  = numarul de aparitii al unui element
# list.reverse() = reversul listei!!! opereaza pe lista
# min(list)     =  Minimul listei
# max(list)     = Maximul listei: nr cel mai mare din lista, la litere se ia in 
#               considerare ordinea alfabetica.
# len(list)



# TUPLE: sunt niste liste imutabile, nu se pot modifica.

countries = ('Romania', 'France', 'Germany', 'Lituania') # tuple se scrie intre () separate prin virgula
default_numbers = 1, 2, 3                           # sau pur si simplu cu virgula
empty_tuple = ()                                    # tuple gol se scrie asa
empty_tuple2 = tuple()                              # sau asa 


# OPERATIUNI PE TUPLE:

# putem aplica 2 metode la tuple:

# .count = numara de cate ori apare in tuple elentul respectiv

# countries.count('Romania')

# .index = returneaza prima aparitie de la stanga la dreapta a elementului cautat.

# countries.index("Romania")

# TUPLE UNPACKING:

red_color = ('red', "#FF0000")
light_green_color = ('light_green', '#21F503')

colors = [red_color, light_green_color]

red_color_code = red_color[0]
red_color_code = red_color[1]

print(red_color_code)

# sau varinta mai simpla cu tuple unpacking:

r_c_n, r_c_c = red_color
print(r_c_c)



# SETURI:


# SET  (este mutabil, putem schimba elementele din lista)
# setul contine doar elemente unice
# duplicatele vor fi eliminate
# folosim paranteze {}

words = {'the', 'is', 'now', 'then'}
empty_set = set()                      # set din lista

numbers = [1, 2, 3, 1, 2, 22]   # convertim o lista intr-un set, duplicatele vor fi eliminate
unique_numbers = set(numbers)   # unique_numbers = 1, 2, 3, 22

# OPERATIUNI PE SET:

# .add = adaugam elemente noi intr-un set existent.

# .update elimina duplicatele din doua seturi combinate de lista cu set, stentie altereaza setul curent.

# .intersection selecteaza doar elementele comune din cele 2 seturi fara al altera setul curent,
# va returna un set nou

# .difference  va returna inversul operatiunii adica toate elementele in afara de cele care apar in
# cele 2 seturi


# DICTIONARE:


# ca sa definim dictionarele folosim {}
# keyword dict
# folosim key ca sa accesam valorile, nu index ca la celelalte colectii de date
# pe post de key putem folosi nr sau stringuri

empty_dict = {}
empty_dict1 = dict()


# OPERATIUNI PE DICTIONARE:


# cum extragem lista cheilor?

print(user_info.keys())

# putem itera:

for key in user_info.keys():
    print(key)

# lista valorilor; values = obiect de tip view

for v in user_info.values():
    print(v)

# putem itera:

for v in u_i_values1():
    print(v)

# lista chei- valori:
# 
# china_years = {
    2010: "Dragonului",
    2011: "Cocosului",
    2012: "Iepurelui",
}

key_values_years = china_years.items()
print(key_values_years)     # dict_items([(2010, 'Dragonului'), (2011, 'Cocosului'), (2012, 'Iepurelui')])

# putem itera:

for kv in china_years.items():
    print("Anul", kv[0], "a fost anul", kv[1])

# sau asa:    asa este corect

for k, v in china_years.items():
    print("Anul", k, "a fost anul", v)


# cum sortam dictionarul dupa chei:

user_info = {
    "name": "Alex",
    "age": 28,
    "email": "alex.radu@email.com",
    "gender": "M"
}

sorted_user_info = sorted(user_info)

print("Sortat dupa chei")

for k, v in sorted(user_info.items()):
    print(k, v)


# sortare dupa valori   

print("Sortat dupa valori") 


