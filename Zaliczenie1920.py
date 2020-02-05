import tkinter, sys
from tkinter import filedialog
import pandas as pd
main = tkinter.Tk()
var = tkinter.StringVar(main)
# Otwarcie pliku z przedmiotami
def openfile():
    var = tkinter.StringVar(main)
    filename = filedialog.askopenfilename(parent=main)
    df = pd.read_excel(filename)
    df = df.to_numpy()
    print (df)
    #DrpDwn['menu'].delete(0, 'end')
    DrpDwn["menu"].delete(0, "end")
    for i in range(0,df.shape[0]):
        print(df[i][0])
        #command = tkinter._setit(var, df[i][0], find_board_info)
        #DrpDwn['menu'].add_command(label=df[i][0], command=command)
        DrpDwn['menu'].add_command(label=df[i][0]
                                   , command = selection(var))
def selection(name):
    var.set(name)
    print(name)
# Zakończenie pracy programu
def finishHim():
    sys.exit()

#def zmiana():
# Stworzenie labelu

Lab = tkinter.Label(main, text = "Test")
Lab.pack()
# Open file

menubar = tkinter.Menu(main)
filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=main.quit)
menubar.add_cascade(label="File", menu=filemenu)

# Drop down lista

variable = tkinter.StringVar(main)
variable.set("wybierz produkt")
DrpDwn = tkinter.OptionMenu(main, variable, "Otworz plik")
DrpDwn.pack()

# Przycisk zakończenia pracy bez zapisania
Koniec = tkinter.Button(main, text = "Zakończ", command = finishHim)
Koniec.pack()


main.config(menu=menubar)
main.mainloop()