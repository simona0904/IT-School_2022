
# ora si data curenta?
from datetime import datetime

current_dt = datetime.now()

# ziua curenta
print(current_dt.day)

# luna curenta
print(current_dt.month)

# anul curent
print(current_dt.year)

# ora curenta
print("Ora:", current_dt.hour)

# minute si secunde
print("Minut:", current_dt.minute)
print("Secunda:", current_dt.second)

# output:
# 16
# 6
# 2022
# Ora: 12
# Minut: 9
# Secunda: 57