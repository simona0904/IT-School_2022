
names = ['Vlad', 'Dana', 'Sergiu', 'Cleopatra']

# vreau sa vad numele si lungimea lui
# vreau sa le vad ordonate alfabetic
# vreau sa vad de cate ori apare litera a in toata lista

for name in names:
    print(name, len(name))


names.sort() 
for name in names:
    print(name) 
      

total_aparitii_a = 0

for name in names:
    aparitii_a = name.count('a')
    total_aparitii_a += aparitii_a
print(total_aparitii_a)   



   
