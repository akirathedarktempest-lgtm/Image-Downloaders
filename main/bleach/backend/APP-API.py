from fastapi import FastAPI,HTTPException
import sqlite3
import base64
import random

app=FastAPI()

@app.get("/images/{types}/{ids}")
def getImages(types:str,ids:int):
    if types=="pfps" or types=="wallpapers":
        if ids>number(types):
            raise HTTPException(404)
        if ids<1:
            raise HTTPException(404)
        connect=sqlite3.connect("Image.db")
        cursor=connect.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {types}(
                            id INT,
                            image BLOB,
                            credit TEXT,
                            type TEXT)""")
        cursor.execute(f"SELECT * FROM {types} WHERE id={ids}")
        data=cursor.fetchone()
        if ids==number(types):
            check="yes"
        else:
            check="no"
        if ids==1:
            check1="yes"
        else:
            check1="no"
        connect.close()
        print(data[0],data[2],type(data[1]))
        image=data[1]
        image=base64.b64encode(image)
        print(type(image))
        return {"image":image,"credit":data[2],"last?":check,"first?":check1,"ids":ids}
    else:
        raise HTTPException(404)

def wallpaperNumber(types:str="wallpapers"):
    if types=="wallpapers":
        connect=sqlite3.connect("WallImage.db")
        cursor=connect.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {types}(
                            id INTEGER,
                            image BLOB,
                            credit TEXT,
                            type TEXT)""")
        cursor.execute("SELECT * FROM {types}")
        info=cursor.fetchall()
        return len(info)#there's no use of this, ignore this command

def number(types:str):
    if types=="pfps" or types=="wallpapers":
        connect=sqlite3.connect("Image.db")
        cursor=connect.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {types}(
                        id INT,
                        image BLOB,
                        credit TEXT,
                        type TEXT)""")
        cursor.execute(f"SELECT * FROM {types}")
        info=cursor.fetchall()
        connect.close()
        return len(info)
    else:
        return 0

@app.get("/randomimages/{types}")
def randomImage(types:str):
    if types =="pfps":
        connect=sqlite3.connect("Image.db")
        cursor=connect.cursor()
        cursor.execute(f"SELECT image FROM pfps")
        data=cursor.fetchall()
        image=random.choice(data)
        print(type(image))
        image=image[0]
        print(type(image))
        img=base64.b64encode(image)
        print(type(img))
        return {"image":img}
    else:
        raise HTTPException(404)

#there was so mess at db, i added wallpapers but i don't know how it only went to pfps table
#and from pfps table, it was showing them as well, then an hour later i realized it, then shifted them all to wallpapers db and removed from pfps...i don't know what the code of inserting images did, but never mind
