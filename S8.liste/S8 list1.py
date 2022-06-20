
leader_board = ['Alex', 'George', 'Ionut'] 
#                 0         1        2           
#  sau: leader_board = list()

print(type(leader_board))    # class list
print(leader_board)

print('-' * 30)

print("Nr. castigatori:", len(leader_board))   # 3

print("Locul 1:", leader_board[0])    # Alex
print("Locul 1:", leader_board[2])    # Ionut

# accesarea ultimului element din lista, nestiind ce lungime are lista
# len() = returneaza lungimea unei structuri de date

print("Locul 1:", leader_board[0])

# print("Ultimul loc:", leader_board[len(leader_board)])
print("Ultimul loc:", leader_board[-1])       # mai scurt

# modificare elemente:

print("Locul 2 initial:", leader_board[1])  # daca vrem sa schimbam numele:
leader_board[1] = "Andrei"
print("Locul 2 dupa modificare:", leader_board[1])

# stergerea unui element dintr-o lista:
# del = sterge un obict din memorie

del leader_board[-1]
print("Dupa stergerea ultimului element")
print(leader_board)    # ['Alex, "Andrei"]

print('-' * 30)
print("Castigatorii sunt:")

for name in leader_board:
    print(name)