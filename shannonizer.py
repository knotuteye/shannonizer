import math


def greeter():
    print("\n\t -- S H A N N O N I Z E R -- \n")
    print("This program calculates the amount of information of an event or series of events in bits based on the probability")


def selfInformation(prob):
    return math.log2(1/prob)


def entropy(prob_list):
    info_list = []
    for prob in prob_list:
        info_list.append(prob*math.log2(1/prob))
    sum = 0
    for info in info_list:
        sum += info


if __name__ == "__main__":
    greeter()
