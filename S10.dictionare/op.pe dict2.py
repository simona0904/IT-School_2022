user_info = {
    "name": "Alex",
    "age": 28,
    "email": "alex.radu@email.com",
    "gender": "M"
}

# lista valorilor; values = obiect de tip view

for v in user_info.values():
    print(v)

# lista valorilor; values = obiect de tip view

u_i_values1 = user_info.values()
print(type(u_i_values1))          # <class 'dict_values'>
 
# putem itera:

for v in u_i_values1():
    print(v)
 
  