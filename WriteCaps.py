#Read through a file and print the contents of the file (line by line) all in upper case.
fname = input("enter the file name: ")
try:
    fhand = open(fname)
except:
	print("file not exist:", fname)
	exit()
for line in fhand:
    line = line.rstrip()
    print(line.upper())
