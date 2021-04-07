from _thread import start_new_thread
from time import sleep

threadID = 1
waiting = 2

def factorial(n):
    global threadID
    rc = 0
    if n < 1:
        print("{} : {} *".format('\nThread', threadID))
        threadID += 1
        rc = 1
    else:
        returnNumer = n * factorial(n - 1 )
        print("{}!= {}  > ".format(str(n), str(returnNumer)))
    return rc
start_new_thread(factorial, (5,))
start_new_thread(factorial, (4, ))
print("Waiting for theads to return...")
sleep(waiting)