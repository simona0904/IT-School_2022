# 3. Scrieti un program care citeste de la tastatura un nr natural "n", 
# si afiseaza suma primelor n numere multiple de 5 si 3.



n = int(input("n= "))
suma = 0

for i in range(3, n, 3):                     # pas="" se pune ca sa nu apara spatiu intre 
    if i % 5 == 0:
        suma = suma + i
print(suma) 

