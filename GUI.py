import tkinter

root = tkinter.Tk()



unitnameLabel = tkinter.Label(root, text = "Unit name")
unitnameField = tkinter.Entry(root)

unitwoundLabel = tkinter.Label(root, text = "Wounds")
unitwoundField = tkinter.Entry(root)

unittoughLabel = tkinter.Label(root, text = "Toughness")
unittoughField = tkinter.Entry(root)

unitstrLabel = tkinter.Label(root, text = "Strength")
unitstrField = tkinter.Entry(root)

unitmodelLabel = tkinter.Label(root, text = "Model count")
unitmodelField = tkinter.Entry(root)


modelCount = unitmodelField.get()
str = unitstrField.get()
tough = unittoughField.get()
wounds = unitwoundField.get()
name = unitnameField.get()


weaponNameLabel = tkinter.Label(root, text = 'Weapon name')
weaponNameEntry = tkinter.Entry(root)
 
weaponSLabel = tkinter.Label(root, text = 'Weapon Strength')
weaponSEntry = tkinter.Entry(root)

weaponBSLabel = tkinter.Label(root, text = "Ballistic skill")
weaponBSEntry = tkinter.Entry(root)
 
weaponAPLabel = tkinter.Label(root, text = 'AP')
weaponAPEntry = tkinter.Entry(root)
 
weaponALabel = tkinter.Label(root, text = '# of shots')
weaponAEntry = tkinter.Entry(root)

weaponDamageLabel = tkinter.Label(root, text = "Damage")
weaponDamageEntry = tkinter.Entry(root)

 

def rerollSelect():
    sel = var.get()
    
 
var = tkinter.IntVar() 
RR1 = tkinter.Radiobutton(root, text = "Re-roll to-hit 1's", variable = var, value = 1, command = rerollSelect)
RR2 = tkinter.Radiobutton(root, text = "Re-roll to-hit all", variable = var, value = 2, command = rerollSelect)
RR3 = tkinter.Radiobutton(root, text = "No re-rolls to-hit", variable = var, value = 3, command = rerollSelect)  

poisonVar = tkinter.IntVar()
Poison = tkinter.Checkbutton(root, text = "Poison attack", variable = poisonVar, onvalue = 1, offvalue = 0)   

def rerollWoundSelect():
    sel = var2.get()

var2 = tkinter.IntVar()
RRW1 = tkinter.Radiobutton(root, text = "Re-roll to wound 1's", variable = var2, value = 1, command = rerollWoundSelect) 
RRW2 = tkinter.Radiobutton(root, text = "Re-roll all to wound", variable = var2, value = 2, command = rerollWoundSelect) 
RRW3 = tkinter.Radiobutton(root, text = "No re-rolls to wound", variable = var2, value = 3, command = rerollWoundSelect) 
    
 
def printWeaponData():
    print('Weapon name: ' + weaponNameEntry.get(), 'Weapon Strength: ' + weaponSEntry.get(), 'Ballistic skill' + weaponBSEntry.get(), 'AP: ' + weaponAPEntry.get(), '# of shots: ' + weaponAEntry.get())


def printData ():
    print("Name: " + unitnameField.get(), "Wounds:" + unitwoundField.get(), "Strength:" + unitstrField.get(), "Toughness:" + unittoughField.get(), "Model count:" + unitmodelField.get())

printbutton = tkinter.Button(root, text = "Print unit data", command = printData)  

printWeaponButton = tkinter.Button(root, text = 'Print weapon data', command = printData)



unitnameLabel.pack()
unitnameField.pack()
unittoughLabel.pack()
unittoughField.pack()
unitwoundLabel.pack()
unitwoundField.pack()
unitstrLabel.pack()
unitstrField.pack()
unitmodelLabel.pack()
unitmodelField.pack()

printbutton.pack()

weaponNameLabel.pack()
weaponNameEntry.pack()
 
weaponSLabel.pack()
weaponSEntry.pack()

weaponBSLabel.pack()
weaponBSEntry.pack()
 
weaponAPLabel.pack()
weaponAPEntry.pack()
 
weaponALabel.pack()
weaponAEntry.pack()

weaponDamageLabel.pack()
weaponDamageEntry.pack()

RR1.pack()
RR2.pack()
RR3.pack()

RRW1.pack()
RRW2.pack()
RRW3.pack()

Poison.pack()

printWeaponButton.pack()

root.mainloop()