import sqlite3
import os

_db = None

def initConnection(db):
    global _db
    _db = str(db)
    conn = sqlite3.connect(_db)
    
    cursor = conn.cursor()
    
    #Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS carlist (ID integer primary key, make TEXT, model TEXT, year TEXT, horsepower TEXT, engine TEXT,transmission TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS carparts (CARID INT, partname TEXT, notes TEXT)''')
    
    # Save (commit) the changes
    conn.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
    

def listCars():
    conn = sqlite3.connect(_db)
    cursor = conn.cursor()
    
    #Create table
    cursor.execute("SELECT * FROM carlist")
    
    carlist = cursor.fetchall()
    # Save (commit) the changes
    conn.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
    
    return carlist

def clearAllValues():
    conn = sqlite3.connect(_db)
    cursor = conn.cursor()
    
    #Create table
    cursor.execute("DELETE FROM carlist")
    
    # Save (commit) the changes
    conn.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


def addCar(_car):
    conn = sqlite3.connect(_db)
    cursor = conn.cursor()
    
    #NONE for ID
    cursor.execute("INSERT INTO carlist VALUES (?,?,?,?,?,?,?)", (None,_car[0],_car[1],_car[2],_car[3],_car[4],_car[5]) )
    
    conn.commit()
    conn.close()
    
def updateCar(ID, _car):
    conn = sqlite3.connect(_db)
    cursor = conn.cursor()
    
    #NONE for ID
    #cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (uPrice, uId))
    cursor.execute("UPDATE carlist SET MAKE = ?, MODEL = ?, YEAR = ?, HORSEPOWER = ?, ENGINE = ?, TRANSMISSION = ? WHERE ID = ?", (_car[0],_car[1],_car[2],_car[3],_car[4],_car[5], ID) )
    
    conn.commit()
    conn.close()
    
def selectCar(carID):
    conn = sqlite3.connect(_db)
    cursor = conn.cursor()
    
    
    cursor.execute("SELECT * FROM carlist WHERE ID = " + str(carID))
    car = cursor.fetchall()
    
    conn.commit()
    conn.close()
    return car[0]
    

def fetchCarParts(carID):
    conn = sqlite3.connect(_db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM carparts WHERE CARID = " + carID)
    parts = cursor.fetchall()
    #print parts
    conn.commit()
    conn.close()
    return parts
    
def addCarPart(carID, carPartName, carNotes):
    conn = sqlite3.connect(_db)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO carparts VALUES (?,?,?)",(carID, carPartName, carNotes))
    
    conn.commit()
    conn.close()
    
    
def removeCar(car):
    conn = sqlite3.connect(_db)
    
    cursor = conn.cursor()
    
    #Create table
    cursor.execute("DELETE FROM carlist WHERE ID = " + car)
    cursor.execute("DELETE FROM carparts WHERE carid = " + car)
    
    # Save (commit) the changes
    conn.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
    
def removeCarParts(carID, partname):
    conn = sqlite3.connect(_db)
    cursor = conn.cursor()
    #Create table
    cursor.execute("DELETE FROM carparts WHERE carid = ? AND partname = ? ", (carID, partname))
    conn.commit()
    conn.close()
    