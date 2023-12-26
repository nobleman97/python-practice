from time import sleep;
import os;

def doSomething():
    for char in range(1, 4):
        print(f"this is run {char}")
        sleep(3)
        os.system('clear')
doSomething()