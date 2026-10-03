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
right=CTkButton(window,text=">",state=DISABLED,command=lambda:pfpClick(types,ids+1,label,button,pfpButton,right,left,wallButton),hover_color="orange",border_width=1,border_color="white",height=50,width=50,corner_radius=100,text_color="white",bg_color="black",fg_color="black",font=CTkFont("Baskerville Old Face",size=35,weight="bold"))
right.place(anchor=CENTER,rely=0.5,relx=0.9)
left=CTkButton(window,text="<",state=DISABLED,command=lambda:pfpClick(types,ids-1,label,button,pfpButton,right,left,wallButton),hover_color="orange",border_width=1,border_color="white",height=50,width=50,corner_radius=100,text_color="white",bg_color="black",fg_color="black",font=CTkFont("Baskerville Old Face",size=35,weight="bold"))
left.place(anchor=CENTER,rely=0.5,relx=0.1)
pfpButton=CTkButton(window,text="PFP",state=NORMAL,command=lambda:pfpClick("pfps",1,label,button,pfpButton,right,left,wallButton),fg_color="black",text_color="white",font=CTkFont("Castellar",size=20),hover_color="#851818",height=20,width=50,corner_radius=100)
pfpButton.place(anchor=CENTER,rely=0.9,relx=0.35)
label=CTkLabel(window,text="",font=CTkFont("Baskerville Old Face",size=15))
label.place(anchor=CENTER,rely=0.1,relx=0.5)
wallButton=CTkButton(window,text="WallPaper",state=NORMAL,command=lambda:pfpClick("wallpapers",1,label,button,wallButton,right,left,wallButton),fg_color="black",text_color="white",font=CTkFont("Castellar",size=20),hover_color="#851818",height=20,width=50,corner_radius=100)
wallButton.place(anchor=CENTER,rely=0.9,relx=0.65)

ids=1
types="pfps"

def pfpClick(types:str,ids:int,label:CTkLabel,imageButton:Button,pfp:CTkButton,right:CTkButton,left:CTkButton,wall:CTkButton,random=randomImage):
    global randomImage
    global window
    global button
    data=databaseSearch(ids,types)
    label.configure(text=data[0])
    button.destroy()
    randomImage=ImageTk.PhotoImage(data=data[1],format='png')
    button=Button(window,image=randomImage,command=lambda:download(data[1],data[0]))
    button.place(anchor=CENTER,rely=0.5,relx=0.5)
    if data[0]==1:
        leftSide=DISABLED
    else:
        leftSide=NORMAL
    if data[0]==length(types):
        rightSide=DISABLED
    else:
        rightSide=NORMAL
    right.configure(state=rightSide,command=lambda:pfpClick(types,ids+1,label,imageButton,pfp,right,left,wall))
    left.configure(state=leftSide,command=lambda:pfpClick(types,ids-1,label,imageButton,pfp,right,left,wall))
    if types=="pfps":
        pfp.configure(state=DISABLED,command=lambda:pfpClick("pfps",1,label,imageButton,pfp,right,left,wall,randomImage))
        wall.configure(state=NORMAL,command=lambda:pfpClick("wallpapers",1,label,imageButton,pfp,right,left,wall,randomImage))
    else:
        pfp.configure(state=NORMAL,command=lambda:pfpClick("pfps",1,label,imageButton,pfp,right,left,wall,randomImage))
        wall.configure(state=DISABLED,command=lambda:pfpClick("wallpapers",1,label,imageButton,pfp,right,left,wall,randomImage))

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
#and i haven't added wallpapers for now, and decoration is also needed, but in one day, i can do this much only, i have written from beginning and used all by my brain...and no single debugging needed, lol Date: 10/01/26
#so, wallpaper is also fixed...and...haha, there were two problems coming, the button widget and the name...i didn't know what to do for a moment...but after spending some time at discord, suddenly an idea came and i realized what's the problem and solved that
#and then, at the button, image one, the screen wasn't appearing good because of old screen behind...once again, i just...made the button global and no use of imageButton...and the problem was fixed, lol
#i don't know...but i am just a genius, you see Date: 10/02/26
#and decoration is also done! (i just copied from the backend one...why can't i?)
#and this is also over, so...yay! and i'll work on alnst next, and also may try pyinstaller and join db, i don't know how though...
#but all set! Date: 10/03/26
