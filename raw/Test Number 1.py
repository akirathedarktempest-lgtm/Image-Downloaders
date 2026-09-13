import requests
import sqlite3
from tkinter import *

connect=sqlite3.connect("Image.db")
cursor=connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS pfps(
                  id INT,
                  image BLOB
)""")
def numbers():
    cursor.execute("SELECT * FROM pfps")
    images=cursor.fetchall()
    number=0
    for _ in images:
        number+=1
    return number

root=Tk()

entry=Entry(root)
entry.pack()
button=Button(root,text="Send to DB",command=lambda:sendImage(str(entry.get()),label))
button.pack()
label=Label(root,text="")
label.pack()

def sendImage(image:str,label:Label):
    response=requests.get(image)
    if response.status_code==200:
        cursor.execute("INSERT INTO pfps VALUES (?,?)",[numbers()+1,response.content])
        connect.commit()
        label.config(text="Done!")
        return
    else:
        return label.config(text="Not a valid link!")

root.mainloop()

#this will basically download the images in the db, this will be for the backend, not frontent
#i just wanted to test whether it can work or not, and i guess it did
