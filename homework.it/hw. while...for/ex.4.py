# 4. Scrieti un program care citeste de la tastatura un nr natural "n", 
# si afiseaza n! (factorial). 6! = 1 * 2 * 3 * 4 * 5 * 6

# 5. Scrieti un program care afiseaza toate litere (capitale) ale 
# alfabetului englez, pe aceiasi linie despartite prin spatiu. 
# **A se vedea tablelul ASCII. chr(65) -> A



                                        # cautam tabelul ASCII si vedem ca literele capitale se afla in intervalul 65, 91.
for i in range(65, 91):                 # pt variabila i in range de la 65 la 91 (pt ca literele capitale sunt in acest interval)
    chr(i)                              # aplicam functia chr (functie care converteste nr in caractere) pt i
    print(chr(i), end=" ")              # printam chr(i) si end=" " care ne ajuta sa scriem pe aceeasi linie inspre dreapta cu spatiu
                                        # de data aceasta pt ca asta e cerinta.
                                    
   