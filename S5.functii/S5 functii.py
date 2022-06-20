# DEFINIREA:

# cuvantul cheie def : def
# numele functiei : wellcome_message
# paranteze rotunde : ()
# corpul functiei : print("Bine ai venit")

# def wellcome_message():
#      print("Bine ai venit")

# # import random

# # n = random.randint(0, 100)


# def wellcome_message():
#     print("welcome back")        # daca functia nu face nimic se scrie pass
#     print("Lucky number is 20")  # daca trebuie sa modificam in print modificam doar nr

# wellcome_message()               # apel   
       

# DRY = do not repeat youself, a nu se repeta codul.

# cu ctrl f putem schimba numele functiei

# Functii cu parametrii:

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

# scrieti o functie care verifica daca un nr este par
# daca este par returneaza True, daca nu False. Functia are un singur argument.


# def is_even(n):          # check if nr is even
#     if n % 2 == 0:
#         return True
#     else:
#         return False  

# print(is_even(10)) 
# print(is_even(5)) 

# for i in range(101):
#     print(is_even(i))

#     # sau:

# for i in range(101):
#     if is_even(i):
#         print("**") 
#     else:
#         print("--") 

#     # sau:    

# for i in range(101):
#     if is_even(i):
#         print(i, "este par")  
#     else:
#         print(i, "este impar")

# 2. Utilizati functia de la pct 1 pentru a afisa toate numerele impare in intervalul
# [0, 50] si in intervalul [2000, 2100].

# def is_even(n):         
#     if n % 2 == 0:
#         return True
#     else:
#         return False   

 

# for i in range(51):
#      if not is_even(i):
#          print(i, end = " ")
# for i in range(1999, 2001): 
#     if not is_even(i): 
#         print(i, end = " ") 
# 
#       

# 3. Scrieti o functie care returneaza daca unu nr. (reprezentan un an) este
# considerat an bisect.


# def is_bisect(an):
#     if an % 4 == 0:
#         return True
#     else:
#         return False 

# is_bisect(2012)   
# is_bisect(2021) 

# print(is_bisect(2012)) 
# print(is_bisect(2021))      





