from sys import argv

script, last, step = argv
last = int(last)
step = int(step)

def mywhileloop(last = 10, step = 1):
    i = 0
    numbers = []

    while i < last:
        print("At the top i is %d" % i)
        numbers.append(i)

        i += step
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers: ")

    for num in numbers:
        print(num)

mywhileloop(last, step)
