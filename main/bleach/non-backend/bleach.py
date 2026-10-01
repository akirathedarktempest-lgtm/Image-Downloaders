from customtkinter import *
from tkinter import Button, CENTER
import random
import sqlite3
from PIL import ImageTk

window=CTk()
set_appearance_mode("dark")
window.geometry("1920x1080")

def returnRandom():
    connect=sqlite3.connect("Image.db")
    cursor=connect.cursor()
    cursor.execute("SELECT * FROM pfps")
    data=cursor.fetchall()
    ran=random.choice(data)
    return [ran[1],ran[0]]

def download(image:bytes,number:int):
    with open(f"bleach-{number}.jpg","wb") as file:
        file.write(image)

image=returnRandom()

randomImage=ImageTk.PhotoImage(data=(image[0]),format='png')
button=Button(window,image=randomImage,command=lambda:download(image[0],image[1]),height=randomImage.height(),width=randomImage.width())
button.place(anchor=CENTER,rely=0.5,relx=0.5)
right=CTkButton(window,text=">",state=DISABLED,command=lambda:pfpClick(ids+1,label,button,pfpButton,right,left))
right.place(anchor=CENTER,rely=0.5,relx=0.9)
left=CTkButton(window,text="<",state=DISABLED,command=lambda:pfpClick(ids-1,label,button,pfpButton,right,left))
left.place(anchor=CENTER,rely=0.5,relx=0.1)
pfpButton=CTkButton(window,text="PFP",state=NORMAL,command=lambda:pfpClick(1,label,button,pfpButton,right,left))
pfpButton.place(anchor=CENTER,rely=0.9,relx=0.5)
label=CTkLabel(window,text="")
label.place(anchor=CENTER,rely=0.1,relx=0.5)

ids=1

def pfpClick(ids:int,label:CTkLabel,imageButton:Button,pfp:CTkButton,right:CTkButton,left:CTkButton):
    global randomImage
    global window
    data=databaseSearch(ids,"pfps")
    label.configure(text=data[0])
    imageButton.destroy()
    randomImage=ImageTk.PhotoImage(data=data[1],format='png')
    imageButton=Button(window,image=randomImage,command=lambda:download(data[1],data[0]))
    imageButton.place(anchor=CENTER,rely=0.5,relx=0.5)
    pfp.configure(state=DISABLED,command=lambda:pfpClick(1,label,imageButton,pfp,right,left),)
    if data[0]==1:
        leftSide=DISABLED
    else:
        leftSide=NORMAL
    if data[0]==length("pfps"):
        rightSide=DISABLED
    else:
        rightSide=NORMAL
    right.configure(state=rightSide,command=lambda:pfpClick(ids+1,label,imageButton,pfp,right,left))
    left.configure(state=leftSide,command=lambda:pfpClick(ids-1,label,imageButton,pfp,right,left))

def databaseSearch(ids:int,types:str):
    connect=sqlite3.connect("Image.db")
    cursor=connect.cursor()
    cursor.execute(f"SELECT * FROM {types} WHERE id={ids}")
    data=cursor.fetchone()
    connect.close()
    return data

def length(types:str):
    connect=sqlite3.connect("Image.db")
    cursor=connect.cursor()
    cursor.execute(f"SELECT * FROM {types}")
    data=cursor.fetchall()
    connect.close()
    return len(data)

window.mainloop()

#this is how you can do that, without backend or internet, the database should be with you in your pocket or hands
#and i haven't added wallpapers for now, and decoration is also needed, but in one day, i can do this much only, i have written from beginning and used all by my brain...and no single debugging needed, lol
