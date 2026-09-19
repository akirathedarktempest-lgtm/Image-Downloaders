#not going to make everything at once, slow and steady wins the race
from tkinter import *#for you and i-- i mean, gui
import requests#for backend
from PIL import ImageTk#for images

root=Tk()
root.iconbitmap()
root.title("Bleach PFPs, Wallpaper!")

call=""
button1=Button(root,text="PFPs!",command=lambda:func(root,"pfps"))
button2=Button(root,text="Wallpapers!",command=lambda:func(root,"wallpapers"))
button3=Button(root,text="Fan~Made!",command=lambda:func(root,"fanmade"))

def func(root:Tk,text:str):
    global call
    if text=="pfps":
        call=call.replace(call,"pfps")
    if text=="wallpapers":
        call=call.replace(call,"wallpapers")
    if text=="fanmade":
        call=call.replace(call,"fanmade")

root.mainloop()
