import tkinter as tk
import dbconnector as dbc

labels1 = ["MW name", "Strength", "Damage", "AP", "Points"]

r = 0
for label in labels1:
    tk.Label(text = label).grid(row = r, column = 0)
    r = r +1

# variables to store defender data from entries
wnameVar = tk.StringVar()
strengthVar = tk.StringVar()
damageVar = tk.StringVar()
apVar = tk.StringVar()
pointsVar = tk.StringVar()


#name
wnameEntry = tk.Entry(textvariable = wnameVar).grid(row = 0, column = 1)

#Strength
strEntry = tk.Entry(textvariable = strengthVar).grid(row = 1, column = 1)

#Damage
dmgEntry = tk.Entry(textvariable = damageVar).grid(row = 2, column = 1)

#AP
apEntry = tk.Entry(textvariable = apVar).grid(row = 3, column = 1)

#Points
pointsEntry = tk.Entry(textvariable = pointsVar).grid(row = 4, column = 1)


def saveInfoButton():
	
    weaponName = wnameVar.get()
    strength = strengthVar.get()
    damage = damageVar.get()
    ap = float(apVar.get())
    points = float(pointsVar.get())



    dbc.melee_weapon_inserter(weaponName, strength, damage, ap, points) 
	
	
	
saveButton = tk.Button(text = "Save info", command = saveInfoButton).grid(row=23, column = 1)



	


