print("Type the filename:")
filename = input("> ")
print("Here's your file %r:" % filename)

txt = open(filename)

print(txt.read())

txt.close()
