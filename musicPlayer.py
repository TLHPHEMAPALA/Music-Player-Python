import cv2
from tkinter import *
import tkinter as tk 
from tkinter import PhotoImage,filedialog
from PIL import Image, ImageTk
from pygame import mixer
import os


mixer.init()

def update_frame():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=img)
        panel.img = img
        panel.config(image=img)
        root.after(10, update_frame)


def start_camera():
    global cap
    cap = cv2.VideoCapture(0)
    update_frame()


def stop_camera():
    cap.release()
    panel.config(image="")
    panel.img = None


def play_song():
    music_name = playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])

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


root = tk.Tk()
root.title("Camera App")
root.geometry("1080x480")  # Set your desired width and height

# Create left and right frames
left_frame = tk.Frame(root, width=480, height=600, bg="lightblue")
left_frame.pack(side=tk.LEFT, fill=tk.BOTH)

# Disable propagation for the left frame
left_frame.pack_propagate(False)

right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

# Right frame content for camera preview
panel = tk.Label(right_frame)
panel.pack()

# Logobackground
#Logobackground = PhotoImage(file="Logobackground.png")
#label_logobackground = Label(root, image=Logobackground, bg="lightblue")
#label_logobackground.place(x=15, y=320)

# label
music = Label(root, text="", font=("arial", 13), fg="white", bg="lightblue")
music.place(x=40, y=630, anchor="center")

# music
Menu = PhotoImage(file="whitebg.png")
label_menu = Label(root, image=Menu, bg="lightblue")
label_menu.place(x=40, y=55)

music_frame = Frame(root, bd=2, relief=RIDGE)
music_frame.place(x=60, y=75, width=360, height=199)


scroll = Scrollbar(music_frame)
playlist = Listbox(music_frame, width=200, font=("arial", 10), bg="#333333", fg="grey",
                   selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.xview)
#scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)


# Left frame content
Button(root, text="Open Playlist", width=13, height=2, font=(
    "arial", 7, "bold"), fg="white", bg="#21b3de", command=open_folder).place(x=60, y=320)

Button(root, text="Emotion Mode", width=12, height=2, font=(
    "arial", 7, "bold"), fg="white", bg="#21b3de", command=open_folder).place(x=148, y=320)

Button(root, text="Hand Gesture Mode", width=15, height=2, font=(
    "arial", 7, "bold"), fg="white", bg="#21b3de", command=open_folder).place(x=230, y=320)

Button(root, text="Stop Camera", width=12, height=2, font=(
    "arial", 7, "bold"), fg="white", bg="#21b3de", command=open_folder).place(x=330, y=320)

# Canvas-based buttons
play_button = PhotoImage(file="play.png")
canvas_play = Canvas(root, width=play_button.width(), height=play_button.height(), bg="#ffffff", bd=0, highlightthickness=0)
canvas_play.place(x=40, y=370)
canvas_play.create_image(0, 0, anchor=NW, image=play_button)
canvas_play.bind("<Button-1>", lambda event: play_song())

pause_button = PhotoImage(file="pause.png")
canvas_pause = Canvas(root, width=pause_button.width(), height=pause_button.height(), bg="#ffffff", bd=0, highlightthickness=0)
canvas_pause.place(x=140, y=370)
canvas_pause.create_image(0, 0, anchor=NW, image=pause_button)
canvas_pause.bind("<Button-1>", lambda event: mixer.music.pause())

stop_button = PhotoImage(file="stop.png")
canvas_stop = Canvas(root, width=stop_button.width(), height=stop_button.height(), bg="#ffffff", bd=0, highlightthickness=0)
canvas_stop.place(x=240, y=370)
canvas_stop.create_image(0, 0, anchor=NW, image=stop_button)
canvas_stop.bind("<Button-1>", lambda event: mixer.music.stop())

resume_button = PhotoImage(file="fastforward.png")
canvas_resume = Canvas(root, width=resume_button.width(), height=resume_button.height(), bg="#ffffff", bd=0, highlightthickness=0)
canvas_resume.place(x=340, y=370)
canvas_resume.create_image(0, 0, anchor=NW, image=resume_button)
canvas_resume.bind("<Button-1>", lambda event: mixer.music.unpause())



root.mainloop()
