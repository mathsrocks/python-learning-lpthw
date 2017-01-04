from sys import argv

script, start, last, step = argv
start = int(start)
last = int(last)
step = int(step)

def myforloop(start = 0, last = 10, step = 1):
    numbers = []

    for i in range(start, last, step):
        print("At the top i is %d" % i)
        numbers.append(i)

#        i += step
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers: ")

    for num in numbers:
        print(num)

myforloop(start, last, step)
