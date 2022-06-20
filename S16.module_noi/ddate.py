from datetime import datetime

# formatare ora
print(datetime.now().strftime("%H:%M:%S"))    # 18:44:23

# formatare data:
print(datetime.now().strftime("%d/%b/%y"))    # 14/Jun/22

# 04/09/1984

b_day = datetime(1984, 4, 9)
print(b_day.strftime("%m/%d/%Y"))

# output:
# 12:11:39
# 16/Jun/22
# 04/09/1984


