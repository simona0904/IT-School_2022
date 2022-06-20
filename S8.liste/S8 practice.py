# list.append(x)

user_id = [33, 455, 3, 32, 34, 12, 90, 3, 234]
leader_board = ['Alex', 'George', 'Ionut'] 

print(user_id)

# Lungimea listei:
print("Lungimea listei:", len(user_id))

# Maximul listei: nr cel mai mare din lista
print("Maximul listei:", max(user_id))
print("Maximul listei:", max(leader_board)) 

# la str ia in considerare litera din alfabet cea mai mare

# Minimul listei:
print("Minimul listei:", min(user_id))

print("-" * 10)

# adaugare element nou - append:

user_id.append(100)
print(user_id)      # s-a adaugat 100 la lista si lista are 8 elemente
print("Lungimea listei:", len(user_id))

# eliminare element - remove:

user_id.remove(3)   # elimina prima val gasita in lista cu cifra 3
print("Dupa remove")
print(user_id)      # o sa primim eroare daca val cautata nu este prezenta

# verificare daca val face parte din lista:

# value_to_remove = int(input("remove value:"))

# if value_to_remove in user_id:
#     user_id.remove(value_to_remove)
# else:
#     print("valoarea nu este in lista") 

# print("END")  

# numarul de aparitii al unui element - count:

print("Elementul 33 apare de", user_id.count(33), "ori.")
print(user_id.count(33))

# insert la index:

user_id.insert(1, 0)   # la index 1 inseram 0
user_id.insert(-1, 0)  # adaugam 0 la penultimul element

print(user_id)

# gaseste indexul unei valori:

# sa introducem val x inainte de 32

print(user_id.index(32))
index_magic = user_id.index(32)
user_id.insert(index_magic + 1, "x")

print("Dupa index magic")
print(user_id)




