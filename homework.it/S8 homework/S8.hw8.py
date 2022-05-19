# Make a function to remove all the element with a maximal value from a list; return a new list 
# (original list does not modify)

def remove_maximal_number(numbers):
    new_numbers = numbers.copy()                         # lista copiata
    maximal_number = max(numbers)                        # aflam nr cu val cea mai mare
    maximal_number_count = numbers.count(maximal_number) # aflam daca sunt mai multe nr cu acea val maxima
    for i in range(maximal_number_count):                # iteram          
        new_numbers.remove(maximal_number)               # eliminam nr cele mai mari
    return new_numbers                                   # returnam lista noua (fara nr cele mai mari)


numbers = [5, 10, 80, 80]
print(remove_maximal_number(numbers))   
print(numbers)


    


          


