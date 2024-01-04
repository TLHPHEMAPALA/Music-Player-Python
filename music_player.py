from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root = Tk()
root.title("Music Player")
root.geometry("920x670+290+85")
root.configure(bg="#1a1b2b")
root.resizable(False, False)

mixer.init()

def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)

def play_song():
    music_name = playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])

# icon
image_icon = PhotoImage(file="icons8-music-100.png")
root.iconphoto(False, image_icon)

# logo
Logo = PhotoImage(file="icons8-music-100.png")
Label(root, image=Logo, bg="#1a1b2b").place(x=50, y=50)

# Canvas-based buttons
play_button = PhotoImage(file="play.png")
canvas_play = Canvas(root, width=play_button.width(), height=play_button.height(), bg="#1a1b2b", bd=0, highlightthickness=0)
canvas_play.place(x=20, y=550)
canvas_play.create_image(0, 0, anchor=NW, image=play_button)
canvas_play.bind("<Button-1>", lambda event: play_song())

pause_button = PhotoImage(file="pause.png")
pause_button = pause_button.zoom(1, 1)
canvas_pause = Canvas(root, width=pause_button.width(), height=pause_button.height(), bg="#1a1b2b", bd=0, highlightthickness=0)
canvas_pause.place(x=120, y=550)
canvas_pause.create_image(0, 0, anchor=NW, image=pause_button)
canvas_pause.bind("<Button-1>", lambda event: mixer.music.pause())

stop_button = PhotoImage(file="stop.png")
canvas_stop = Canvas(root, width=stop_button.width(), height=stop_button.height(), bg="#1a1b2b", bd=0, highlightthickness=0)
canvas_stop.place(x=220, y=550)
canvas_stop.create_image(0, 0, anchor=NW, image=stop_button)
canvas_stop.bind("<Button-1>", lambda event: mixer.music.stop())

resume_button = PhotoImage(file="fastforward.png")
canvas_resume = Canvas(root, width=resume_button.width(), height=resume_button.height(), bg="#1a1b2b", bd=0, highlightthickness=0)
canvas_resume.place(x=320, y=550)
canvas_resume.create_image(0, 0, anchor=NW, image=resume_button)
canvas_resume.bind("<Button-1>", lambda event: mixer.music.unpause())

# label
music = Label(root, text="", font=("arial", 13), fg="white", bg="#1a1b2b")
music.place(x=250, y=530, anchor="center")

# music
Menu = PhotoImage(file="White_box_28x52.png", width=430, height=260)
label_menu = Label(root, image=Menu, bg="#1a1b2b")
label_menu.place(x=470, y=55)

music_frame = Frame(root, bd=2, relief=RIDGE)
music_frame.place(x=485, y=70, width=400, height=230)

Button(root, text="Open Folder", width=15, height=2, font=(
    "arial", 10, "bold"), fg="white", bg="#21b3de", command=open_folder).place(x=30, y=170)

scroll = Scrollbar(music_frame)
playlist = Listbox(music_frame, width=100, font=("arial", 10), bg="#333333", fg="grey",
                   selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.xview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)

root.mainloop()
