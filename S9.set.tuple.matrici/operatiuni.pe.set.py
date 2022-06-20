
# OPERATIUNI PE SET:

# .add = adaugam elemente noi intr-un set existent.

# user_name = set()

# n = 0
# # sa citim de la tastatura 3 nume

# while n < 3:
#     name = input()             # Simona  Ciprian  Simona
#     user_name.add(int(name))   # int(name) pt a putea citi nr de la tastatura
#     n += 1

# print(user_name)               # {'Simona', 'Ciprian'} a eliminat duplicatele
# print(user_name) # si dam nr la tastatura: 6,3,4 => le sorteaza in ordine crescatoare {3, 4, 6}



# .remove = elimina un element dintr-un set existent.


user_name = set()

user_name.add("Simona")
user_name.add("Ciprian")
user_name.add("Mihai")

user_name.remove('Simona')
print(user_name)            # {'Ciprian', 'Mihai'} numele Simona l-a eliminat

# putem verifica daca un element face parte dintr-un set astefel:

if "Simona" in user_name:
    user_name.remove("Simona")
print(user_name) 

# sau putem face reversul:

if "Simona" not in user_name:
    user_name.add("Simona")
print(user_name) 

# clear = elimina toate elementele dintr-un set.

user_name.clear(user_name)    # sterge toate elementele dintr-un set
print(user_name)