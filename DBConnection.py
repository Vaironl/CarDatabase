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
    cursor.execute('''CREATE TABLE IF NOT EXISTS carparts (carid INT, partname TEXT, notes TEXT)''')
    
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
    
def selectCar(carID):
    conn = sqlite3.connect(_db)
    cursor = conn.cursor()
    
    
    cursor.execute("SELECT * FROM carlist WHERE ID = " + str(carID))
    car = cursor.fetchall()
    
    conn.commit()
    conn.close()
    return car[0]
    

def fetchCarParts(carId):
    conn = sqlite3.connect(_db)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM carparts WHERE carid = " + str(carId))
    parts = cursor.fetchall()
    print parts
    
    conn.commit()
    conn.close()
    
    
    
def addCarPart():
    conn = sqlite3.connect(_db)
    cursor = conn.cursor()
    
    carID = selectCar()
    carPartName = raw_input("What is the name of the car part?")
    carNotes = raw_input("Add description or notes of this part: ")
    
    cursor.execute("INSERT INTO carparts VALUES (?,?,?)",(carID, carPartName, carNotes))
    
    conn.commit()
    conn.close()
    
def removeCar(car):
    conn = sqlite3.connect(_db)
    
    cursor = conn.cursor()
    
    #Create table
    cursor.execute("DELETE FROM carlist WHERE ID = " + car)
    
    # Save (commit) the changes
    conn.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()