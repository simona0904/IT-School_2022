# sys interactioneaza strict cu interpretorul python

import sys

print(sys.maxsize)    # arata care este marimea maxima de biti folosita pt un str
print(sys.modules)

sys.exit(0)    # ajuta sa oprim un program

user_choice =int(input("Enter a number"))

if user_choice % 2 == 0:
    print("nr par")
    print("oprire program cu sys")
    sys.exit
else:
    print("nr impar")
    print("programul va continua")

print(datetime.now())    

