# scrieti o functie (get_week_days) care returneaza un dictionar ce contine zilele saptamanii, mapate de forma "luni": 1
# functia trebuie sa primeasca un param. optional de tip bool (work_week) cu val default False;
# Daca work_week este adevarat atunci se va returna un dict. ce contine doar zilele lucratoare.

week_days = {
    "luni": 1,
    "marti": 2,
    "miercuri": 3,
    "joi": 4,
    "vineri": 5,
    "sambata": 6,
    "duminica": 7
}

def get_week_days(week_days, work_week):
   work_week == False
   for day in week_days:
    if day >= 6:
        return week_days

     

 