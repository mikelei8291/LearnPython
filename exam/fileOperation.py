f = open("testfile.txt", "w+")
print(f.name, f.mode, f.closed)
f.write("Test str1\nTest str2\nTest str3")
for line in f:
	print(line, end="")
f.seek(0,0)
flist = f.readlines()
print(flist)
count = len(flist)
print(count)
f.seek(0,0)
lnum = -1
for lnum,line in enumerate(f):
	lnum += 1
print(lnum)
f.close()