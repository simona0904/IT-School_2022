# input()

# age = input("What is your age?\n ") #sau \n in loc de enter 
# print(age)     # putem scrie in terminal

# ENTER in terminal ne da posibiliatea sa raspundem 
# type CASTING  schimbarea tipului de date...int in str sau invers

# age = input("Varsta ta:")
# int_age = int(age)   # cast la int => 19
# print(int_age / 2)

# f_age = float(age)    # cast la float
# str_age = str(age)    # cast la str


# sau alta metoda pt conversie:

# print(type(age))  => "str"
# age = int(age) 

# age = input("Vrsta" )
# age = int(age)
# print("Jumatate din varsta ta:")
# print(age / 2)

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

# if True:          # daca ce este dupa if este true at se executa True
#     print("Conditie adevarata.")  # bloc de cod inseamna tot ce are indentare
# else:
#     print("Conditie falsa.")    

# if 7 == 9:
#     print("Adevarat")
# else:
#     print("fals")    

# varsta = int(input("Varsta: "))
# if varsta >= 18:
#     print("major")
# else:
#     print("Minor")    

# numar = int(input("Nr: "))   # sau numar = int(numar) pe alt rand

# if numar % 2 == 0:   # modulo ne spune daca e nr par sau impar, 0 fiind par.
#     print("Nr.par ")
# else:
#     print("Nr.impar ")   
# 
# sa se afiseze nr acceptat daca nr din input este in intervalul inchis [10 50]

# numar = int(input(" n= "))

# if numar >= 10 and numar <= 50:
#     # True and True pt 12 pt ca toate conditiile au dat true
#     print("nr acceptat")
# else:
#     print("nr neacceptat")    

# folosim or daca nr de la input se afla in afara intervalului:
# if numar < 10 or numar > 50:
#     print("nr acceptat")
# else:
#     print("nr neacceptat")
# 
# ELIF:
# 
#  Scrie un program care citeste de la tastatura doua numere, a si b.
# Daca a > b se verfica daca b este mai mic decat diferenta dintre a si b, daca da,
# afiseaza "b este mai mic decat jumatatea lui a". Daca diferenta este egala cu b atunci
# afiseaza "b este jumatatea lui a".
# Daca b > a se afiseaza "b mai mare decat a"  


# a = int(input("a= "))
# b = int(input("b= "))

# if a > b:
#     print("a mai mare decat b")
#     if b < b - a:
#         print("b este mai mic decat jumatatea lui a")
# elif a == b:
#     print("numerele sunt egale")
# else:
#     print("b mai mare decat a")   
# 
# putem folosi if fara else:
# 
# ora = 9
# m = 12
# if ora < 15:
#     print("Buna dimineata.") 
# if ora > 9:
#     print("Mai dormi") 
# elif ora > 9 and ora <= 17:
#     print("Buna ziua")     





 








