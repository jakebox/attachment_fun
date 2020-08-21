# 
# GUI for random iMessage attachment opener
# By Jake Boxerman, Aug. 2020
#

import tkinter as tk
import subprocess, time
from randomImage import *

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

imageGrabber = RandomAttachmenter(messages_path)
media_path, file_type = imageGrabber.get_random_image()
#print("\n" + media_path, file_type)

def runScript():
    global file_type
    media_path, file_type = imageGrabber.get_random_image()
    imageGrabber.open_media(media_path, file_type)

def closeMediaApps():
    if file_type == "image":
        subprocess.call(["sh", "scripts/closePreview.sh"])
    elif file_type == "video":
        subprocess.call(["sh", "scripts/closeQuicktime.sh"])

def cycleImage():
    closeMediaApps()
    runScript()

def quit():
    subprocess.call(["sh", "scripts/closeQuicktime.sh"])
    subprocess.call(["sh", "scripts/closePreview.sh"])
    root.destroy()

# Buttons
button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit) 
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Open",
                   height="10",
                   width="20",
                   command=cycleImage)
slogan.pack(side=tk.LEFT)

root.title("Attachment Fun")
root.attributes("-topmost", True)
root.mainloop()
