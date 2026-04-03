import tkinter as tk
import thirdWheel


class TextFrame(tk.Frame):
    def __init__(self, mainWindow, text, **otherStuff):
        super().__init__(mainWindow, **otherStuff)

        self.label = tk.Label(self, text=text, bg=self["bg"], font = ("Happy Festive", 30), fg = "yellow")
        self.label.pack()


clampOne = 0
clampTwo = 0

clampOneFrame = None
clampTwoFrame = None
smallVioletSquare = None

setToDefault = True
def createClampButton(mainWindow):
    clampButton = tk.Button(mainWindow, bg = "#722ec9", text = "C", font = ("Happy Festive", 72), fg = "yellow", command = lambda: putClamps(mainWindow))
    clampButton.place(x = 270, y = 17, width = 91, height = 91)

alreadyClicked = False

clampersAreOn = False

def putClamps(mainWindow):

    if thirdWheel.currentUI != "mainUI":
        return

    global setToDefault, clampOne, clampTwo, clampOneFrame, clampTwoFrame, alreadyClicked, smallVioletSquare
    
    if smallVioletSquare is None:

        if clampOneFrame is None:
            clampOneFrame = TextFrame(mainWindow, text = "1", bg = "#722ec9")
        if clampTwoFrame is None:
            clampTwoFrame = TextFrame(mainWindow, text = "2", bg = "#722ec9")
        if smallVioletSquare is None:
            smallVioletSquare = tk.Frame(mainWindow, bg = "#a531ce")
            smallVioletSquare.place(x = 631, y = 83, height = 20, width = 20)


        placeForOne = clampOne - thirdWheel.displayStartLine
        placeForTwo = clampTwo - thirdWheel.displayStartLine

        if clampOne >= thirdWheel.displayStartLine and clampOne <= thirdWheel.displayStartLine + 10:
            clampOneFrame.place(x = 0, y = 137 + 50*placeForOne, width = 34, height = 41)
        if clampTwo >= thirdWheel.displayStartLine and clampTwo <= thirdWheel.displayStartLine + 10:
            clampTwoFrame.place(x = 0, y = 137 + 50*placeForTwo, width = 34, height = 41)

    elif smallVioletSquare is not None:
        alreadyClicked = False

        clampOneFrame.place_forget()
        clampTwoFrame.place_forget()

        smallVioletSquare.destroy()
        smallVioletSquare = None

def hideClamps():
    global smallVioletSquare
    if smallVioletSquare is not None:
        alreadyClicked = False

        clampOneFrame.place_forget()
        clampTwoFrame.place_forget()

        smallVioletSquare.destroy()
        smallVioletSquare = None


def dinamicUpdateClamps():
    global placeForOne, placeForTwo, clampOne, clampTwo

    if smallVioletSquare is None:
        return


    placeForOne = clampOne - thirdWheel.displayStartLine
    placeForTwo = clampTwo - thirdWheel.displayStartLine

    if clampOne >= thirdWheel.displayStartLine and clampOne <= thirdWheel.displayStartLine + 10:
        clampOneFrame.place(x = 0, y = 137 + 50*placeForOne, width = 34, height = 41)
    else:
        clampOneFrame.place(x = -100, y = 0)
    if clampTwo >= thirdWheel.displayStartLine and clampTwo <= thirdWheel.displayStartLine + 10:
        clampTwoFrame.place(x = 0, y = 137 + 50*placeForTwo, width = 34, height = 41)
    else:
        clampTwoFrame.place(x = -100, y = 0)

def setNewClampersFirst(event):
    global clampOne
    if smallVioletSquare is None or thirdWheel.currentUI != "mainUI":
        return

    if thirdWheel.textString < clampTwo:
        clampOne = thirdWheel.textString
        dinamicUpdateClamps()

def setNewClampersSecond(event):
    global clampTwo
    if smallVioletSquare is None or thirdWheel.currentUI != "mainUI":
        return
    if thirdWheel.textString > clampOne:
        clampTwo = thirdWheel.textString
        dinamicUpdateClamps()


clamperLines = []
def getLines(lines): #I update it in redactText every time change is done
    global clamperLines, setToDefault, clampOne, clampTwo

    clamperLines = lines

    if setToDefault:
        clampOne = 11
        clampTwo = len(clamperLines) - 1
        setToDefault = False
