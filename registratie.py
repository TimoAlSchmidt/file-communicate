import tkinter, yaml, json, os
from tkinter import ttk
from tkinter.messagebox import showinfo, WARNING

window = tkinter.Tk()

window.title("Registratie Formulier")   
window.geometry("250x250")

naam = tkinter.StringVar()
leeftijd = tkinter.StringVar()
geslacht = tkinter.StringVar()


def removeWidgets():
    for widget in window.winfo_children():
        widget.destroy()


def finish():
    if not naam.get() or not leeftijd.get() or not geslacht.get():
        return
    




    removeWidgets()
    naamlabeler = ttk.Label(window, text="Uw naam is {}".format(naam.get()))
    naamlabeler.pack()
    leeftijder = ttk.Label(window, text="U bent {} jaar oud.".format(leeftijd.get()))
    leeftijder.pack()
    geslachter = ttk.Label(window, text="U bent een {}.".format(geslacht.get()))
    geslachter.pack()

    with open("settings.yml", "r") as file:
        settings = yaml.safe_load(file)
    
    diavolo = { settings["one"] : naam.get(), settings["two"] : leeftijd.get(), settings["three"] : geslacht.get()}

    if not os.path.exists("databron"):
        os.mkdir("databron")


    with open("databron/"+naam.get()+leeftijd.get()+geslacht.get()+".json", "a") as file:
        file.write(json.dumps(diavolo))


naamlabel = ttk.Label(window, text="Naam:")
namer = ttk.Entry(window, textvariable=naam)

leeftijdlabel = ttk.Label(window, text="Leeftijd:")
levertijd = ttk.Entry(window, textvariable=leeftijd)

geslachtlabel = ttk.Label(window, text="Geslacht:")


naamlabel.pack()
namer.pack()

leeftijdlabel.pack()
levertijd.pack()

geslachtlabel.pack()
g = ttk.Radiobutton(window, value="Man", text="Man",variable=geslacht)
g.pack()
g = ttk.Radiobutton(window, value="Vrouw", text="Vrouw",variable=geslacht)
g.pack()
g = ttk.Radiobutton(window, value="Anders", text="Anders",variable=geslacht)
g.pack()

btn = ttk.Button(window, command=finish,text="Klaar")

btn.pack()

#Button die Alle ingevulde waardes checken en zo

window.mainloop()