import time
from datetime import datetime

while True:
    # suspenda executia pt o secunda
    time.sleep(1)
    if datetime.now().second == 30:
        print("Jumatate de minut")

