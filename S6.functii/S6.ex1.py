# Scrie un program care citeste de la tastatura un nr. natural
# si verifica daca acesta este palindrom. 111 121 292 2992 33533
# sa facem o functie care returneaza True daca un nr este palidrom.
# citim de la tastatura un nr.
# apelam fct si afisam.

# 178 citit de dr la st ar fi 871   178!= 871
# 121 == 121
# 178 == 871 Flse

# 178 extragem pe 8 si ramane:
# 8
# 17 din 17 extragem pe 7 si ramane 1:
# 7
# 1
# ultima cifra o aflam cu % impartirea cu rest
# 178 % 10 = 8
#  8 * 10 + 7
# = 87
# 87 * 10 + 1
# =871

# functie care vede nr in oglinda:
# 871   871 / 10 = 87.10 ignoram ce e dupa virgula
# 87     87 / 10 = 8.7 adica 8
# 8       8 / 10 = 0
# 0
# rev = 1
# rev = 17 
# rev = 178 

def reverse(n):              # functie care face reverse la un nr. n = nr de la tastatura
    rev = 0                  # reverse are valoare initiala 0.
    while n != 0:            # while numar tastatura nu este egal cu 0
        c = n % 10           # rest   c = cifra curenta
        n = n // 10          # catul ( // impartire cu rest, dispare ce e dupa virgula)
        rev = rev * 10 + c   # 0 * 10 + cifra curenta
    return rev

def palindrom(n):
    """Check if palindrom"""
    if n == reverse(n):
        return True
    else:
        return False

n = int(input("Introduceti un numar: "))

if palindrom(n):
    print("Numarul este palindrom")
else:
    print("Numarul nu este palindrom")

            
    
# print(reverse(871))  # => 178 
print(reverse(n)) 





