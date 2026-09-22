from fastapi import FastAPI
import sqlite3
import base64
import random

app=FastAPI()

@app.get("/images/{types}/{ids}")
def getImages(types:str,ids:int):
    if types=="pfps" or types=="wallpapers" or types=="fandoms":
        if ids>number(types):
            return {"Out of the range":":("}
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
        image=base64.b64encode(image)#i learned something new by this project! an image can't be encoded easily by utf-8 or any level of utf, you will need base64 for that, and similar would be videos and audios, they are binary
        print(type(image))
        return {"image":image,"credit":data[2],"last?":check,"first?":check1,"ids":ids}
    else:
        return {"no type found":":("}

def number(types:str):
    if types=="pfps" or types=="wallpapers" or types=="fandoms":
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
        cursor.execute(f"SELECT image FROM {types}")
        data=cursor.fetchall()
        image=random.choice(data)
        print(type(image))
        image=image[0]
        print(type(image))
        img=base64.b64encode(image)
        print(type(img))
        return {"image":img}
    else:
        raise HTTPException(404)#fixed this error, shouldn't give 422 error, i actually changed the name and put types, working right now
