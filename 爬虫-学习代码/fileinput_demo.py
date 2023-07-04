import fileinput
fileobj = fileinput.input('urls.txt')
#print(fileobj.readline().rstrip())
for line in fileobj:
          line = line.rstrip()
          if line != "":
                    print(fileobj.lineno(),':',line)
          else:
                    print(fileobj.filename)
