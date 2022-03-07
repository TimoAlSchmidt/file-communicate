import tkinter, json, os
from tkinter import ttk
from tkinter.messagebox import showinfo
from datetime import datetime

window = tkinter.Tk()
window.title('Database demo')
window.geometry('620x400')
stringvar = tkinter.StringVar()

def refreshContacts():
    global contacts, stringvar
    
    content = os.listdir('databron')
    contacts = []
    latest = 0
    for filename in content:
        file = open("databron/"+filename, "r")
        info = file.read()
        infor = json.loads(info)
        contacts.append((infor["Naam"], infor["Leeftijd"], infor["Geslacht"]))
        latest = max(latest, os.path.getmtime("databron/"+filename))

    tree.delete(*tree.get_children())    
    # add data to the treeview
    for contact in contacts:
        tree.insert('', tkinter.END, values=contact)
    
    stringvar.set("Latest Modified: "+str(datetime.fromtimestamp(latest).strftime("%A, %B %d, %Y %I:%M:%S")))



columns = ('Naam', 'Leeftijd', 'Geslacht')

tree = ttk.Treeview(window, columns=columns, show='headings')

tree.heading('Naam', text='Naam')
tree.heading('Leeftijd', text='Leeftijd')
tree.heading('Geslacht', text='Geslacht')

# generate sample data


contacts = []

refreshContacts()


tree.grid(row=0, column=0, sticky='nsew')

# add a scrollbar
scrollbar = ttk.Scrollbar(window, orient=tkinter.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

button = ttk.Button(window,text="Verversen",command=refreshContacts)
button.grid(row=2,column=0, sticky='ns')


label = ttk.Label(window, textvariable = stringvar)
label.grid(row=3,column=0)

# run the app
window.mainloop()
