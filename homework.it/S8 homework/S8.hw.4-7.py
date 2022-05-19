# 4) Create a mixed (string and int) list with 10 elements
# 5) Print first and last element
# 6) Replace second element with 144
# 7) Print the index of element with value 144

mixed_list = ['apple', 20, "bread", 'kiwi', 15, 8, 'milk', 50, 'lemons', 25]

print(mixed_list[0])                # printam primul element din lista
print(mixed_list[-1])               # printam ultimul element din lista
del mixed_list[1]                   # eliminam al doilea element din lista
print(mixed_list)
mixed_list.insert(1, 144)           # inlocuim al doilea element cu 144
print(mixed_list)
print(mixed_list.index(144))        # printam indexul lui 144

