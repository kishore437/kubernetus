
# file handling

a = open('hi.txt', 'w')
b = a.write('this is day28')
print(b)
a.close()

a = open('hi.txt', 'r')
b = a.read()
print(b)
a.close()




