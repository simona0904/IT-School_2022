# 2. Utilizati functia de la pct 1 pentru a afisa toate numerele impare in intervalul
# [0, 50] si in intervalul [2000, 2100].


def is_even(number):
    if number % 2 == 0:         
        return True
    else:
        return False

for i in range(51):
    if not is_even(i):
        print(i, end=" ") 
for k in range(1999, 2101): 
    if not is_even(k): 
        print(k, end =" ") 
        