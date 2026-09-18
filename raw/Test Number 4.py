from tkinter import *
import sqlite3
from PIL import ImageTk#use pillow, PIL

connect=sqlite3.connect("Image.db")
cursor=connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS pfps(
                  id INT,
                  image BLOB
)""")
cursor.execute("SELECT * FROM pfps")
data=cursor.fetchone()
root=Tk()

fileformat='png'
mae=data[1]
connect.close()

#canvas=Canvas(root,width=300,height=300)
#canvas.pack()
img=ImageTk.PhotoImage(data=mae,format=fileformat)#don't use tkinter PhotoImage, it will cause a lot of problem, so use PIL ImageTk.PhotoImage
label=Label(root,image=img)
label.pack()
#canvas.create_image(image=img)

root.mainloop()
#to be honest, i was losing my hope, but then download pillow from pip and then run and boom!
#bambi was in front of me...laughing...and i am still blushing by looking at her! aaaaahhhhhhhh!!!!!!(her image which was in db)
#...i am still blushing...i thought it wouldn't work (because of tkinter.PhotoImage) but pil...made me blush now...
#now we are almost there to make a basic image downloader, first by tkinter and then customtkinter i guess, and all set!
