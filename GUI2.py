import tkinter as tk

root = tk.Tk()

labels1 = ["Unit name", "Wounds", "Toughness", "Model count", "Armor save", "Inv. save", "FnP"]
labels2 = ["Weapon name", "Damage", "Strength", "Model count", "Armor piercing", "No. of attacks"]
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
    tk.Entry().grid(row = r2, column = 3)
    r2 = r2 +1

r3 = 0
for label in labels3:
    tk.Button(text = label).grid(row = 10, column = r3)
    r3 = r3 +1

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


root.mainloop()