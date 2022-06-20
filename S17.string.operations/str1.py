
# stringurile sunt o insiruire de caractere, orice text simplu scris intre "" (ghilimele).
# sunt imutabile, adica o data ce le-am creat nu putem sa operam pe ele.
# orice operatiune facem cu str rezulta un string nou, nu se poate modifica str creat.
# str fiind o insiruire de caractere pot fi privite ca si o lista si putem sa aplicam o parte din
# operatiunile care le aplicam si pe liste.


full_name = "Simona Cordos"

print(full_name[0])
print(full_name[-1])

first_name = "Simona"
last_name = "Cordos"

# concatenarea:

my_full_name = first_name + " " + last_name
print(my_full_name)

# multiplicarea:

name_10x = my_full_name * 10

print(type(name_10x))

# sliceing:

first_four = full_name[:4]    # printeaza primele 4 litere din str
last_two = full_name[-2]      # printeaza penultima litera (-1 este ultima, apoi -2 penultima etc)

print(first_four)           # Simo
print(last_two)             # o



