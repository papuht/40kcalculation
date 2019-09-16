import tkinter as tk
import calculation
import attacker
import defender

        


root = tk.Tk()

# strings for different fields of data

labels1 = ["Unit name", "Wounds", "Toughness", "Model count", "Armor save", "Inv. save", "FnP"]
labels2 = ["Weapon name", "Damage", "Strength", "Model count", "Armor piercing", "No. of attacks", "Ballistic skill"]
labels3 = ["Print unit data", "Print attack data", "Calculate result"]
labels4 = ["Re-roll to hit 1's", "Re-roll to hit all", "No to hit re-rolls"]
labels5 = ["Re-roll to wound 1's", "Re-roll to wound all", "No to wound re-rolls"]
labels6 = ["Poison attack"]

r = 0
for label in labels1:
    tk.Label(text = label).grid(row = r, column = 0)
    r = r +1

# variables to store defender data from entries
unameVar = tk.StringVar()
woundVar = tk.StringVar()
toughVar = tk.StringVar()
dmcVar = tk.StringVar()
asVar = tk.StringVar()
isVar = tk.StringVar()
fnpVar = tk.StringVar()

unameEntry = tk.Entry(textvariable = unameVar).grid(row = 0, column = 1)
woundEntry = tk.Entry(textvariable = woundVar).grid(row = 1, column = 1)
toughEntry =tk.Entry(textvariable = toughVar).grid(row = 2, column = 1)
dmcEntry =tk.Entry(textvariable = dmcVar).grid(row = 3, column = 1)
asEntry =tk.Entry(textvariable = asVar).grid(row = 4, column = 1)
isEntry = tk.Entry(textvariable = isVar).grid(row = 5, column = 1)
fnpEntry = tk.Entry(textvariable = fnpVar).grid(row = 6, column = 1)

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
var = tk.IntVar()
var1 = tk.IntVar()

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
    
    #defender = defender.DefendingUnit(defendName, wounds, toughness, dmc, armor, invu, fnp)  # asetettu kommenteiksi jotta ei tekisi vielä mitään


    wname = wnameVar.get()
    damage = float(damaVar.get())
    str = float(strVar.get())
    ap = float(apVar.get())
    bs = float(bsVar.get())
    att = float(attVar.get())
    mc = float(mcVar.get())
    poison = poisonVar.get()
    rerollHit = var.get()
    rerollWound = var1.get()
    
    
     
    
    
    #att = attacker.Attacker(wname, str, damage, ap, bs, att, mc)
    print("Attacking weapon:", wname)
    print("Target unit:", defendName)
    print("Number of hits:", calculation.calculateHits(bs, att, mc, rerollHit))
    Hits = calculation.calculateHits(bs, att, mc, rerollHit)
    print("Number of wounds:", calculation.calculateWounds(Hits, str, toughness, rerollWound))
    Wounds = calculation.calculateWounds(Hits, str, toughness, rerollWound)
    print("Number of succesfull saves:", calculation.calculateSaveType(Wounds, armor, invu, ap))
    savesMade = calculation.calculateSaveType(Wounds, armor, invu, ap)
    print("Initial damage:", calculation.calculateDamage(Wounds, damage, savesMade))
    damageDone = calculation.calculateDamage(Wounds, damage, savesMade)
    print("After FnP:", calculation.calculateFNP(damageDone, fnp))





  
# radiobuttons below are for determining rerolls for calculation 

r4 = 0
value = 1
for label in labels4:
    tk.Radiobutton(text = label, variable = var, value = value).grid(row = 7, column = r4) 
    value = value +1
    r4 = r4 +1
    


r5 = 0
value2 = 1
for label in labels5:
    tk.Radiobutton(text = label, variable = var1, value = value2).grid(row = 8, column = r5) 
    value2 = value2 +1
    r5 = r5 +1

# checkbutton to mark attack as poisoned     
   
tk.Checkbutton(text = "Poison attack", variable = poisonVar, onvalue = 1, offvalue = 0).grid(row = 8, column = 3)  
calculateButton = tk.Button(text = "Calculate hits", command = calculateButtonCB).grid(row = 11, column = 1)



root.mainloop()