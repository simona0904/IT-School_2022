
# OPERATIUNI PE SET 2:


magic_numbers = {1, 44, 3, 23, 2, 33}  # {1, 2, 3, 33, 23, 44}
print(magic_numbers)

magic_numbers.update([1, 2, 3, 99])
print(magic_numbers)                   # {1, 2, 3, 33, 99, 23, 44}

# .update elimina duplicatele din doua seturi combinate de lista cu set, stentie altereaza setul curent.

# .intersection selecteaza doar elementele comune din cele 2 seturi fara al altera setul curent,
# va returna un set nou

# .difference  va returna inversul operatiunii adica toate elementele in afara de cele care apar in
# cele 2 seturi