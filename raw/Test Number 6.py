from tkinter import *
import requests
from PIL import ImageTk
import json#forget to use this by mistake, but fixed

root=Tk()
root.iconbitmap()
root.title("Bleach PFPs, Wallpaper!")

call=""
button1=Button(root,text="PFPs!",command=lambda:func(root,"pfps",1))
button2=Button(root,text="Wallpapers!",command=lambda:func(root,"wallpapers",1))
button1.place(anchor=CENTER,relx=0.20,rely=0.5)
button2.place(anchor=CENTER,relx=0.50,rely=0.5)
ids=1

def createImage(image:bytes,number:int):
    with open(f"Bleach{number}.jpg","wb") as f:
        f.write(image)

def func(root:Tk,text:str,ids:int):
    global call
    call=call.replace(call,text)
    data=requests.get(f"http://127.0.0.1:8000/images/{text}/{ids}")
    data=data.content
    data=json.loads(data)
    image=data["image"].encode("utf-8")#but here now, there's something wrong with the api giving 404 error, not even coming on if else statement
    number=data["ids"]#i thought...i know backend...lol
    credit=data["credit"]#but i will find the problem, don't worry
    last=data["last?"]
    first=data["first?"]
    if first=="yes":
        left=DISABLED
    else:
        left=NORMAL
    if last=="yes":
        right=DISABLED
    else:
        right=NORMAL
    window=Tk()
    root.destroy()
    root=window
    labelIds=Label(root,text=f"{number}")
    labelIds.pack()
    img=ImageTk.PhotoImage(data=image,format='png')
    button=Button(root,image=img,command=lambda:createImage(image,ids))
    button.pack()
    buttonLeft=Button(root,text="<<",command=lambda:func(root,text,ids-1),state=left)
    buttonLeft.pack()
    buttonRight=Button(root,text=">>",command=lambda:func(root,text,ids+1),state=right)
    buttonRight.pack()
    labelCredit=Label(root,text=f"{credit}")
    labelCredit.pack()

root.mainloop()
