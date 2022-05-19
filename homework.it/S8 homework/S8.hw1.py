# S8 homework1

# Scrieti o functie care returneaza reversul unei liste. Lista primita ca parametru nu 
# trebuie modificata.



def reverse_numbers(numbers):
    new_numbers = list(numbers)
    new_numbers.reverse()

    return new_numbers
        
numbers = [3, 5, 11, 6, 19, 10]

numere_inversate = reverse_numbers(numbers)
print(numbers)  
print(numere_inversate) 
    





    