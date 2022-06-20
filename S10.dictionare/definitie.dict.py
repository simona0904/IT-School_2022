
# ca sa definim dictionarele folosim {}
# keyword dict
# folosim key ca sa accesam valorile, nu index ca la celelalte colectii de date
# pe post de key putem folosi nr sau stringuri

empty_dict = {}
empty_dict1 = dict()

print(empty_dict)                    # {}
print(type(empty_dict))              # <class 'dict'>

user_info = {
    "name": "Alex",
    "age": 28,
    "email": "alex.radu@email.com",
    "gender": "M"
}

dir2 = {                         # dictionar care contine o cheie/valoare si un alt dictionar care contine o cheie si o lista
    "key1": 1,                   # asta se numeste structura de date imbricata sau 'nested'
    "key2": {
        "key1": 1,
        "key2": ['elem1', 'elem2']
    }
}

# OPERATIUNI PE DICTIONARE:

# accesare informatii din dictionar:
# "name" este key (cheia)
# ce este dupa : este valoarea accesata

print("Nume:", user_info["name"])
print("Varsta:", user_info["age"])

# sau asa:

print(user_info.get("name", "negasit"))

# modificare:

print("---------")
user_info["name"] = "George"

print("Nume:", user_info["name"])
print("Varsta:", user_info["age"])

# adaugare element nou, o noua pereche key/valoare:

print(empty_dict)

empty_dict["ro"] = "Buna ziua!"

print(empty_dict)

empty_dict["en"] = "Good afternoon!"

print(empty_dict["en"])

# stergere key: (cu tot cu valoare)

del user_info['email']

print(user_info)

# CRUD = create read update delete (operatiuni pe care le vrem de la o structura de date)

