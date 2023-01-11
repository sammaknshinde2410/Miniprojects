#Python program to set an alarm

#Importing required libraries
from datetime import *
import time,pyttsx3,winsound
from threading import *
from tkinter import *


#simple alarm clock using GUI

root=Tk()
#creating a canvas
canvas=Canvas(root,width=500,height=400)
canvas.pack()
root.title("My Alarm")

#create labels
label1=Label(root,text="Set Hour:",font=('calibri',10,'bold'),bg="white").place(x=150,y=90)
label2=Label(root,text="Set minutes:",font=('calibri',10,'bold'),bg="white").place(x=150,y=120)
label3= Label(root,text="Alarm message:",font=('calibri',10,'bold'),bg="white").place(x=150,y=150)

#create entry boxes for the user to put input
hour=Entry(root)
canvas.create_window(310,100,window=hour)

minute=Entry(root)
canvas.create_window(310,130,window=minute)

msg=Entry(root)
canvas.create_window(310,160,window=msg)


def Threading():
    '''This function manages the button in the waiting period'''
    t1=Thread(target=alarm)
    t1.start()

def dismiss():
    winsound.PlaySound(None,winsound.SND_PURGE)
    audio.stop()
##    root.destroy()

def snooze():
    winsound.PlaySound(None,winsound.SND_PURGE)
    time.sleep(10)
    winsound.PlaySound('sound2.mp3',winsound.SND_ASYNC)
        
def alarm():
    '''This function pops up a diablog box for the user to set his/her alarm'''
    global audio
    #getting the input that the user has entered
    user_in1= hour.get()
    user_in2= minute.get()
    user_in3= msg.get()
    while True:
        now=datetime.now().strftime("%H:%M")
        if user_in1==now[:2] and user_in2==now[3:5]:
            print(user_in3)
            #text to speech when alarm goes off
            audio= pyttsx3.init()
            audio.say(f"It is {user_in1} {user_in2} Hours")
            audio.runAndWait()
            
            #play sound for given time, if no loop is given it will play according to the music filelength
            for i in range(5):
                winsound.PlaySound('classic.wav',winsound.SND_ASYNC)
                break
        else:
            time.sleep(10)
#creating a 'set alarm' button
button=Button(root,text="Set alarm",bg="white",command=Threading)
snooze=Button(root,text="Snooze",bg="white",command=snooze)
dismiss=Button(root,text="Dismiss",bg="white",command=dismiss)
canvas.create_window(250,200,window=button)
canvas.create_window(250,230,window=snooze)
canvas.create_window(250,260,window=dismiss)           
root.mainloop()






