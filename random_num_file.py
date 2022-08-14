from random import randint
s1 = ''
s2 = ''
for i in range(0, 2000000000):
    s1 += ' ' + str(randint(101, 200))
for n in range(0, 2000000000):
    s2 += ' ' + str(randint(1, 100))
openfile = open('num_file.txt','x')
openfile.write(s1)
openfile.write(s2)
openfile.close()
