#reading strings from a file
#open the file for reading data

f = open('currexchange.txt','r')

#read strings from the file
print('The file contents are : ')
str = f.read()
print(str)

#closing the file
f.close()
