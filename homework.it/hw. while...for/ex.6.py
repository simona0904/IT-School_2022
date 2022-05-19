# 7. Scrieti un program care citeste doua nr de la tastatura si calculeaza produsul
# lor. A nu se utiliza operatorul de inmultire.



a = int(input("a= "))            # cerem un nr a de la tastatura =2
b = int(input("b= "))            # cerem un nr b de la tastatura =3
                                 # pt ca inmultirea se poate calcula ca si a+a+a...trebuie sa aplicam a +c eva de b ori
suma = 0                         # stabilim o valoare initiala 0 la care vom aduna a (de b ori)
for i in range(b):               # pt variabila i, pe care nu o folosim aici, doar face parte din sintaxa, in range(b) sau (3)
    suma += a                    # adunam suma initiala 0 la a si ne da 0 + 2 = 2, deci 2 de b ori este 2 de 3 ori.
print(suma)                      # printam suma si ne da egal cu 6.

