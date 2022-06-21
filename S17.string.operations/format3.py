first_name = "Mihai"
last_name = "Dinu"
age = 20

user = {
    "name": "Mihai",
}

print(f"Nume: {user['name']} | Varsta: {age:*^{30 -2}}") # ^ =  aliniere centrat, cu o lungime maxima de 30 - 2

# Output:
# Nume: Mihai | Varsta: *************20*************

# ^ = aliniere centrat
# intre {} punem numele variabilei pe care vrem sa o folosim
# la f strings putem executa cod intre {} (la .format nu se poate)