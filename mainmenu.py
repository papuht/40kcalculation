import tkinter as tk



def openUnitInsert():
    import unitInsertGUI as uiGUI
    
    

top = tk.Tk()
top.title("Cheat spirit")

menubar = tk.Menu(top)

file = tk.Menu(menubar, tearoff = 0)



insert = tk.Menu(file, tearoff = 0)
insert.add_command(label = "Insert units", command = openUnitInsert)
insert.add_command(label = "Insert melee weapons")
insert.add_command(label = "Insert ranged weapons")
insert.add_command(label = "Insert factions")

search = tk.Menu(file, tearoff = 0)
search.add_command(label = "Search units")
search.add_command(label = "Search melee weapons")
search.add_command(label = "Search ranged weapons")


file.add_cascade(label = "Insert into database...", menu = insert)
file.add_cascade(label = "Search from database", menu = search)
file.add_command(label = "Calculate results")


file.add_separator()
file.add_command(label = "Exitus", command = top.quit)

menubar.add_cascade(label="File", menu=file)



 
top.config(menu = menubar)
top.mainloop()  