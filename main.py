from tkinter import filedialog
from tkinter import *
from pygame import mixer
import tkinter.font as font
import os
from PIL import ImageTk, Image

root = Tk()
root.title('Music Player')
root.geometry("500x300")

mixer.init()

songlist = Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('arial',15),height=12,width=47,selectbackground="gray",selectforeground="black")
songlist.grid(columnspan=9)
songlist.pack()

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
        mixer.music.load(os.path.join(root.directory, current_song))
        mixer.music.play()
    else:
        mixer.music.unpause()
        paused = False

def pause_music():
    global pause
    mixer.music.pause()
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
        songlist.select_clear(0, END)
        songlist.selection_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(label='Select Folder', command=load_music)
menubar.add_cascade(label='File', menu=file_menu)

play_btn_img = ImageTk.PhotoImage(Image.open("play.png"))
pause_btn_img = ImageTk.PhotoImage(Image.open("pause.png"))
next_btn_img = ImageTk.PhotoImage(Image.open("next.png"))
back_btn_img = ImageTk.PhotoImage(Image.open("back.png"))

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image=play_btn_img, borderwidth=0, command=play_music)
pause_btn = Button(control_frame, image=pause_btn_img, borderwidth=0, command=pause_music)
next_btn = Button(control_frame, image=next_btn_img, borderwidth=0, command=next_music)
back_btn = Button(control_frame, image=back_btn_img, borderwidth=0, command=prev_music)

play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
back_btn.grid(row=0, column=0, padx=7, pady=10)

root.mainloop()