
# 2. Scrieti o functie care returneaza True daca lista primita ca param. este sortata,
# altfel returneaza False.

def are_numbers_sorted(numbers: list[int]):
    sorted_numbers = list(numbers)                   # lista copiata
    sorted_numbers.sort()                            # lista copiata sortata
    if numbers == sorted_numbers:
        return True
    else:
        return False    

print(are_numbers_sorted([15, 2, 45])) 
print(are_numbers_sorted([1, 2, 3]))
print(are_numbers_sorted([-15, -2, -45]))
print(are_numbers_sorted([-3, -2, -1]))

    

