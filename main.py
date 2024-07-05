from tkinter import filedialog
from tkinter import *
import pygame
from pygame import mixer
import os

root = Tk()
root.title('Music Player')
root.geometry("500x300")
pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

songs = []
current_song = ""
paused = False
def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        songlist.insert("end", song)

    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]

def play_music():
    global current_song, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False
def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True
def next_music():
    global current_song, paused
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

def prev_music():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass


songlist = Listbox(root, bg="black", fg="white", height=15, width=75)
songlist.pack()

add = Menu(menubar, tearoff=False)
menubar.add_cascade(label='Add Music', menu=add)
add.add_command(label='Select Folder', command=load_music)

play_btn_img = PhotoImage(file="play.png")
pause_btn_img = PhotoImage(file="pause.png")
next_btn_img = PhotoImage(file="next.png")
back_btn_img = PhotoImage(file="back.png")

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image=play_btn_img, borderwidth=0, command=play_music)
pause_btn = Button(control_frame, image=pause_btn_img, borderwidth=0, command=pause_music)
next_btn = Button(control_frame, image=next_btn_img, borderwidth=0, command=next_music)
back_btn = Button(control_frame, image=back_btn_img, borderwidth=0, command=prev_music)

play_btn.grid(row=0, column=1, padx= 7, pady= 10)
pause_btn.grid(row=0, column=2, padx= 7, pady= 10)
next_btn.grid(row=0, column=3, padx= 7, pady= 10)
back_btn.grid(row=0, column=0, padx= 7, pady= 10)

root.mainloop()