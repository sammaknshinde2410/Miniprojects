# a python program to create a text file to store individual characters
#creating a file to stroe characters
#open the file for writing data

f = open("currexchange.txt", 'w')

#enter characters from keyboard
str = input('Enter the text: ')

#write the string into file
f.write(str)


#closing the file
f.close()