###Taking format input from user 
##form= int(input("Select 1 for: To enter in 12Hrs-Format\n\
##Select 2 for: To enter in 24Hrs-Format\n\
##>"))
##print(80*'=')
##
###Save date in day-month-year format
##date=datetime.now().strftime("%d %b %Y")
##
##class Alarm:
##    '''
##    A class to represent the working of an Alarm clock
##    ...
##    Attributes:
##        h: int
##           represents hour in alarm time
##        m: int
##            represents minutes in alarm time
##    ...
##    Methods:
##        h12(self):
##            sets alarm in 12Hrs format
##        h24(self):
##            sets alarm in 24Hrs format
##    '''
##    
##    def __init__(self,h,m):
##        '''Constructs all neccessary attributes for the alarm object.
##
##        Parameters:
##            h: int
##               represents hour in alarm time
##            m: int
##                represents minutes in alarm time
##        '''
##        self.h=h
##        self.m=m
##
##    def h12(self):
##        """Allows user to enter in 12Hrs format of clock"""
##        
##        #to check if current time is equal to time entered by user
##        while True:
##            now= datetime.now().strftime('%I:%M %p')
##            if now[:2]==("%02d"%h) and now[3:5]==("%02d"%m) and now[6:8]==am_pm:
##                print('----'+label+'----')
##                #text to speech when alarm goes off
##                audio= pyttsx3.init()
##                audio.say(f"It is {h} {m} {am_pm}")
##                audio.runAndWait()
##                
##                #play sound for given time, if no loop is given it will play according to the music filelength
##                for i in range(5):
##                    winsound.PlaySound(ring,winsound.SND_ASYNC)
##                    
##                #Dismissing or Snoozing the alarm    
##                while True:
##                    a=int(input('Press 1 for: Dismiss\nPress 2 for: Snooze 10secs\n>'))
##                    if a==1:
##                        winsound.PlaySound(None,winsound.SND_PURGE)
##                        sys.exit()
##
##                    elif a==2:
##                        winsound.PlaySound(None,winsound.SND_PURGE)
##                        time.sleep(10)
##                        winsound.PlaySound(ring,winsound.SND_ASYNC)
##                    else:
##                        print('Enter valid number!')
##            else:
##                time.sleep(10)
##
##    
##    def h24(self):
##        """Allows user to enter in 24Hrs format of clock"""
##
##        #to check if current time is equal to time entered by user
##        while True:
##            now= datetime.now().strftime('%H:%M')
##            if now[:2]==("%02d"%h) and now[3:5]==("%02d"%m): #and now[6:8]==am_pm:
##                print('----'+label+'----')
##                audio= pyttsx3.init()
##                audio.say(f"It is {h} {m} Hours")
##                audio.runAndWait()
##                for i in range(5):
##                    winsound.PlaySound(ring,winsound.SND_ASYNC)
##                
##                #Dismissing or Snoozing the alarm    
##                while True:
##                    a=int(input('Press 1 for: Dismiss\nPress 2 for: Snooze 10 secs\n>'))
##                    if a==1:
##                        winsound.PlaySound(None,winsound.SND_PURGE)
##                        sys.exit()
##
##                    elif a==2:
##                        winsound.PlaySound(None,winsound.SND_PURGE)
##                        time.sleep(10)
##                        winsound.PlaySound(ring,winsound.SND_ASYNC)
##                    else:
##                        print('Enter valid number!')
##            else:
##                time.sleep(10)
##
##def input_h12():
##    
##    #Taking time inputs from the user 
##    global h,m,am_pm,label,ring
##    h,m=[int(x) for x in input('\t\tSet hour and minutes with colon:').split(':')]
##    am_pm= input('\t\tAM or PM?:').upper()
##    print(80*'=')
##
##    #Taking display message from user
##    label=input('\t\tAdd alarm message:')
##    print(80*'=')
##
##    #Taking ringtone from user
##    ring= input('\t\tAvailable ringtones:\n\
##                              1>fast.wav\n\
##                              2>heavy.wav\n\
##                              3>classic.wav\n\
##                              4>waves.wav\n\
##                         Select ringtone:')
##    print(80*'=')
##    #Displaying the set alarm time and date, and saving the data in a file
##    f=open('alarm_file.txt','a')
##    x=(f'\t\tALARM SET AT {"%02d"%h}:{"%02d"%m} {am_pm} on {date}        ')
##    print(x)
##
##    #enter new line in file
##    f.write('\n')
##    f.write(x)
##    f.close()
##    print(80*'=')
##
##def input_h24():
##
##    #Taking time inputs from the user 
##    global h,m,label,ring
##    h,m=[int(x) for x in input('\t\tSet hour and minutes with colon:').split(':')]
##    print(80*'=')
##
##    #Taking display message from user
##    label=input('\t\tAdd alarm message:')
##    print(80*'=')
##
##    #Taking ringtone from user
##    ring= input('\t\tAvailable ringtones:\n\
##                          1>fast.wav\n\
##                          2>heavy.wav\n\
##                          3>classic.wav\n\
##                          4>waves.wav\n\
##                     Select ringtone:')
##    print(80*'=')
##    #Displaying the set alarm time and date, and saving the data in a file
##    f=open('alarm_file.txt','a')
##    x=(f'\t\tALARM SET AT {"%02d"%h}:{"%02d"%m} Hours on {date}        ')
##    print(x)
##
##    #enter new line in file
##    f.write('\n')
##    f.write(x)
##    f.close()
##    print(80*'=')
##
##
###Calling the function
##if form==1:
##    input_h12()
##    a=Alarm(h,m)
##    a.h12()
##elif form==2:
##    input_h24()
##    a=Alarm(h,m)
##    a.h24()
##else:
##    print('Invalid!!!')
##    

##def hour_24():
##
##    #create labels
##    label1=Label(root,text="SET HRS:").place(x=150,y=90)
##    label2=Label(root,text="SET MINS:").place(x=150,y=120)
##    
##    #create entry boxs for the user to put input
##    entry1=Entry(root)
##    canvas2.create_window(300,100,window=entry1)
##
##    entry2=Entry(root)
##    canvas2.create_window(300,130,window=entry2)
##    
##    user_in1= entry1.get()
##    user_in2= entry2.get()
##    while True:
##        now=datetime.now().strftime("%H:%M")
##        if user_in1==now[:2] and user_in2==now[3:5]:
##            print('wake up')
##            #text to speech when alarm goes off
##            audio= pyttsx3.init()
##            audio.say(f"It is {entry1} {entry2} Hours")
##            audio.runAndWait()
##                
##            #play sound for given time, if no loop is given it will play according to the music filelength
##            for i in range(5):
##                winsound.PlaySound(ring,winsound.SND_ASYNC)
##        else:
##            time.sleep(10)
##            
###creating a 'set alarm' button
##set_alarm=Button(root,text="set alarm",command=Threading)
##canvas2.create_window(250,200,window=set_alarm)
##
####button1= Button(root,text="12hour clock",command=hour_12).pack()
####button2= Button(root,text="24hour clock",command=hour_24).pack()
####root.mainloop()
##    
##
#####creating a 'set alarm' button
####set_alarm=Button(root,text="set alarm",command=Threading)
####canvas.create_window(250,200,window=set_alarm)
##
###creating menu bar
##menubar= Menu(root)
####clock_format= Menu(menubar,tearoff=0)
##menubar.add_command(label="12Hrs clock",command=hour_12)
##menubar.add_command(label="24Hrs clock",command=hour_24)
####menubar.add_cascade(label="Clock format",menu=clock_format)
##root.config(menu=menubar)
##root.mainloop()


