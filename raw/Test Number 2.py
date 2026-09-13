import sqlite3

connect=sqlite3.connect("Image.db")
cursor=connect.cursor()

cursor.execute("SELECT * FROM pfps")
info=cursor.fetchone()
image=info[1]
with open("image.jpg","wb") as f:
    f.write(image)

#this was to see whether it actually has it or not, and it has actually
