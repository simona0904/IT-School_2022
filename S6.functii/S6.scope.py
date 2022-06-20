
def reverse(n):
    rev = 0
    while n != 0:
        c = n % 10    # rest   c = cifra curenta
        n = n // 10   # catul
        rev = rev * 10 + c

    return rev

# ex de variabila care se gaseste in mai multe locuri in py: path
# ex de aici este rev
# exista 2 tipuri de scope: global si local

# global scope:
  
rev = 20
PI =3.14  # nu le putem modifica valorile
age = 20


# local scope = orice este indentat 
 
def bar ():
    age = age + 10
    print(age1)

# scopul local are prioritate scopului global
# din scopul local avem acees la variabilele din scopul global dar nu invers.

PI =3.14

def p_cerc(r):
    return 2 * PI * r

def a_cerc(r):
    return PI * r ** 2  

print(p_cerc(10))     
   

