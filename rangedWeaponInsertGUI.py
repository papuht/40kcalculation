import tkinter as tk
import dbconnector as dbc


labels = ["Name", "Strength", "Damage", "Range", "AP", "Type", "Attacks", "Points"]


r = 0
for label in labels:
    tk.Label(text = label).grid(row = r, column = 0)
    r = r +1

#variables to store data from entries
rwnameVar = tk.StringVar()
strVar = tk.StringVar()
damVar = tk.StringVar()
rangeVar = tk.StringVar()
apVar = tk.StringVar()
typeVar = tk.StringVar()
attacksVar = tk.StringVar()
pointsVar = tk.StringVar()

#name 
nameEntry = tk.Entry(textvariable = rwnameVar).grid(row = 0, column = 1)


#strength
strEntry = tk.Entry(textvariable = strVar).grid(row = 1, column = 1)

#damage
damEntry = tk.Entry(textvariable = damVar).grid(row = 2, column = 1)

#range 
rangeEntry = tk.Entry(textvariable = rangeVar).grid(row = 3, column = 1)

#ap 
apEntry = tk.Entry(textvariable = apVar).grid(row = 4, column = 1)

#type 
typeEntry = tk.Entry(textvariable = typeVar).grid(row = 5, column = 1)

#attacks 
attacksEntry = tk.Entry(textvariable = attacksVar).grid(row = 6, column = 1)

#points cost 
pointsEntry = tk.Entry(textvariable = pointsVar).grid(row = 7, column = 1)



def saveInfoButton():
	
    name = rwnameVar.get()
    strength = float(strVar.get())
    damage = damVar.get()
    range = float(rangeVar.get())
    ap = float(apVar.get())
    type = typeVar.get()
    attacks = attacksVar.get()
    points = int(pointsVar.get())


    dbc.ranged_weapon_inserter(name, strength, damage, range, ap, type, attacks, points) 
	
	
	
saveButton = tk.Button(text = "Save info", command = saveInfoButton).grid(row=23, column = 1)

 