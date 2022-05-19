# 3. Scrie un program care citeste de la tastatura doua numere, a si b.
# Daca a > b sa se diferenta suma lor.
# Daca a == b sa se afiseze a la puterea b
# Altfel sa se afiseze suma lor.

a = int(input("Nr.a : "))
b = int(input("Nr.b : "))

if a > b: 
    print(a - b)
elif a == b:
    print(a ** b)   
else:
    print(a + b)     