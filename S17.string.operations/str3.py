
# OPERATII PE SIRURI DE CARACTERE:

# capitalize: face prima data toate literele mici si apoi o face mare pe prima
text = "simona CORDOS"

calatori = [
    "Otavă Bogdan",
    "Greta Mihaela Geabelea",
    "Iustin Gabriel Manciu",
    "Corina Lungu",
    "Melissa Madalina Haj Abdo",
    "Gabriel Guțui",
    "George Valeanu",
    "Andreea-Simona Telegeanu",
    "Ionuț Alin Preda",
    "Arthur Timbalariu",
    "Cristian Laurentiu Șandor",
    "Alex Raul Bonat-Mihalca",
    "Artsanyo Dennis Kachi",
    "Sergiu Mihai Predel",
    "Marian-Gabriel Tohaneanu-Iatan",
    "Irina Florentina Barbu",
    "Cordos Simona",
]

print(text.capitalize())          # Hello john


print(text.title())               # face litera mare prima litera care apare dupa limitator (. , etc)
print(text.zfill(10))             # zfill umple spatiile date cu zerouri, (10 caractere in total cu tot cu text)

# endswith:

print(text.endswith("DOS"))       #  returneaza True daca un str se termina intr-un sub-str

# startswith:

print(text.startswith("s"))    # returneaza True daca un str incepe intr-un sub-str
# print(text.lower())          # transforma in litere mici
# print(text.upper())          # transforma in litere mari
# print(text.replace())        # inlocuieste un str cu un sub-str
# print(text.count())          # ne afiseaza nr de aparitii al unui str

# daca un sub-str face parte dintr-un str:

print("simona" in text)           # True

# daca un nume are in componenta a anumita litera...o de ex:

# for i in calatori:
#     if o in i:
#         print(i)







