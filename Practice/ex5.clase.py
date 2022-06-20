#  cerinta: vreau sa reprezinti numarul casei si numele proprietarului
#  uite si o lista de case de pe strada mea
#  23, Sana'gonda Milelie
#  32, Wilhelm Scream
#  24, Marius
#  25 Silviu Macedonia
#  27 Sighet WWW
#  26 Lender al 4lea
# alta cerinta: vreau ca programul sa reprezinte nume, email si telefon pentru clientii mei
# i extra points bonus: afiseaza numele proprietarilor de la case de la prima cerinta
# descrescator in functie de numarul casei

class House:

    def __init__(self, owner_name: str, number: int) -> None:
        self.owner_name = owner_name
        self.number = number


neighbours = [
    House("Sana_gonda_Milelie", 23 ),
    House("Wilhelm Scream", 32),
    House("Marius", 24),
    House("Siviu Macedonia", 25),
    House("Sighet www", 27),
    House("Lender al 4 lea", 26),
]

neighbours.sort(key=lambda house: house.number, reverse=True)

for house in neighbours:
    print(house.owner_name)






