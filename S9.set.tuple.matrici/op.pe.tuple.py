
banned_countries = ('Romania', 'Lituania', 'Novegia')
print(banned_countries[0])                  # Romania

list_banned = list(banned_countries)
print(list_banned)                          # ['Romania', 'Lituania', 'Novegia']

# daca vrem sa verificam daca lista tuple a fost alterata verificam daca are aceeasi lungime:

same_elements = True

if len(banned_countries) == len(list_banned):    # daca lungimea celor doua liste este egala
    for i in range(len(banned_countries)):         # aflam indexul
        if banned_countries[i] != list_banned[i]:  # daca banned_countries nu este egal cu list_banned
            same_elements == False                  # returneaza False
            break                                  # break ca sa oprim for-ul

print("Lista nemodificata:", same_elements)      # Lista nemodificata: True  




# putem aplica 2 metode la tuple:

# .count = numara de cate ori apare in tuple elentul respectiv

# countries.count('Romania')

# .index = returneaza prima aparitie de la stanga la dreapta a elementului cautat.

# countries.index("Romania")
