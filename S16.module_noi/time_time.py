import time

# timestamp - secunde trecute de la 01.01.1970 00:00:00 UTC

print(time.time())

b_day = time.strptime("04/09/1984", "%m/%d/%Y")
wday = {
    0: "luni",
    1: "marti",
    2: "miercuri",
    3: "joi",
    4: "vineri",
    5: "sambata",
    6: "duminica"
}
print(wday[b_day.tm_wday])  # ziua sapt in care ne-am nascut
print(time.mktime(b_day))   # time stamp pt ziua npastra de nastere

b_day_ts = time.mktime(b_day)

# output:
# 1655370773.5850992
# luni
# 450306000.0

