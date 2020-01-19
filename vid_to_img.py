import tkinter
from tkinter import *
import os
import time
import sqlite3
from tkinter import messagebox
from tkinter import filedialog
import cv2
video =' '
path_output_dir=''


def UploadAction(event=None):
    global video, path_output_dir
    filename = filedialog.askopenfilename()

    temp = str(filename).split('/')
    try:
        os.mkdir('{}'.format(temp[-1][:-4]))
    except:
        pass
    video = filename
    path_output_dir= temp[-1][:-4]

def video_to_frames():
    global video, path_output_dir
    print(video, path_output_dir)
    if len(video)<2 or len(path_output_dir)<2:
        messagebox.showinfo("Hello !!", "Please Enter Valid File")
        return 0
    # extract frames from a video and save to directory as 'x.png' where
    # x is the frame index
    vidcap = cv2.VideoCapture(video)
    count = 0
    while vidcap.isOpened():
        success, image = vidcap.read()
        if success:
            cv2.imwrite(os.path.join(path_output_dir, '%d.png') % count, image)
            count += 1
        else:
            break
    cv2.destroyAllWindows()
    vidcap.release()
    messagebox.showinfo("Hello !!", "Task Successfully Completed")


if __name__ == '__main__':

    qw=Tk()
    qw.title('Video To Image Converter')
    qw.geometry("300x200")
    l2 = Label(text='Choice Video File', font=("Calibri", 15))
    l2.place(x=10, y=25)
    button =  Button(qw, text='Open', command=UploadAction, width=8, height=2,background='#26548F')
    button.pack()
    button.place(x=170, y=25)
    button = Button(qw, text='Video To Images', command=video_to_frames, width=15, height=2, background='#26548F')
    button.pack()
    button.place(x=70, y=105)
    qw.mainloop()