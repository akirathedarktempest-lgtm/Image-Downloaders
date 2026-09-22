from tkinter import *
import requests
from PIL import ImageTk
import json
import base64

root=Tk()
root.iconbitmap()
root.title("Bleach PFPs, Wallpaper!")

call=""
button1=Button(root,text="PFPs!",command=lambda:func(root,"pfps",1))
button2=Button(root,text="Wallpapers!",command=lambda:func(root,"wallpapers",1))
button1.place(anchor=CENTER,relx=0.20,rely=0.5)
button2.place(anchor=CENTER,relx=0.50,rely=0.5)
ids=1
#img=ImageTk.PhotoImage()

def createImage(image:bytes,number:int):
    with open(f"Bleach{number}.jpg","wb") as f:
        f.write(image)

def func(root:Tk,text:str,ids:int):
    global img
    root.destroy()
    window=Tk()
    root=window
    data=requests.get(f"http://127.0.0.1:8000/images/{text}/{ids}")
    data=data.content
    data=json.loads(data)
    image=data["image"]
    image=base64.b64decode(image)
    number=data["ids"]
    credit=data["credit"]
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
    labelIds=Label(root,text=f"{number}")
    labelIds.pack()
    img=ImageTk.PhotoImage(data=image,format='png')
    button=Button(root,image=img,command=lambda:createImage(image,ids))#yesterday, this wasn't working, the photos werent appearing, and it reminded me what i was taught when i was learning tkinter
    button.pack()#so i thought to start with an image already, so i used that random image thing in api, but today...it worked, lol...sometimes devs just need prayers to fix the bug
    buttonLeft=Button(root,text="<<",command=lambda:func(root,text,ids-1),state=left)
    buttonLeft.pack()
    buttonRight=Button(root,text=">>",command=lambda:func(root,text,ids+1),state=right)
    buttonRight.pack()
    labelCredit=Label(root,text=f"{credit}")
    labelCredit.pack()

root.mainloop()
