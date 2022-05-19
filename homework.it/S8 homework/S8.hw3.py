# 3. Scrieti o functie care primeste doua liste ca parametri. Listele contin numere intregi.
# Fct. returneaza o singura lista formata din inmultirea dupa cum urmeaza: primul elem. din prima 
# lista X primul elem. din a 2-a lista .... etc.
# [1, 2, 3]
# [3, 4, 6]
# => [3, 8, 18]

def multiply_numbers(numbers_a, numbers_b):
    multiplyed_numbers = []
    for number_a, number_b in zip(numbers_a, numbers_b):
        multiplyed_numbers.append(number_a * number_b)
    return multiplyed_numbers
    

result = multiply_numbers([2, 5, 8,], [5, 3, 6,])    
print(result)  
 



    