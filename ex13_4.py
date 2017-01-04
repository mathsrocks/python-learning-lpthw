from sys import argv

script, first, second, third, fourth = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", fourth)

input_var1 = input("Input variable 1: ")
input_var2 = input("Input variable 2: ")

print("Input variables: %r, %r" % (input_var1, input_var2))
