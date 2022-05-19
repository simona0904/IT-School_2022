# 4. Scrieti o functie care returneaza volumul unui cub in litri. Aceasta va primi
# un singur agument reprezentand muchia cubului in metri.

# 5. Scrieti o functie care returneaza volumul unui cilintru in litri,
# Aceasta va primi doua argumente reprezentand inaltimea si raza bazei in metri.

# 6. Scrie o functie care converteste litrii in metri cubi.

# 7. Foloseste functiile de la pct. 4-6 pentru a calcula cate cuburi cu muchia de 18 metri
# sunt necesare pentru a umple un cilindru cu raza bazei de 20 m si inaltimea de 55 m.
# - Printeaza volumul cubului in metri cubi #### Volumul cubului: 20 m^3
# - Printeaza volumul cilindrului in metri cubi.
# - Printeaza rezultatul de la pct. 7
# - Toate valorile printate vor fi insotite de mesaje descriptive.


# 4: vol. cub => L*l*h 
#    vl. cilindru => V = Pi R patrat * h
#    muchia = diagonala : radical din 3

def cube_volume(edge):
    # calculate cube volume in liters
    # 1 m3 = 1000 l
    return edge ** 3 * 1000


# 6: Conversie litri in m3:  l = m3 / 1000

# liters = int(input("Liters you want to convert: "))

# def is_liter(m3):
#     res = m3 / 1000
#     m3 = 1000
#     return res
    
        
# is_liter(100) 
# print(is_liter(100)) 
 
# facut in clasa:
#   
def convert_to_m3(liters):
    #    convert liters in m3
    return liters / 1000

print("Volumul cubului:", convert_to_m3(cube_volume(18)), m3)

# ierarhie de apelare:

# 1.cube_volume
# 2.convert_volume
# 3.print



       