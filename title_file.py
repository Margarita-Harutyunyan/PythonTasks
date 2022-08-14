#make a new file where the first character of every word in a given file is upper case 
def title_file():
    openfile = open('givenfile.txt','r')
    readfile = openfile.read()
    new = readfile.title()
    newfile = open('titlefile.txt', 'x')
    newfile.write(new)
    openfile.close()
    newfile.close()
