import tkinter as tk
import pandas as pd
import random as rd

main = tk.Tk()
filename="C:\\Users\\Zabawny Komputer\\Documents\\Python Scripts\\slowa.xlsx"
df = pd.read_excel(filename)
df = df.to_numpy()
global ukryteslowo
global polukryte
global bledneliterki
ukryteslowo = ""
polukryte = ""
bledneliterki = ""
# Wyzeruj ustawienia
def abc():
    ukryteslowo = startgame()
def startgame():
    global ukryteslowo
    missings = ""
    rnd = round(rd.random()*df.shape[0])
    ukryteslowo = df[rnd][0]
    print(ukryteslowo)
    for i in range(0,len(ukryteslowo)):
        missings = missings + "_ "
    cel.config(text=missings)
    l3.config(text="Błędne literki: ")
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    l5.config(text="")

def checkletter():
    l5.config(text="")
    global bledneliterki
    literka = e1.get()
    #bledneliterki = l3.
    if len(literka)!=1:
        l5.config(text="Wpisz jedną literkę!")
    else:
        if ukryteslowo.lower().find(literka.lower()) >= 0:
            whereismyletter = ukryteslowo.rfind(literka)
            while whereismyletter != 0:

            e1.delete(0, 'end')
        else:
            bledneliterki =  bledneliterki + literka + ";"
            l3.config(text="Błędne literki: " + bledneliterki)
            e1.delete(0, 'end')

def checkslowo():
    slowo = e2.get()
    global ukryteslowo
    if slowo == ukryteslowo and slowo != "":
        l5.config(text="Brawo! Twoje słowo to " + str(slowo))
        e1.delete(0, 'end')
        e2.delete(0, 'end')
        cel.config(text=slowo)
    elif slowo=="":
        l5.config(text="Wprowadź słowo!")
    else:
        l5.config(text="Niestety " + str(slowo) + " to nie rozwiązanie")

#Ustawianie labeli
l1 = tk.Label(main, text = "Wprowadź literkę")
l2 = tk.Label(main, text = "Wprowadź słowo")
l3 = tk.Label(main, text = "Błędne literki: ")
l4 = tk.Label(main, text = "Ukryte słowo:")
l5 = tk.Label(main, text = "")
cel = tk.Label(main, text = "")
l1.grid(row = 0, column = 0, sticky = tk.W, pady = 2)
l2.grid(row = 1, column = 0, sticky = tk.W, pady = 2)
l3.grid(row = 2, column = 0, sticky = tk.W, pady = 2)
l4.grid(row = 0, column = 3, sticky = tk.W, pady = 2)
l5.grid(row = 2, column = 3, sticky = tk.W, pady = 2)
cel.grid(row = 1, column = 3, sticky = tk.W, pady = 2)

#ustawianie literek i słów
e1 = tk.Entry(main)
e2 = tk.Entry(main)
e1.grid(row=0, column=1, pady=2)
e2.grid(row=1, column=1, pady=2)

#Ustawianie przyciskow
b1 = tk.Button(main, text="Reset Gry", command=abc)
b2 = tk.Button(main, text="Sprawdź literkę",command=checkletter)
b3 = tk.Button(main, text="Sprawdź słowo", command=checkslowo)
# arranging button widgets
b1.grid(row=2, column=2, sticky=tk.E)
b2.grid(row=0, column=2, sticky=tk.E)
b3.grid(row=1, column=2, sticky=tk.E)

main.mainloop()