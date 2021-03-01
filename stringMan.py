import time

i = 0
while i < 3:
    print(i, " ", time.time().real)
    time.sleep(2.0)
    i += 1

