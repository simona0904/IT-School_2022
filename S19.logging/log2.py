
import logging
import sys
import pathlib
from datetime import datetime

# AICI FACEM UN ROOT LOGGER CUSTOMIZAT:

# configurare root logger pt a scrie in fisier: (folosim functia basic Config)

# fisierele se creaza in locul din care se executa scriptul
# caile absolute pornesc cu numele partitiei(C, D...)
# default fisierele se dechid in mode append
# filemode:
# r = read
# a = append
# w = write

root = pathlib.Path(__file__).parent
logs_path = root.joinpath("logs")
log_filename = datetime.now().strftime("%d%m%Y_%H%M%S.log")
log_abs_path = logs_path.joinpath(log_filename)

try:
    # creem folderul de loguri
    logs_path.mkdir(exist_ok=True)
except OSError as err:
    print(err)


logging.basicConfig(filename=log_abs_path, level=logging.INFO, filemode="w")

logging.info("Starting...")
logging.debug(f"Running on Python: {sys.version}")
logging.info("Job done. Exiting...")


print(logs_path)    # calea absoluta catre folderul logs este log_path

# print(f"File name: {__file__}")

# print(root)        # c:\Users\simon\OneDrive\Desktop\itschool\S19.logging\log2.py
# print(type(root))  # <class 'pathlib.WindowsPath'>

# print(root)          # c:\Users\simon\OneDrive\Desktop\itschool\S19.logging


# cu filename putem emite logurile intr-un fisier
# ca sa putem da acest nume de fisier trebuie sa-l accesam din consola astfel:
# pwd = print working directory = in ce director te afli => (C:\Users\simon\OneDrive\Desktop\itschool)
# ls = afiseaza fisierele din director.(toate fisierele din it school in acest caz)
# dir =  face exact acelasi lucru ca si ls

# Ca sa te referi la un fisier in programare exista cai absolute si cai relative.
# caile relative incep cu / in linus si cu numele partitiei (C) in windows.