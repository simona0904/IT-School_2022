# 1. Scrieti o functie care verifica daca unu nr este par.
# Daca este par returneaza True, altfel False. Functia are un singur argument.



def is_even(number):
    if number % 2 == 0:         
        return True
    else:
        return False

print(is_even(2)) 
print(is_even(6))
print(is_even(7)) 

# or shorter:

def is_even_shorter(number):
    return number % 2 == 0    

print(is_even_shorter(2)) 
print(is_even_shorter(6))
print(is_even_shorter(7)) 


