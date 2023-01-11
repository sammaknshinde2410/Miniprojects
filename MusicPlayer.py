#Building a music player
#required libraries Tkinter and pygame
#pip install pygame (cmd command to install a module)


from tkinter import *
#from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    '''created a class for Music Player Controls'''
    def __init__(self,window):
        window.geometry("320x100");
        window.title('MY MUSIC PLAYER');
        window.resizable(0,0);
        Load = Button(window, text= 'Load', width = 10, font=('Times',10), command=self.load)
        Play = Button(window,text ='Play', width=10,font=('Times',10),command=self.play)
        Pause = Button(window,text ='Pause', width=10,font=('Times',10),command=self.pause)
        Stop =Button(window,text ='Stop', width=10,font=('Times',10),command=self.stop)

        Load.place(x=0, y=20);
        Play.place(x=110,y=20);
        Pause.place(x=220,y=20);
        Stop.place(x=110,y=60);

        self.music_file = False
        self.playing_state = False

    def load(self):
        '''Adding load method to our music player class'''
        self.music_file = filedialog.askopenfilename()

    def play(self):
        '''Adding play method to our music player class'''
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):
        '''Adding pause method to our music player class'''
        if not self.playing_state:
            mixer.music.pause();
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        '''adding srop method'''
        mixer.music.stop()



#creating tkinter class object
root = Tk()

#passing the tkinter class object as argument to MusicPlayer
app = MusicPlayer(root)

#calling a loop to keep the app window running
root.mainloop()
