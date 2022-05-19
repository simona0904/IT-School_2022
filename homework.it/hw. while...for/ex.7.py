# 8. Scrieti un program de tip joc "ghiceste numarul".
#     Cerinte: 
#     1. Programul genereaza un numar aleator in intervalul [1, 99].
#     2. Intr-o bucla conditionata de gasirea numarului cautat:
#         - se citeste de la tastatura un numar
#         - se compara cu numarul cautat
#         - daca numarul introdus este mai mic decat numarul cautat se afiseaza +
#         - daca este mai mic se afiseaza -
#     3. Dupa ce numarul este ghicit se afiseaza un mesaj de felicitare si numarul cautat.

#     EX: 
#     Incepe jocul!
#     Introduceti un numar intre 1 si 99.
#     3
#     +
#     6
#     +
#     20
#     +
#     60
#     -
#     50
#     +
#     56
#     -
#     Felicitari!
#     Ai ghicit numarul: 56



import random

generated_number = random.randint(1, 100)
print(generated_number)                     # random.randit() genereaza nr aleatorii intr-un anumit interval


print("Welcome to Guess a number game!")
print("You have to choose a number between 1 and 99:")
number = int(input("Number is: "))

while number != generated_number:
    if number < generated_number:
        print("+")
    elif number > generated_number:
        print("-") 
    number = int(input("Number is: ")) 
print("Congratulations! You guessed the correct number.")   

   
