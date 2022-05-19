# 4. Scrie un program care citeste de la tastatura doua numere,
# si calculeaza a / b daca a > b sau b / a daca a <= b. Afiseaza 
# rezultatul.

a = int(input("Nr.a : ")) 
b = int(input("Nr.b : "))

if a > b:
    print(a / b)
elif a <= b:
    print(b / a)    
else:
    print("None")    