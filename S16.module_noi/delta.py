from datetime import datetime

b_day = datetime(1984, 4, 9)
delta = datetime.now() - b_day

print(delta)                   # 13945 days from my birth
print(delta.total_seconds())   # 1204916440.947756 seconds from my birth
print(delta.days)

# output:
# 13947 days, 12:12:15.676861
# 1205064735.676861
# 13947