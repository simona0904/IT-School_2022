from datetime import datetime

# 7. Print how much hours passed from this year.

first_day = datetime(2022, 1, 1)
delta = datetime.now() - first_day

# print(delta)
print(delta.total_seconds() / 60)