#threading will control or manage any thread.
#here, after pressing 'set alarm' button, button remains pressed until alarm goes off
#threading will release the button after clicking once
##def Threading():
##    t1=Thread(target=hour_12)
##    t2=Thread(target=hour_24)
##    t1.start()
##    t2.start()
###actual alarm function
##def hour_12():
##    
##    user_in1= entry1.get()
##    user_in2= entry2.get()
##    user_in3= entry3.get()
##    while True:
##        now=datetime.now().strftime("%I:%M %p")
##        if user_in1==now[:2] and user_in2==now[3:5] and user_in3==now[6:8]:
##            print('wake up')
##            #text to speech when alarm goes off
##            audio= pyttsx3.init()
##            audio.say(f"It is {entry1} {entry2} {entry3}")
##            audio.runAndWait()
##                
##            #play sound for given time, if no loop is given it will play according to the music filelength
##            for i in range(5):
##                winsound.PlaySound(ring,winsound.SND_ASYNC)
##        else:
##            time.sleep(10)
##def hour_24():
##    
##    user_in1= entry1.get()
##    user_in2= entry2.get()
##    while True:
##        now=datetime.now().strftime("%H:%M")
##        if user_in1==now[:2] and user_in2==now[3:5]:
##            print('wake up')
##            #text to speech when alarm goes off
##            audio= pyttsx3.init()
##            audio.say(f"It is {entry1} {entry2} Hours")
##            audio.runAndWait()
##                
##            #play sound for given time, if no loop is given it will play according to the music filelength
##            for i in range(5):
##                winsound.PlaySound(ring,winsound.SND_ASYNC)
##        else:
##            time.sleep(10)


   
    
    
    
    



































##import time
##import winsound
##from datetime import *
##
##a=datetime.now()
####print(a)
##b=a.strftime("%x")
####print(b)
##now=a.strftime('%H:%M')
##
##date=input('enter date with /:')
##h,m=[int(x) for x in input('enter hr and min with colon:').split(':')]
##
##while True:
##    if date[:]==b[:] and now[:2]=="%02d"%h and now[3:5]=="%02d"%m:
##        winsound.PlaySound('classic.wav',winsound.SND_ASYNC)
##        break
    
##f=open('alarm_file.txt','w')
##a=input('enter text:')
##f.write(a)
##f.close()

##f=open('alarm_file.txt','r')
####print('YOUR ALARM MSG!: ')
####x=f.read()
##f.truncate()
####print(x)
##f.close()
##
##import pyttsx3
##x=pyttsx3.init()
##text='this is my first text to speech code'
##x.say(text)
##x.runAndWait()




##hour= int(input('Set hour: '))
##minutes= int(input('Set minutes: '))
##ampm= input("am or pm?: ")
###defining a function to convert 12Hrs format into 24Hrs format
##def convert_to_24(hour):
##    '''This function converts 12Hrs format to military time format'''
##
##    #1:00pm to 11:00pm in 24Hrs format
##    if hour>=1 and hour<12 and ampm=='pm':
##        hour+=12
##        print(f'{"%02d"%hour}:{"%02d"%minutes}')
##
##    #12:00pm will remain 12:00pm
##    elif hour==12 and ampm=='pm':
##        hour=hour
##        print(f'{"%02d"%hour}:{"%02d"%minutes}')
##        
##    #1:00am to 11:00am 
##    elif hour>=1 and hour<12 and ampm=='am':
##        hour=hour
##        print(f'{"%02d"%hour}:{"%02d"%minutes}')
##
##    #12:00am in 24Hrs format
##    elif hour==12 and ampm=='am':
##        hour-=hour
##        print(f'{"%02d"%hour}:{"%02d"%minutes}')
##
##    else:
##        print("Wrong input!!")
##
###calling the function
##convert_to_24(hour)


##
##










##def hr_min(hour,minutes):
##    if hour>=1 and hour<=9:
##        hour="%02d"%hour
##    if minutes>=0 and minutes<=9:
##        minutes="%02d"%minutes
##
##    print(f'{hour}:{minutes}')
##
##hr_min(hour,minutes)


##
##





