from sys import argv

script, last = argv
last = int(last)

def mywhileloop(last):
    i = 0
    numbers = []

    while i < last:
        print("At the top i is %d" % i)
        numbers.append(i)

        i += 1
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers: ")

    for num in numbers:
        print(num)

mywhileloop(last)
