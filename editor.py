# Import

from tkinter import *
from moviepy.editor import *

# Global Variables

clip1 = VideoFileClip("1.mp4")
clip2 = VideoFileClip("2.mp4")
clip3 = VideoFileClip("3.mp4")


# Functions

def effect_merge():
    final_clip = concatenate_videoclips([clip1, clip2, clip3])
    final_clip.write_videofile("Final Render.mp4")


def effect_invert():
    clip_invert = clip1.fx(vfx.mirror_x)
    clip_invert.write_videofile("Inverted.mp4")


def effect_resize():
    r = float(input("Enter your Size : "))
    clip_resize = clip1.resize(r)
    clip_resize.write_videofile("Resized.mp4")


def effect_speed():
    s = float(input("Enter your Speed : "))
    clip_speed = clip1.fx(vfx.speedx, s)
    clip_speed.write_videofile("Speed.mp4")


def effect_color():
    c = float(input("Enter your Brightness : "))
    clip_color = clip1.fx(vfx.colorx, c)
    clip_color.write_videofile("Coloured.mp4")


def effect_trim():
    starting = int(input("Enter your Starting Point : "))
    ending = int(input("Enter your Ending Point : "))
    clip_trim = clip1.cutout(starting, ending)
    clip_trim.write_videofile("Trimmed.mp4")


# def effect_audiofile():
# import moviepy.editor as mpe
# audioclip = mpe.AudioFileClip("Audio.mp3")
# videoclip = mpe.videoclip.set_audio(audioclip)
# final_clip = videoclip.set_audio(audioclip)
# final_clip.write_videofile("Final-with-audio.mp4")


# Main Screen

root = Tk()
root.title("Video Editor")
root.geometry("750x200")
root.minsize(750, 200)
root.maxsize(750, 200)
root.config(bg="#232323")

# Actions

# Merge
b = Button(root, text="Merge", relief=GROOVE, bg="#232323", fg="white", command=effect_merge)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

# Invert
b = Button(root, text="Invert", relief=GROOVE, bg="#232323", fg="white", command=effect_invert)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

# Resize
b = Button(root, text="Resize", relief=GROOVE, bg="#232323", fg="white", command=effect_resize)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

# Speed
b = Button(root, text="Speed", relief=GROOVE, bg="#232323", fg="white", command=effect_speed)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

# Color
b = Button(root, text="Color", relief=GROOVE, bg="#232323", fg="white", command=effect_color)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

# Trim
b = Button(root, text="Trim", relief=GROOVE, bg="#232323", fg="white", command=effect_trim)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

# Audio
# b = Button(root, text="Audio", relief=GROOVE, bg="#232323", fg="white", command=effect_audiofile)
# b.pack(side="left", padx=20)
# b.config(width=8, #height=3)

# Main
root.mainloop()
