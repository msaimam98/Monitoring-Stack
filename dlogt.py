import threading


def printit11():
    threading.Timer(2, printit11).start()
    print(1.5)

printit11()


