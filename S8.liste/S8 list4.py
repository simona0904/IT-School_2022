user_id = [33, 455, 3, 32, 34, 12, 90, 3, 234]

# reversul listei!!! opereaza pe lista

print("lista in stare initiala")
print(user_id)

user_id.reverse()    # lista este printatat invers

print("dupa reverse")
print(user_id)

# List sliceing = ne permite sa obt o llista noua plecand de la o lista initiala 
#                 dar ne permite sa facem taieri din lista.

# primele 3 elemente din lista:

top_three_users = user_id[:3]      # de la index 0 la 3 fara al include pe 3

print("user_id", user_id)
print("top_three_users", top_three_users)

# ultimul element:

last_element = user_id[-1]
print(last_element)

# interval:

print(user_id[1:4])


# list copy:

colours1 = ["red", "blue"]
colours2 = colours1.copy()

print(colours1, colours2)

colours2[0] = "modified"

print(colours1, colours2)