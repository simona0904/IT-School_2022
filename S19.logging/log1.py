import logging

# log-urile contin informatii din timpul rularii unui soft.
# daca scriem un soft care ruleaza si vrem sa il testam, sa vedem cu reactioneaza, avem nevoie de log-uri.
# la orice program ar trebui sa facem log-uri.

# logurile sunt de mai multe feluri:
# 1. pe consola (similar cu print-ul doar ca putin mai aranjate, formatate)
# 2. scrise intr-un fisier
# 3. scrise intr-un server extern
# 4. date catre un event logger din sistemul de operare.


# CRITICAL
# ERROR
# WARNING
# INFO
# DEBUG

# cand se seteaza un filtru vedem doar erorile de deasupra celei setate.( la error o sa vedem doar error si critical etc...)
# pe langa nivelul de gravitate putem vedea si info extra: timestamp, ora, data, ziua cand s-a produs evenimentul si mesajul.
# extra poti pune numele functiei unde s-a emis logul, linia unde s-a emis, variabile de context (debugger)

# Ca sa emitem loguri avem nevoie sa configuram modulul logging cu urm:
# 1. formatul mesajului (formatul intra in handler)
# 2. handler (handler intra in logger)
# 3. looger ( in logger pot intra mai multi handleri)


# setam nivelul de gravitate:


logging.root.level = logging.DEBUG    # ca sa ne arate toate mesajele, pt ca afiseaza tot ce e 
                                      # mai mare sau egal cu debug
logging.critical("critical test")
logging.error("error test")
logging.warning("warning test")
logging.info("info test")
logging.debug("debug test")


# Decizia de a seta acest log la DEBUG o putem face cu un command line argument:

# scriem in consola:
# ex: ai un executabil cat --verbose (in interior se seteaza nivelul debug si astfel vom avea mai multe mesaje emise in consola
# ca sa integeti cat mai bine codul tau.

# Modulul logging urmeaza un patern care se numeste singleton
# singleton = are grija sa returneze mereu acelasi obiect (se creaza un sigur obiect in memorie si mereu ti-l da pe acelasi).
