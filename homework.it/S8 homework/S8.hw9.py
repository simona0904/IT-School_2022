
# 9) Make a function for printing the first 5 longest strings in a list ; (len("test"))

fruits = ["apple", "lemons", "kiwi", "oranges", "strawberries", "pears", "bananas"]


fruits_lenght = []
for fruit in fruits:
    fruits_lenght.append(len(fruit))     # aflam lungimea fiecarui cuvant din lista, practic atribuim
                                         # o cifra fiecarui cuvant.

print(fruits)                         # ['apple', 'lemons', 'kiwi', 'oranges', 'strawberries', 'pears', 'bananas']
print(fruits_lenght)                  # [   5,        6,       4,       7,           12,           5,        7]


combined_lists = list(zip(fruits, fruits_lenght)) # cream o variabila noua in care le combinam intr-un tuple
print(combined_lists)  # [('apple', 5), ('lemons', 6), ('kiwi', 4), ('oranges', 7), ('strawberries', 12), ('pears', 5), ('bananas', 7)]
print(combined_lists[0])  # printam primul element din lista
print(combined_lists[0][1])  # apoi de la primul tuple al doilea element care reprez. lungimea cuvantului
combined_lists.sort(key = lambda e: e[1], reverse = True) # lista combinata am sortat-o dupa al doilea element 
print(combined_lists)                                     # din tuple si am inversat

for combination in combined_lists[0:5]:   # pt lista tuple combinata print de la 1 : 5 
    print(combination[0])                 # apoi print la primul element din lista 






