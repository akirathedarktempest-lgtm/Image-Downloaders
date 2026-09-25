from customtkinter import *
import requests
import base64
import json
from PIL import ImageTk
import random
from tkinter import Button

window=CTk()
window.geometry("1920x1080")

data=requests.get("http://127.0.0.1:8000/randomimages/pfps")
image=data.content
image=json.loads(image)
img=image["image"]
img=base64.b64decode(img)
randomImage=ImageTk.PhotoImage(data=img,format='png')
Imagebutton=Button(window,image=randomImage,command=lambda:downloadImage(img,f"#{random.randint(0,1000)}"))
Imagebutton.place(anchor=CENTER,rely=0.5,relx=0.5)
rightSide=CTkButton(window,text=">",state=DISABLED)
rightSide.place(anchor=CENTER,rely=0.5,relx=0.8)
leftSide=CTkButton(window,text="<",state=DISABLED)
leftSide.place(anchor=CENTER,rely=0.5,relx=0.2)
pfpButton=CTkButton(window,text="PFPs!",command=lambda:otherWindows("pfps",1))
pfpButton.place(anchor=CENTER,rely=0.9,relx=0.4)
wallpaperButton=CTkButton(window,text="Wallpapers!",command=lambda:otherWindows("wallpapers",1))
wallpaperButton.place(anchor=CENTER,rely=0.9,relx=0.6)
labelNumber=CTkLabel(window,text="")
labelNumber.place(anchor=CENTER,rely=0.1,relx=0.5)

def downloadImage(image:bytes,name:str):
    with open(f"Bleach{name}.jpg","wb") as file:
        file.write(image)

def otherWindows(text:str,ids:int,rightbutton:CTkButton=rightSide,leftbutton:CTkButton=leftSide,pfp:CTkButton=pfpButton,wallpaperButton:CTkButton=wallpaperButton,label:CTkLabel=labelNumber,images=randomImage,imageButton=Imagebutton):
    global window
    global randomImage
    if text=="pfps":
        pfp.configure(state=DISABLED)
        wallpaperButton.configure(state=NORMAL)
    elif text=="wallpapaers":
        pfp.configure(state=NORMAL)
        wallpaperButton.configure(state=DISABLED)
    else:
        return print("Something's wrong there...")
    imageButton.destroy()
    data=requests.get(f"http://127.0.0.1:8000/images/{text}/{ids}")
    info=data.content
    info=json.loads(info)
    image=info["image"]
    image=base64.b64decode(image)
    randomImage=ImageTk.PhotoImage(data=image,format='png')
    imageButton=Button(window,image=randomImage,command=lambda:downloadImage(image,f"-bleach-{ids}"))
    imageButton.place(anchor=CENTER,rely=0.5,relx=0.5)
    label.configure(text=f"{ids}")
    if info["last?"] =="yes":
        right=DISABLED
    else:
        right=NORMAL
    if info["first?"] =="yes":
        left=DISABLED
    else:
        left=NORMAL
    rightbutton.configure(state=right,command=lambda:otherWindows(text,ids+1,imageButton=imageButton))
    leftbutton.configure(state=left,command=lambda:otherWindows(text,ids-1,imageButton=imageButton))

window.mainloop()

#hehe...took a while on fixing the little problem, the image wasn't showing up, and the problem was i was making a new image, i need to use randomImage one
#and there are more things left though, my db only has three images for now and only of pfps, now i will also add wallpapers to it
#maybe shifting from sqlite3 to mysql, and decoraton still matters for better ui/ux, so we will be working on that
#also, imported the db file, and backend...and all set!
