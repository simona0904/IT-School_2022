# 1. Scrieti un program care afiseaza numerele prime din intervalul [0 100].

numar_interval = int(input("Intervalul este: "))



for i in range(1, numar_interval):
    for n in range(2, numar_interval):
        if i % n == 0 and i != n:
            break
    else:
        print(i)

        

