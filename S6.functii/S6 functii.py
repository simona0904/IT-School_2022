# Parametrii cu valoare initiala:

def hello(name="Guest"):   #=""
#     # print welcome message.Default name is Guest.
    print("Hello and welcome", name)

hello()
hello("Simona")
    

# scriem o functie care primeste 2 parametrii si printeaza primele 10 nr si le printeaza
# 0===1===2=== etc. una sub alta.

def b_range(stop, sep, sep_c):    # stop reprez. nr la care vrem sa se opreasca
    for i in range(stop):         # sep reprez. separatorul pe care vrem sa-l folosim       
        print(i)                  # sep_c arata cate caractere folosim in operatie
        print("===")

b_range(10, None, None) 

# # folosim si alt semn in loc de ==

def b_range(stop, sep, sep_c):    #sep_c arata cate caractere folosim in operatie
    for i in range(stop):
        print(i)
        print(sep * 3)

b_range(10, "+", None) 

# # vrem sa aflam si lungimea separatorului:

def b_range(stop, sep, sep_c):    #sep_c arata cate caractere folosim in operatie
    for i in range(stop):
        print(i)
        print(sep * sep_c)

b_range(10, "*", 10)

# dar sa zicem ca se schimba functia cu un singur parametru (oricare dintre ele)

def b_range(stop, sep="+", sep_c=10):    #sep_c arata cate caractere folosim in operatie
    for i in range(stop):
        print(i, end="")                 # end="" apar toate pe aceeasi linie spre dreapta
        print(sep * sep_c)

# # b_range(12)
# # b_range(5)

b_range(5, "+", 20)
  # scurtam operatiunea:
b_range(5, sep_c=20)









