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
    

def unit_inserter(name, move, ws, bs, str, tough, wound, att, ld, ar, invu, fnp, type, fact, war, points, min , max):
    database = r"WH40Kdata.db"
    
    conn = create_connection(database)
    
    with conn:
        UNIT = (name, move, ws, bs, str, tough, wound, att, ld, ar, invu, fnp, type, fact, war, points, min, max)
        UNIT_id = create_unit(conn, UNIT)
        
        
def create_melee_weapon(db, MW):



    sql = '''INSERT INTO MW (Name, Strength, Damage, AP, Points)

              VALUES(?,?,?,?,?)'''

    cur = conn.cursor()

    cur.execute(sql, MW)

    return cur.lastrowid

    

def melee_weapon_inserter(name, str, d, ap, pts):

    database = r"WH40Kdata.db"

    conn = create_connection(database)

    

    with conn:

        MW = (name, str, d, ap, pts)

        MW_id = create_melee_weapon(conn, MW)

    

def create_ranged_weapon(db, RW):

    sql = ''' INSERT INTO RW (Name, Strength, Damage, Range, AP, Type, Points)

                VALUES(?,?,?,?,?,?,?)'''

    cur = conn.cursor()

    cur.execute (sql, RW)

    return cur.lastrowid



def ranged_weapon_inserter(name, str, d, rng, ap, type, pts):

    database = r"WH40Kdata.db"

    conn = create_connection(database)

    

    with conn: 

        RW = (name, str, d, rng, ap, type, pts)

        RW_id = create_ranged_weapon(conn, RW)

        

def create_faction(db, Faction):



    sql = '''INSERT INTO Faction (Faction, Subfaction)

              VALUES(?,?)'''

    cur = conn.cursor()

    cur.execute (sql, Faction)

    return cur.lastrowid
    
    
def faction_inserter(faction, subfaction):
    database = r"WH40Kdata.db"
    
    conn = create_connection(database)
    
    with conn:
        Faction = (faction, subfaction)
        
        Faction_id = create_faction(conn, Faction)