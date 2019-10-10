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
    return sum


if __name__ == "__main__":
    greeter()
    choice = input("\nEnter 1 for a single event or 2 for a series of events: ")
    if choice=="1":
        print("\nSingle Event")
        prob = input("Enter the probability of the event: ")
        info = str(selfInformation(float(prob))) + " bits"
        print("\nThe total information is ",info)
    if choice=="2":
        print("\nSeries of Events")
        n_events = input("\nEnter the number of events: ")
        print("\nEnter the probabilities consecutively")
        i = 0
        probabilities = []
        while i<n_events:
            probabilities.append(input())
        info = str(entropy(probabilities)) + " bits"