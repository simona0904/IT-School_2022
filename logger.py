
# Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
# # sa scriem 5 functii

# debug("Mesaj") -> [DEBUG] Mesaj
# info("Mesaj") -> [INFO] Mesaj
# warining("Mesaj") -> [WARNING] Mesaj
# error("Mesaj") -> [ERROR] Mesaj
# critical("Mesaj") -> [CRITICAL] Mesaj


def log(msg, level):
    print("[", level,"]", msg)

def debug(msg):
    log(msg, "DEBUG")

def info(msg):
    log(msg, "INFO")  

def warning(msg):
    log(msg, "WARNING") 

def error(msg):
    log(msg, "ERROR") 

def critical(msg):
    log(msg, "CRITICAL")     
    
             


log("Start script", "DEBUG")
log("Start script", "INFO")
log("Start script", "WARNING")
log("Start script", "ERROR")
log("Start script", "CRITICAL")

 


