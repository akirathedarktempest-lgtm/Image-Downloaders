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

@app.get("/images/random/pfp")
def randomImage():
    connect=sqlite3.connect("Image.db")
    cursor=connect.cursor()
    cursor.execute("SELECT * FROM pfps")
    data=cursor.fetchall()
    image=random.choice(data)
    image=image[1]
    img=base64.b64encode(image)#here is a problem, giving 422 error, which means the code and requests was taken but can't send information? but i'll look at its types
    return {"image":img}
