
# cum sortam dictionarul dupa chei:

user_info = {
    "name": "Alex",
    "age": 28,
    "email": "alex.radu@email.com",
    "gender": "M"
}

sorted_user_info = sorted(user_info)

print("Sortat dupa chei")

for k, v in sorted(user_info.items()):
    print(k, v)


# sortare dupa valori   

print("Sortat dupa valori") 

