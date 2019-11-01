import tkinter as tk
import dbconnector as dbc

root = tk.Tk()
labels1 = ["Unit name", "Move", "WS", "BS", "Wounds", "Strength", "Toughness", "Attacks", "Model count", "Leadership", "Armor save", "Inv. save", "FnP", "Faction", "Points"]

labels10 = ["Is Warlord", "Not Warlord"]

r = 0
for label in labels1:
    tk.Label(text = label).grid(row = r, column = 0)
    r = r +1

# variables to store defender data from entries
unameVar = tk.StringVar()
moveVar = tk.StringVar()
wsVar = tk.StringVar()
ballisVar = tk.StringVar()
ldVar = tk.StringVar()
warLordVar = tk.IntVar()
factionVar = tk.StringVar()
woundVar = tk.StringVar()
strengthVar = tk.StringVar()
toughVar = tk.StringVar()
attackVar = tk.StringVar()
dmcVar = tk.StringVar()
asVar = tk.StringVar()
isVar = tk.StringVar()
fnpVar = tk.StringVar()
typeVar = tk.IntVar()
pointsVar = tk.StringVar()

#name
unameEntry = tk.Entry(textvariable = unameVar).grid(row = 0, column = 1)

#move
moveEntry = tk.Entry(textvariable = moveVar).grid(row = 1, column = 1)

#WS
wsEntry = tk.Entry(textvariable = wsVar).grid(row = 2, column = 1)

#BS 
bsEntry = tk.Entry(textvariable = ballisVar).grid(row = 3, column = 1)

#wounds
woundEntry = tk.Entry(textvariable = woundVar).grid(row = 4, column = 1)

#strength
strEntry = tk.Entry(textvariable = strengthVar).grid(row = 5, column = 1)

#toughness 
toughEntry =tk.Entry(textvariable = toughVar).grid(row = 6, column = 1)

#attacks
attacksEntry = tk.Entry(textvariable = attackVar).grid(row = 7, column = 1)

#model count
dmcEntry =tk.Entry(textvariable = dmcVar).grid(row = 8, column = 1)

#Leadership
ldEntry = tk.Entry(textvariable = ldVar).grid(row = 9, column = 1)

#armor
asEntry =tk.Entry(textvariable = asVar).grid(row = 10, column = 1)

#invu save
isEntry = tk.Entry(textvariable = isVar).grid(row = 11, column = 1)

#fnp
fnpEntry = tk.Entry(textvariable = fnpVar).grid(row = 12, column = 1)

#faction
factionEntry = tk.Entry(textvariable = factionVar).grid(row = 13, column = 1)

#points
pointsEntry = tk.Entry(textvariable = pointsVar).grid(row = 14, column = 1)


r2 = 0
value = 1
for label in labels10:
    tk.Radiobutton(text = label, variable = warLordVar, value = value).grid(row = 22, column = r2)
    value = value +1 
    r2 = r2 +1

def saveInfoButton():
	
    defendName = unameVar.get()
    wounds = float(woundVar.get())
    toughness = float(toughVar.get())
    armor = float(asVar.get())
    invu = float(isVar.get())
    fnp = float(fnpVar.get())
    type = typeVar.get()
    warlord = warLordVar.get()
    str = float(strengthVar.get())
    move = float(moveVar.get())
    attacks = float(attackVar.get())
    faction = factionVar.get()
    ws = float(wsVar.get())
    bs = float(ballisVar.get())
    points = int(pointsVar.get())
    ld = float(ldVar.get())
	
	#model count, does not go in to same db table
    dmc = dmcVar.get()
	


    dbc.inserter(defendName, move, ws, bs, str, toughness, wounds, attacks, ld, armor, invu, fnp, type, faction, warlord, points) 
	
	
	
saveButton = tk.Button(text = "Save info", command = saveInfoButton).grid(row=23, column = 1)



	


