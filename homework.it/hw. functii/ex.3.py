# 3. Scrieti o functie care returneaza daca unu nr. (reprezentan un an) este
# considerat an bisect.

def is_bisect(an):
    if an % 4 == 0:
        return True
    else:
        return False 

is_bisect(2012)   
is_bisect(2021) 

print(is_bisect(2012)) 
print(is_bisect(2021))