import tkinter as tk
import calculation
import attacker
import defender
import dbconnector as dbc
        


root = tk.Tk()

# strings for different fields of data

labels1 = ["Unit name", "Move", "WS", "BS", "Wounds", "Strength", "Toughness", "Attacks", "Model count", "Leadership", "Armor save", "Inv. save", "FnP", "Faction", "Points"]
labels2 = ["Weapon name", "Damage", "Strength", "Model count", "Armor piercing", "No. of attacks", "Ballistic skill"]
labels3 = ["Print unit data", "Print attack data", "Calculate result"]
labels4 = ["Re-roll to hit 1's", "Re-roll to hit all", "No to hit re-rolls"]
labels5 = ["Re-roll to wound 1's", "Re-roll to wound all", "No to wound re-rolls"]
labels6 = ["Poison attack 2+", "Poison attack 4+", "No poison attack"]
labels7 = ["Target is vehicle", "Target is monster", "Target is infantry", "Target is flyer", "Target is character"]
labels8 = ["-3 AP on 6's to-hit", "-4 AP on 6's to-hit", "-6 AP on 6's to-hit", "No AP bonus"]
labels9 = ["Auto wounds on hit"] 
labels10 = ["Is Warlord", "Not Warlord"]
r = 0
for label in labels1:
    tk.Label(text = label).grid(row = r, column = 0)
    r = r +1

# variables to store defender data from entries
unameVar = tk.StringVar()
moveVar = tk.StringVar()
wsVar = tk.StringVar()
bsVar = tk.StringVar()
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
bsEntry = tk.Entry(textvariable = bsVar).grid(row = 3, column = 1)

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
for label in labels2:
    tk.Label(text = label).grid(row = r2, column = 2)
    r2 = r2 +1


# variables to store attacker data 
wnameVar = tk.StringVar()
damaVar = tk.StringVar()
strVar = tk.StringVar()
apVar = tk.StringVar()
mcVar = tk.StringVar()
attVar = tk.StringVar()
bsVar = tk.StringVar()
poisonVar = tk.IntVar()
RRHitvar = tk.IntVar()
RRWoundvar = tk.IntVar()
rendVar = tk.IntVar()
autoWoundVar = tk.IntVar()

wnameEntry = tk.Entry(textvariable = wnameVar).grid(row = 0, column = 3)
damaEntry = tk.Entry(textvariable = damaVar).grid(row = 1, column = 3)
strEntry = tk.Entry(textvariable = strVar).grid(row = 2, column = 3)
mcEntry = tk.Entry(textvariable = mcVar).grid(row = 3, column = 3)
apEntry = tk.Entry(textvariable = apVar).grid(row = 4, column = 3)
noAtEntry = tk.Entry(textvariable = attVar).grid(row = 5, column = 3)
bsEntry = tk.Entry(textvariable = bsVar).grid(row = 6, column = 3)
    
def calculateButtonCB(): # this callback employs the calculation methods and creates objects for calculation 


    defendName = unameVar.get()
    wounds = float(woundVar.get())
    toughness = float(toughVar.get())
    dmc = float(dmcVar.get())
    armor = float(asVar.get())
    invu = float(isVar.get())
    fnp = float(fnpVar.get())
    type = typeVar.get()
	
    
    #defender = defender.DefendingUnit(defendName, wounds, toughness, dmc, armor, invu, fnp)  # asetettu kommenteiksi jotta ei tekisi vielä mitään


    wname = wnameVar.get()
    damage = float(damaVar.get())
    str = float(strVar.get())
    ap = float(apVar.get())
    bs = float(bsVar.get())
    att = float(attVar.get())
    mc = float(mcVar.get())
    poison = poisonVar.get()
    rerollHit = RRHitvar.get()
    rerollWound = RRWoundvar.get()
    rending = rendVar.get()
    autoWound = autoWoundVar.get()
    
    
     
    
    
    #att = attacker.Attacker(wname, str, damage, ap, bs, att, mc)
    print("Attacking weapon:", wname)
    print("Target unit:", defendName)
    print("Number of hits:", calculation.calculateHits(bs, att, mc, rerollHit))
    Hits = calculation.calculateHits(bs, att, mc, rerollHit)
    print("Number of wounds:", calculation.calculateWounds(Hits, str, toughness, rerollWound))
    Wounds = calculation.calculateWounds(Hits, str, toughness, rerollWound)
    print("Number of succesfull saves:", calculation.calculateSaveType(Wounds, armor, invu, ap, rending))
    savesMade = calculation.calculateSaveType(Wounds, armor, invu, ap, rending)
    print("Initial damage:", calculation.calculateDamage(Wounds, damage, savesMade))
    damageDone = calculation.calculateDamage(Wounds, damage, savesMade)
    print("After FnP:", calculation.calculateFNP(damageDone, fnp))



def saveInfoButton():
	
    defendName = unameVar.get()
    wounds = float(woundVar.get())
    toughness = float(toughVar.get())
    dmc = float(dmcVar.get())
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
    bs = float(bsVar.get())
    points = float(pointsVar.get())
    ld = float(ldVar.get())
	
	


    dbc.inserter(name, move, ws, bs, str, toughness, wounds, attacks, ld, armor, invu, fnp, type, faction, warlord) 
    


  
# radiobuttons below are for determining rerolls for calculation 


r4 = 0
value = 1
for label in labels4:
    tk.Radiobutton(text = label, variable = RRHitvar, value = value).grid(row = 16, column = r4) 
    value = value +1
    r4 = r4 +1
    


r5 = 0
value2 = 1
for label in labels5:
    tk.Radiobutton(text = label, variable = RRWoundvar, value = value2).grid(row = 17, column = r5) 
    value2 = value2 +1
    r5 = r5 +1

# radiobutton to mark attack as poisoned     

r6 = 0
value3 = 1
for label in labels6:
    tk.Radiobutton(text = label, variable = poisonVar, value = value3).grid(row = 18, column = r6)
    value3 = value3 +1
    r6 = r6 +1

r7 = 0
value4 = 1
for label in labels7:
        tk.Radiobutton(text = label, variable = typeVar, value = value4).grid(row = 19, column = r7)
        value4 = value4 +1
        r7 = r7+1
        
r8 = 0
value5 = 1
for label in labels8:
    tk.Radiobutton(text = label, variable = rendVar, value = value5).grid(row = 20, column = r8)
    value5 = value5 +1
    r8 = r8 +1

r9 = 0
value6 = 1
for label in labels9:
    tk.Radiobutton(text = label, variable = autoWoundVar, value = value6).grid(row = 21, column = r9)


r10 = 0
value7 = 1
for label in labels10:
    tk.Radiobutton(text = label, variable = warLordVar, value = value7).grid(row = 22, column = r10) 


calculateButton = tk.Button(text = "Calculate hits", command = calculateButtonCB).grid(row = 22, column = 0)
saveButton = tk.Button(text = "Save info", command = saveInfoButton).grid(row=22, column = 1)
loadButton = tk.Button(text = "Load from database").grid(row = 22, column = 2)

root.mainloop()