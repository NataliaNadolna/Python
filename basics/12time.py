import time

timer = time.time()
timer2 = time.time()

while True:
    if time.time()-timer > 2:
        print("2 sek")
        timer = time.time()

    if time.time()-timer2 > 5:
        break
