
# definire clasa:
# naming rules: numele clasei trebuie sa inceapa cu litera mare:
# NumeDeClasa  => se mai numeste Caps Case

class Car:      # Car este o clasa
    pass

class AirplaneTicket:
    pass

print(Car)        # <class '__main__.Car'>
print(type(Car))  # <class 'type'> adica cand definim o clasa  cream un type nou


# instantiere
# automobil este un obiect!!!

automobil = Car()    # cand facem apelul aceasta se creaza un obiect nou care trebuie
                     # salvat intr-o variabila (automobil)
print(automobil)     # <__main__.Car object at...
print(type(automobil))  # <class '__main__.Car'>


print("automobil este Car")
print(isinstance(automobil, Car))   # True, face parte din clasa Car




