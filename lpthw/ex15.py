from sys import argv

script, filename = argv

t = open(filename)

print(f"Here's your file {filename}:")
print(t.read())
t.close()

print("Type the filename again:")
f = input("> ")

tn = open(f)

print(tn.read())
tn.close()
