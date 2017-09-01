from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("(RETURN/CTRL-C)?")

print("Opening the file...")
f = open(filename, 'w')

print("Truncating the file. Goodbye!")
f.truncate()

print("Now I'm going to ask you for three lines.")

l1 = input("Line 1: ")
l2 = input("Line 2: ")
l3 = input("Line 3: ")

print("I'm going to write these lines to the file.")

f.write(l1 + "\n")
f.write(l2 + "\n")
f.write(l3 + "\n")

print("And finally, we close it.")
f.close()
