

words = {'test', 'tester', 'dev', 'analist', 'manager', 1}
empty_set = set()      # ca sa nu fie confundat cu dictionary se scrie asa ()

# print(type(words))      # <class 'set'>
# print(words)            # {1, 'test', 'analist', 'dev', 'manager', 'tester'}
# print(words[0])         # nu putema ccesa elementele prin index pt ca ele sunt amestecate in memori


# de cele mai multe ori vom folosi seturile ca seturi goale unde sa putem adauga elemente

# putem itera setul cu un for: dar apar random in terminal deci nu se prea foloseste

# for i in words:
#     print(i)

numbers = [1, 22, 33, 4, 5, 2, 1, 33, 4, 55, 56, 5, 4,]
print("lista intreaga, lungime", len(numbers))       # lista intreaga, lungime 13
print(numbers)                                       # [1, 22, 33, 4, 5, 2, 1, 33, 4, 55, 56, 5, 4]



unique_numbers = set(numbers)

print("Set unic, lungime", len(unique_numbers))     # Set unic, lungime 8  
print(unique_numbers)                       # {1, 33, 2, 4, 5, 22, 55, 56} s-au eliminat 5 duplicate                          



   