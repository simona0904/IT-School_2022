
# join ne permite sa concatenam doua str folosind anumite elemente de alipire


list1 = ["a", "b", "c"]

# vrem sa obtinem a>b>c
# sau a_b_c

# join:   putem adauga
# nu putem folosi "\" backslash pt ca este escape caracter in python

new_str =">".join(list1)   # sintaxa: ">".join()
print(new_str)             # a>b>c

# vreau sa obt. c-b-a

new_str2 = "-".join(reversed(list1))
print(new_str2)
