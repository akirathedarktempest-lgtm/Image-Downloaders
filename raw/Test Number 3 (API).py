from fastapi import FastAPI
import sqlite3

app=FastAPI()

@app.get("/images/<type>/<ids>")
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
        cursor.execute(f"SELECT * FROM {types} WHERE ids={ids}")
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
        return {"image":data[1].decode("utf-8"),"credit":data[2],"last?":check,"first?":check1}
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
