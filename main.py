import threading
'''Progreama1'''
def print_square(num):
    #print("square: {}".format(num * num))
    print("Square: "+ str(num * num))

def print_cube(num):
    print("Cube: " + str(num * num * num))
    t1 = threading.Thread(target=print_cube, args=(10,))
    t2 = threading.Thread(target=print_square, args=(10,))
    print("Hello world")

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("By world")
print_cube(1)
'''Programa2'''
