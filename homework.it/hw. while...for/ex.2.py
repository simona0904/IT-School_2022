# 2. Scrieti un program care afiseaza numerele impare in intervalul [0, 1000]



for i in range(1, 1001, 2):
    print(i)

# sau:

for i in range(1001):
    if i % 2 == 1:          # % modulo aflam care sunt nr pare sau impare
        print(i) 
 
    
