# python standard library:
# TEXT PROCESSING SERVICES in jos gasim module ( in docs.python.org)

import time

# help si dir

# aflam cat dureaza sa executam un program:

timestamp = time.time()

print(timestamp)

start = time.time()

for i in range(10000):
    print(10 ** i)

stop = time.time()

print("Started at", start)
print("Stoped at", stop)
print("Duration:", stop - start)


