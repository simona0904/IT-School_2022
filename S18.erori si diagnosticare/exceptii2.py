"""
EXCEPTIILE sunt obiecte create atunci cand o functie intampina erori care ii impiedica functionalitatea
normala.

In momentul in care o exceptie este ridicata, executia normala a functiei este opritasi se revine
in punctul in care a fost chemata functia.

Daca acolo nu se trateaza exceptia, ea se propaga la urmatorul nivel pana cand ajunge in "main". Daca nici acolo
nu este tratata, executia se opreste si o eroare este afisata pe consola.

"""

Exceptii:

# ridicare exceptie:
raise Exception()


# prindere exceptie:
try:
    code
except Exception as err:
    print(err) 
else:
    # se executa cand codul din try nu are erori
    code
finally:
    # se executa chiar daca codul din try are erori
    # dar dupa ce se executa codul din except
    code         