# Importing Modules
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar, Scale
from pygame import mixer

mixer.init()

win = Tk()

font_tup = ('consolas', 17)

win.title('Music Player')
win.resizable(False, False)
win.geometry('240x50')
win.config(bg='white')

mixer.music.set_volume(1)

progress = 0

toggle_state = True

def open():
    filename = filedialog.askopenfilename()
    if filename == '':
        return
    global song_lenght
    song_lenght = mixer.Sound(filename).get_length()
    mixer.music.load(filename)
    mixer.music.play()
    global toggle_state
    toggle_state = True

def toggle_state():
    if toggle_state == True:
        mixer.music.pause()
        toggle_state = False
    else:
        mixer.music.unpause()
        toggle_state = True

def replay():
    mixer.music.set_pos(0)

def mute():
    global init_vol
    init_vol = mixer.music.get_volume()
    mixer.music.set_volume(0)

def unmute():
    mixer.music.set_volume(init_vol)

open_button = Button(win, text='🔍', command=open, width=3, font=font_tup)
open_button.pack(anchor=S, side=LEFT)

toggle_button = Button(win, text='⏯', command=toggle_state, width=3, font=font_tup)
toggle_button.pack(anchor=S, side=LEFT)

mute_button = Button(win, text='🔇', command=mute, width=3, font=font_tup)
mute_button.pack(anchor=S, side=LEFT)

unmute_button = Button(win, text='🔊', command=unmute, width=3, font=font_tup)
unmute_button.pack(anchor=S, side=LEFT)

replay_button = Button(win, text='⟳', command=replay, width=3, font=font_tup)
replay_button.pack(anchor=S, side=LEFT)


win.mainloop()