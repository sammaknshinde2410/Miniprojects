#A Python Program for Currency Conversion,
'''This program is made with the most basic concepts of python for converting a particular country's currency into another.''' 
import sys
data = {}#created an empty dictionary for storing currency name and exchange rates into key-value format.
with open('currexchangedata.txt','r') as f:#selected a file to fetch data about currency conversion.
    x =input("Choose Conversion Option\n1)INR-Other\n2)Other-INR\n3)Other-Other\nEnter your choice : ")
    if x == '1':
        for lines in f:#created a loop to access every line.
            a = lines.split(' \t')#created a list of the above imported text file using .split() method.
            #print(a)
            data[a[0]] = a[1]#added the currency name as key and the value of 1INR in that currency as value in a dictionary.
        amount = int(input('Enter INR Amount to be converted into desired currency : '))
        print('Available options for the name of Currency you want to convert INR into :\n')
        [print(i ) for i in data]# Used list comprehension for printing the currency names.
        currency  = input('Please enter name of Currency : ')
        print('{} INR in {} ='.format(amount,currency),amount*float(data[currency]))
    elif x == '2':
        for lines in f:#created a loop to access every line.
            a = lines.split(' \t')#created a list of the above imported text file using .split() method.
            #print(a)
            data[a[0]] = a[2]#added the currency name as key and the value of 1 unit currency in INR as value in a dictionary.
        amount = int(input('Enter Amount to be converted into INR : '))
        print('Available options for the name of Currency you want convert into INR :\n')
        [print(i ) for i in data]# Used list comprehension for printing the currency names.
        currency  = input('Please enter name of Currency : ')
        print('{} {} in INR ='.format(amount,currency),amount*float(data[currency]))
        #we can also use the code in if block by just dividing the amount by the currency value
    elif x == '3':
        for lines in f:#created a loop to access every line.
            a = lines.split(' \t')#created a list of the above imported text file using .split() method.
            data[a[0]] = a[1]#added the currency name as key and the value of 1INR in that currency as value in a dictionary.
            data[a[0]] = a[2]#added the currency name as key and the value of 1 unit currency in INR as value in a dictionary.
        print('Available options for the name of Currency you want convert :\n')
        [print(i ) for i in data]# Used list comprehension for printing the currency names.
        curr1 = input('Enter the input currency : ')
        amount = int(input('Enter the Amount to be converted : '))
        halfcon = amount * float(data[curr1])
        #print(halfcon)
        curr2 = input('Enter name of the currency to be converted into : ')
        print(float(halfcon)/float(data[curr2]))
    else:
        sys.exit("Program Terminated!!!!PLEASE CHOOSE OPTION 1,2 OR 3..")
        
    
        
        
        
    

        
        