#checking if last two elements of time are 'am' or not
#and if first two elements are '12' or not
##def convert(alarm_time):
##    '''This function will convert the civilian time into military time'''
##    
##    if alarm_time[-2:]=='am' and alarm_time[:2]=='12':
##        #if 'am', add '00' at the start (according to 24hrs format)
##        return '00'+ alarm_time[2:-2]
##    
##    elif alarm_time[-2:]=='pm' and alarm_time[:2]=='12':
##        #if 'pm', then keep as it is
##        return alarm_time[:-2]
##    
##    else:
##        #add 12 to the hours to convert to 24Hrs format
##        return str(int(alarm_time[:2])+12)+alarm_time[2:8]
##
##format_24=print(convert(alarm_time))


#

##
##class AmPm:
##    '''Converting 12Hrs format into military time format'''
##    #this is a constructor
##    def __init__(self,alarm_time):
##        self.alarm_time= alarm_time
##        
##    def pm(self):
##        '''This method converts 01:00pm to 11:00pm timings into 24Hrs format,
##           except 12:00pm,which will remain 1200Hrs in military time as well'''
##        
##        if alarm_time[:2]>='01' and alarm_time[:2]<'12' and ampm=='pm':
##            #add 12 to the hours to convert to 24Hrs format
##            print(str(int(alarm_time[:2])+12)+alarm_time[2:5])
##            
##        if alarm_time[:2]=='12' and ampm=='pm':
##            #keeping time as it is
##            print(alarm_time[:])
##        
##    def am(self):
##        '''This method converts 12:00am into 0000Hrs of military time'''
##        
##        if alarm_time[1:2]>='01' and alarm_time[:2]<'12' and ampm=='am':
##            print(alarm_time[:])
##            
##        if alarm_time[:2]=='12' and ampm=='am':
##            #changing 12:00am into 24Hrs format
##            print('00:'+alarm_time[3:])
##            
##        
##obj= AmPm(alarm_time)
##x= obj.pm()
##y= obj.am()
        
    

















###taking am or pm input from user
##am_pm= input("am or pm?: ")
##
###converting 12-hour format to 24-hour format, for after 12:00pm
##if am_pm==('pm' or'Pm' and hour!=12):
##    hour+=12
####print(f'Alarm set for {hour}:{minutes}{am_pm}')
##
###printing the time remaining for the alarm to turn on
##if minutes=='0' and hour=='12' and am_pm=='am':
##    print(f'Alarm set for {((hour-1)+12)-datetime.now().hour}hours and {60-datetime.now().minute}minutes from now')
##elif minutes==0 and hour=='12' and am_pm=='pm':
##    print(f'Alarm set for {((hour-1)+24)-datetime.now().hour}hours and {60-datetime.now().minute}minutes from now')
##else:
##    print(f'Alarm set for {(hour+12)-datetime.now().hour}hours and {minutes-datetime.now().minute}minutes from now')
  




##
###if user enters 1, do the below
##if form==1:     
##    
##    h,m=[int(x) for x in input("Set hour and minutes for alarm with colon: ").split(':')]
##    am_pm= input('AM or PM?: ').upper()
##    print(f'Alarm set at {h}:{m} {am_pm}')
##    
##    def hour_12(h,m):
##        '''This function rings an alarm for a 12Hrs-format clock'''
##
##        #to check if current time is equal to time entered by user
##        while True:
##            now= datetime.now().strftime('%I:%M %p')
##            if now[:2]==("%02d"%h) and now[3:5]==("%02d"%m) and now[6:8]==am_pm:
##                print('Wake up!!!')
##                for i in range(5):
##                    winsound.Beep(1000,10)
##                    time.sleep(0.1)
##                break
##            else:
##                time.sleep(10)
##
##    #calling the function hour_12()            
##    hour_12(h,m)
##
##
###if user enters 1, do the below
##elif form==2:
##
##    #taking input from user
##    h,m=[int(x) for x in input("Set hour and minutes for alarm with colon: ").split(':')]
##    am_pm= input('AM or PM?: ').upper()
##    print(f'Alarm set at {h}:{m} {am_pm}')
##    
##    def hour_24(h,m):
##        '''This function rings an alarm for 24Hrs-format clock'''
##        
##        #to check if current time is equal to time entered by user
##        while True:
##            now= datetime.now().strftime('%H:%M %p')
##            if now[:2]==("%02d"%h) and now[3:5]==("%02d"%m) and now[6:8]==am_pm:
##                print('Wake up!!!')
##                for i in range(5):
##                    winsound.Beep(1000,10)
##                    time.sleep(0.1)
##                break
##            else:
##                time.sleep(10)
##
##    #calling the function hour_24()
##    hour_24(h,m)
##
###if user enters neither 1 nor 2
##else:
##    print('invalid input!!')
