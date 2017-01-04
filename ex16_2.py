from sys import argv

script, filename = argv

print("A script named: %r is run." %script)

txt = open(filename)

print(txt.read())

txt.close()
