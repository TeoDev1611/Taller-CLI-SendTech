import sys
from colorama import Fore,init

init(autoreset=True)

def Validate(num1,num2):
    if num1 == None:
        print(Fore.RED+"ERROR: NON TYPE PROVIDE")
        sys.exit(1)
    elif num2 == None:
        print(Fore.RED+"ERROR: NON TYPE PROVIDE")
        sys.exit(1)
    else:
        pass

def sum(a,b):
    return a + b

def substract(a,b):
    return a - b

def multi(a,b):
    return a * b

def divide(a,b):
    return a / b
