# create a file

#file=open("file.txt", 'w')
#file.write("It's an another line ! ")
#file.close()

#file=open("file.txt", 'a')
#file.write("we add another line after appnend !")
#file.close()

file=open("file.txt", 'r')
for i in file.readline():
    print(i, end="")
    file.close()

