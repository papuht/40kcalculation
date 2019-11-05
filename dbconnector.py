import sqlite3
from sqlite3 import Error 



def create_connection(db):
    global conn
    conn = None
    
    try:
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)
    return conn 
    

def create_unit(db, UNIT):
    
    sql = '''INSERT INTO UNIT(Name, Move, WS, BS, Strength, Toughness, Wounds, Attack, Leadership, Armor, Invu, FNP, Type, Faction, Warlord, Points, Min, Max)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, UNIT)
    return cur.lastrowid    
    

def inserter(name, move, ws, bs, str, tough, wound, att, ld, ar, invu, fnp, type, fact, war, points, min , max):
    database = r"/home/raistlin/40kcalculation/WH40Kdata.db"
    
    conn = create_connection(database)
    
    with conn:
        UNIT = (name, move, ws, bs, str, tough, wound, att, ld, ar, invu, fnp, type, fact, war, points, min, max)
        UNIT_id = create_unit(conn, UNIT)