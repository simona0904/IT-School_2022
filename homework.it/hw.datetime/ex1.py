
from datetime import datetime

# 6. Make a function that print messages based on time.

def print_msg_based_on_time():
    current_hour = int(datetime.now().strftime("%H"))
    if current_hour <= 12:
        print("Good morning")
    elif current_hour > 12 and current_hour <= 18:
        print("Good afternoon")  
    elif current_hour > 18 and current_hour <= 21:
        print("Good evening.")  
    else:
        print("Good night")     

print_msg_based_on_time()