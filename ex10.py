tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# Escape Sequences
print("ASCII bell (BELL): [\a]")
print("Horizontal tab (TAB): [\t]")
print("ASCII vertical tab (VT): [\v]")

"""
while True:
    for i in ["/","-","|","\\","|"]:
        print("%s\r" % i, )
"""

# Study Drills
triple_single_quotes = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print(triple_single_quotes)

print("Combining %r with double-quote and single-quote escapes and print them out: ")
print("tabby_cat: raw = [%r], str = [%s]" % (tabby_cat, tabby_cat))
print("persian_cat: raw = [%r], str = [%s]" % (persian_cat, persian_cat))
print("backslash_cat: raw = [%r], str = [%s]" % (backslash_cat, backslash_cat))
print("fat_cat: raw = [%r], str = [%s]" % (fat_cat, fat_cat))
