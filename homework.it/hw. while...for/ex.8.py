 # 9. Sa se modifice programul de la pct. 8 astfel:
#     - modificam intervalul de generare la [1, 300]
#     - in loc de + - o sa afisam dupa cum urmeaza;
#     - cand numarul introdus este:
#         +/- 50 fata de numarul cautat: "Gheata"
#         +/- 40 fata de numarul cautat: "Frig"
#         +/- 30 fata de numarul cautat: "Rece"
#         +/- 20 fata de numarul cautat: "Caldut"
#         +/- 10 fata de numarul cautat: "Cald"
#         +/- 5 fata de numarul cautat: "Frige"
#         +/- 2 fata de numarul cautat: "Arde"

#     EX:
#     Incepe jocul!
#     Introduceti un numar intre 1 si 99.
#     50
#     Caldut
#     44
#     Caldut
#     60
#     Rece
#     34
#     Frige
#     33
#     Frige
#     31
#     Arde
#     Felicitari!
#     Ai ghicit numarul: 31



import random

generated_number = random.randint(1, 300) 
print(generated_number)                  


print("Start game!")
print("You have to choose a number between 1 and 300:")
number = int(input("Number is: "))

while number != generated_number:
    distanta = abs(generated_number - number)
    if distanta > 50:
        print("Gheata")
    elif distanta > 40:
        print("Frig")   
    elif distanta > 30:
        print("Rece")  
    elif distanta > 20:
        print("Caldut")    
    elif distanta > 10:
        print("Cald") 
    elif distanta > 5:
        print("Frige")  
    elif distanta < 2:
        print("Arde") 
    number = int(input("Number is: ")) 
print("Congratulations! You guessed the correct number:", generated_number) 

