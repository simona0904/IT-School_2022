# 2. Scrie un program care citeste de la tastatura un numar 
# natural, reprezentand raza unui cerc, si afiseaza perimetrul
# cercului insotit de mesajul "Perimetru cercului = <valoare>".
# Daca numarul citit este mai mare decat 100 se va calcula si aria
# cercului. Aceasta se va afisa insotita de mesajul "Aria cercului = <valoare>".


raza = int(input("Raza este: "))
perimetru = 2 * 3.14 * raza
aria = 3.14 * (raza ** 2)

if raza <= 100:
    print("Perimetrul cercului =", perimetru)
    print("Aria cercului = " + str(aria)) 
else:
    print("End")     