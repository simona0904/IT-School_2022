
user_info = {
    "name": "Alex",
    "age": 28,
    "email": "alex.radu@email.com",
    "gender": "M"
}

# lista chei- valori

china_years = {
    2010: "Dragonului",
    2011: "Cocosului",
    2012: "Iepurelui",
}

key_values_years = china_years.items()
print(key_values_years)     # dict_items([(2010, 'Dragonului'), (2011, 'Cocosului'), (2012, 'Iepurelui')])

# putem itera:

for kv in china_years.items():
    print("Anul", kv[0], "a fost anul", kv[1])

# sau asa:    asa este corect

for k, v in china_years.items():
    print("Anul", k, "a fost anul", v)