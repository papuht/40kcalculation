import tkinter as tk
import calculation
import attacker


        


root = tk.Tk()



labels1 = ["Unit name", "Wounds", "Toughness", "Model count", "Armor save", "Inv. save", "FnP"]
labels2 = ["Weapon name", "Damage", "Strength", "Model count", "Armor piercing", "No. of attacks", "Ballistic skill"]
labels3 = ["Print unit data", "Print attack data", "Calculate result"]
labels4 = ["Re-roll to hit 1's", "Re-roll to hit all", "No to hit re-rolls"]
labels5 = ["Re-roll to wound 1's", "Re-roll to wound all", "No to wound re-rolls"]
labels6 = ["Poison attack"]

r = 0
for label in labels1:
    tk.Label(text = label).grid(row = r, column = 0)
    tk.Entry().grid(row = r, column = 1)
    r = r +1

r2 = 0    
for label in labels2:
    tk.Label(text = label).grid(row = r2, column = 2)
    r2 = r2 +1

mcVar = tk.StringVar()
attVar = tk.StringVar()
bsVar = tk.StringVar()

wnameEntry = tk.Entry().grid(row = 0, column = 3)
damaEntry = tk.Entry().grid(row = 1, column = 3)
strEntry = tk.Entry().grid(row = 2, column = 3)
mcEntry = tk.Entry(textvariable = mcVar).grid(row = 3, column = 3)
apEntry = tk.Entry().grid(row = 4, column = 3)
noAtEntry = tk.Entry(textvariable = attVar).grid(row = 5, column = 3)
bsEntry = tk.Entry(textvariable = bsVar).grid(row = 6, column = 3)
    
def calculateButtonCB():
    bs = float(bsVar.get())
    att = float(attVar.get())
    mc = float(mcVar.get())
    
    att = attacker.Attacker(bs, att, mc)
    print(calculation.calculateHits(att.getBS(), att.getAtt(), att.getMC()))
    





  

var = tk.IntVar()
r4 = 0
value = 1
for label in labels4:
    tk.Radiobutton(text = label, variable = var, value = value).grid(row = 7, column = r4) 
    value = value +1
    r4 = r4 +1
    

var1 = tk.IntVar()
r5 = 0
value2 = 1
for label in labels5:
    tk.Radiobutton(text = label, variable = var1, value = value2).grid(row = 8, column = r5) 
    value2 = value2 +1
    r5 = r5 +1
    
poisonVar = tk.IntVar()    
tk.Checkbutton(text = "Poison attack", variable = poisonVar, onvalue = 1, offvalue = 0).grid(row = 8, column = 3)  
calculateButton = tk.Button(text = "Calculate hits", command = calculateButtonCB).grid(row = 11, column = 1)



root.mainloop()