# Python has two primitive loop commands:

#     while loops
#     for loops

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

# while True:
#     print("hello")    # se executa la infinit atat timp cat conditia este True

# n = 0               # n = 0 este numita si variabila de control cu care controlam executia si pe care trebuie sa avem grija sa o manipulam                                      
# while n < 3:        # cumva, sa o crestem, sa o scadem etc, din 2 in 2, sau din 3 in 3 etc.
#     print("hello")
#     n = n + 1


            # dam o val lui n de unde sa porneasca si vrem sa printam ceva de n ori dar mai < 3.
# 1. n=0    # prima data n va fi 0, pt ca are val 0 data initial, apoi ajunge in while unde indeplineste conditia True pt ca este mai mic   
# 2. n=1    # decat 3. Apoi n va deveni 1 (pt ca n = n + 1) si din nou este True pt este mai mic decat 3.
# 3. n=2    # Apoi n va deveni 2 (pt ca 1 initial + 1 = 2), la fel e True pt ca 2 < 3 si se executa bucla.
# 4. n=3    # Cand n devine 3 nu se mai  executa pt ca conditia nu mai este adevarata si bucla se opreste.



# n = int(input("n= "))
# # n = 3
# k = 1
# while k <= n:
#     print("*" * k, "+" *(n - k), sep="")            # sep="" se pune pt a lipi cele 2 k si n fara spatiu intre ele
#     k = k + 1 
# print("DONE")     

# avem la prima iteratie n = 3; k = 1   
#                        n = 3; k = 2
#                        n = 3; k = 3
#                        n = 3; k = 4   nu se mai executa pt ca bucla se inchide   
#  *++  k-stelute; n-k plusuri  


# IMPORTANT! 

# Intotdeauna cand ni se cere sa executam ceva de n ori, intotdeauna trebuie sa avem semnul < decat nr de executie:

# while n < 5:     va executa de 5 ori
# while n <= 5:    va executa de 6 ori pt ca numaratoarea incepe de la 0 si va include si 5-ul.



# EX: scrieti un program care afiseaza urm structura, unde n = 6, folosind instructiunea while.
# *
# **
# ***
# ****
# *****
# ****** 


 
# n = int(input("n = "))           # daca luam un nr de la tastatura, va printa cu baza egala cu acel nr.

# k = 1                            # pornim cu val variabilei k de la 1 pt ca prima data trebuie sa printam o stea.
# # n = 6                            # n va avea val 6 pt ca acolo trebuie sa ne oprim, baza are 6 stelute.                  
#                                  # k este nr iteratiei (a cata e), si ca afisam la prima iteratie o *, la a doua 2* si tot asa...
# while k <= n:                    # atat timp cat k este <= n printam * ca string si se inmulteste cu 6(str se pot inmulti cu nr.)
#     print("*" * k)               # "*" * k inseamna * ori nr de iteratii care se vor opri la 6.
#     k = k + 1                    # 1. (la prima iteratie avem) n = 6 ; k = 1: 1 este <= 6? DA at va printa o steluta inmultit cu 1 => *
                                 # 2. n = 6 ; k = 2    k <= n ?  DA at va printa o steluta inmultit cu 2
                                 # 3. n = 6 ; k = 3    k <= n ?  DA at va printa o steluta inmultit cu 3 si tot asa pana ajunge la 7 si se opreste
    

# Modificam programul anterior si completam cu +: *+++++
#                                                 **++++ 
#                                                 ***+++
#                                                 ****++
#                                                 *****+
#                                                 ******     
 
 
# k = 1
# n = 6

# while k <= 6:                               # atat timp cat nr iteratii(k) este < 6
#     print("*" * k,"+" *(n - k), sep=" ")    # printam * ori k (stelutele) si n-k sunt plusurile
#     k = k + 1


     
# k = 1
# n = 6

# while k <= 6:
#     print("Simona"," Cordos", sep="*")
#     k = k + 1   

