'''
f = open('python链接mysqldemo.txt','w')
print(f.write('hello world!'))
print(f.write('i love python'))
f.close()
'''
f2 = open('test.txt','r')
print(f2.read(12))
print(f2.read(13))
f2.close()

f3 = open('test.txt','a+')
print(f3.read())
f3.seek(0)
print(f3.read())
f3.close()
