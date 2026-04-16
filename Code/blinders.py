import tkinter as tk
import scaling as s

isDClicked = False
isEClicked = False
isRClicked = False

globDBlinder = None
globEBlinder = None
globRBlinder = None

def createBlinders(mainWindow, labels):
    global globDBlinder, globEBlinder, globRBlinder
    def blindD():             #blinding D
        global isDClicked
        if isDClicked == False:
            for i in range(11):
                labels[i][0].place_forget()
            isDClicked = True
        else:
            for i in range(11):
                labels[i][0].place(x = s.scaleSize(31), y = s.scaleSize(141 + i*50))
            isDClicked = False



    def blindE():
        global isEClicked
        if isEClicked == False:
            for i in range(11):
                labels[i][1].place_forget()
            isEClicked = True
        else:
            for i in range(11):
                labels[i][1].place(x = s.scaleSize(401), y = s.scaleSize(141 + i*50))
            isEClicked = False

    def blindR():
        global isRClicked
        if isRClicked == False:
            for i in range(11):
                labels[i][2].place_forget()
            isRClicked = True
        else:
            for i in range(11):
                labels[i][2].place(x = s.scaleSize(771), y = s.scaleSize(141 + i*50))
            isRClicked = False


    dBlinder = tk.Button(mainWindow, relief = "flat", text = "D", font = ("Times New Roman", s.scaleSize(29)), fg = "#56b1a7", command = blindD)
    eBlinder = tk.Button(mainWindow, relief = "flat", text = "E", font = ("Happy Swirly", s.scaleSize(29)), fg = "#56b1a7", command = blindE)
    rBlinder = tk.Button(mainWindow, relief = "flat", text = "R", font = ("Love Days", s.scaleSize(29)), fg = "#56b1a7", command = blindR)

    globDBlinder = dBlinder
    globEBlinder = eBlinder
    globRBlinder = rBlinder

    globDBlinder.configure(bg = "#FCF9EA")
    globEBlinder.configure(bg = "#FCF9EA")
    globRBlinder.configure(bg = "#FCF9EA")

    globDBlinder.place(x = s.scaleSize(1088), y = s.scaleSize(20), width = s.scaleSize(91), height = s.scaleSize(91))
    globEBlinder.place(x = s.scaleSize(1219), y = s.scaleSize(20), width = s.scaleSize(91), height = s.scaleSize(91))
    globRBlinder.place(x = s.scaleSize(1350), y = s.scaleSize(20), width = s.scaleSize(91), height = s.scaleSize(91))




def hideBlinders():
    globDBlinder.place_forget()
    globEBlinder.place_forget()
    globRBlinder.place_forget()
