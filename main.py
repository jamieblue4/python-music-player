from tkinter import *
import pygame
import os
from PIL import ImageTk, Image

root = Tk()
root.title('Music Player')
root.geometry("500x300")

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

organize_menu = Menu(menubar, tearoff=False)
organize_menu.add_command(label='Select Folder')
menubar.add_cascade(label='Organize', menu=organize_menu)


songlist = Listbox(root, bg="black", fg="white", width=100, height=15)
songlist.pack()

play_btn_img = ImageTk.PhotoImage(Image.open("play.png"))
pause_btn_img = ImageTk.PhotoImage(Image.open("pause.png"))
next_btn_img = ImageTk.PhotoImage(Image.open("next.png"))
back_btn_img = ImageTk.PhotoImage(Image.open("back.png"))

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image=play_btn_img, borderwidth=0)
pause_btn = Button(control_frame, image=pause_btn_img, borderwidth=0)
next_btn = Button(control_frame, image=next_btn_img, borderwidth=0)
back_btn = Button(control_frame, image=back_btn_img, borderwidth=0)

play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
back_btn.grid(row=0, column=0, padx=7, pady=10)

root.mainloop()