import math


def greeter():
    print("\n\t -- S H A N N O N I Z E R -- \n")
    print("This program calculates the amount of information of an event or series of events in bits based on the probability")
    choice = input("Enter 1 for single event or 2 for series of events: ")
    

def selfInformation(prob):
    return math.log2(1/prob)


if __name__ == "__main__":
    greeter()
