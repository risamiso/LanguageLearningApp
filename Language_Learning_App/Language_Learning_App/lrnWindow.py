import tkinter as tk
import tkinter.font as tkFont
import random
import randomRangeSetter

yPlace = 379
globCentLabels = []
def createCenterLabels(mainWindow, lines):
    global globCentLabels
    centerLabels = [tk.Label(mainWindow, text = f"{i}", bg = "white", fg="black", font=("Arial", 17), anchor = "w", wraplength=533) for i in range(3)] #wraplength does so that after 700 px of text it starts a new line
    globCentLabels = centerLabels
    for i in range(3):
        centerLabels[i].place(x = i*501 + 58, y = yPlace)
    x = random.randint(randomRangeSetter.clampOne, randomRangeSetter.clampTwo)

    rndStr = lines[x]

    print("Random String is ", rndStr)

    words = []
    words.append(rndStr[:25].strip(" 1234567890.\n"))
    words.append(rndStr[25:53].strip(" "))
    words.append(rndStr[53:].strip(" \n"))

    while("----" in words[2]):
        print("aoijfaiosj")
        break

    while words[0] == "" and words[1] == "" and words[2] == "":
        x = random.randint(randomRangeSetter.clampOne, randomRangeSetter.clampTwo)
        rndStr = lines[x]

        words[0] = rndStr[:25].strip(" 1234567890.\n")
        words[1] = rndStr[25:53].strip(" ")
        words[2] = rndStr[53:].strip(" \n1234567890")

        while("----" in words[2]):
            print("aoijfaiosj")
            break


    
    for string in range(3):
        centerLabels[string].config(text = words[string], font=("Arial", 25, "bold"), bg = "#F0E4D3")

def destroyCenterLabels():
    for i in range(3):
        globCentLabels[i].place_forget()


globNextButton = None #next random word Button
def createButtonNextWord(mainWindow, tk): #creating next random word Button
    global globNextButton

    nxtButton = tk.Button(mainWindow, relief="flat", command = rndWord)
    nxtButton.configure(bg = "#a0d3cd")
    nxtButton.place(x = 1391, y = 550, width = 171, height = 93)

    globNextButton = nxtButton


def destroyButtonNextWord(): #hiding next random word Button
    globNextButton.place_forget()

def rndWord():
    global yPlace

    x = random.randint(randomRangeSetter.clampOne, randomRangeSetter.clampTwo)
    rndStr = glbLines[x]

    words = []
    words.append(rndStr[:25].strip(" 1234567890.\n"))
    words.append(rndStr[25:53].strip(" "))
    words.append(rndStr[53:].strip(" \n1234567890"))
    while("----" in words[2]):
        print("first rndWord")
        words[0] += " " + glbLines[x + 1][:25]
        words[1] += " " + glbLines[x + 1][25:53]
        words[2] += " " + glbLines[x + 1][53:]
        words[2] = words[2].strip("-")

    while words[0] == "" and words[1] == "" and words[2] == "":
        x = random.randint(randomRangeSetter.clampOne, randomRangeSetter.clampTwo)
        rndStr = glbLines[x]

        words[0] = rndStr[:25].strip(" 1234567890.\n")
        words[1] = rndStr[25:53].strip(" ")
        words[2] = rndStr[53:].strip(" \n1234567890")


    
    for string in range(3):
        globCentLabels[string].config(text = words[string], font=("Arial", 25, "bold"), bg = "#F0E4D3")

    print("We're working with: ", globCentLabels[2]["text"])

    if "\n" in globCentLabels[2]["text"]:
        print("yPlace")
        yPlace -= 30
    globCentLabels[2].place(x = 1060, y = yPlace)
    yPlace = 379

glbPanelAbBel = [[], [], []]
glbBGPanels = []
def createBackgroundFrames(mainWindow, tk):
    global glbPanelAbBel, glbBGPanels
    pan1 = tk.Frame(mainWindow, bg = "#F0E4D3", width = 559, height = 191)
    pan1.place(x = 0, y = 300)
    panAb1 = tk.Frame(mainWindow, bg = "#d6b688", width = 559, height = 11)
    panAb1.place(x = 0, y = 300)
    panBel1 = tk.Frame(mainWindow, bg = "#d6b688", width = 559, height = 11)
    panBel1.place(x = 0, y = 480)
    pan1.lower()

    pan2 = tk.Frame(mainWindow, bg = "#F0E4D3", width = 495, height = 191)
    pan2.place(x = 559, y = 300)
    panAb2 = tk.Frame(mainWindow, bg = "#d6b688", width = 495, height = 11)
    panAb2.place(x = 559, y = 300)
    panBel2 = tk.Frame(mainWindow, bg = "#d6b688", width = 495, height = 11)
    panBel2.place(x = 559, y = 480)
    pan2.lower()

    pan3 = tk.Frame(mainWindow, bg = "#F0E4D3", width = 701, height = 191)
    pan3.place(x = 1054, y = 300)
    panAb3 = tk.Frame(mainWindow, bg = "#d6b688", width = 701, height = 11)
    panAb3.place(x = 1054, y = 300)
    panBel3 = tk.Frame(mainWindow, bg = "#d6b688", width = 701, height = 11)
    panBel3.place(x = 1054, y = 480)
    pan3.lower()

    panAbBel = [[], [], []]
    panAbBel[0].append(panAb1)
    panAbBel[0].append(panBel1)
    panAbBel[1].append(panAb2)
    panAbBel[1].append(panBel2)
    panAbBel[2].append(panAb3)
    panAbBel[2].append(panBel3)

    bgPanels = []
    bgPanels.append(pan1)
    bgPanels.append(pan2)
    bgPanels.append(pan3)

    glbBGPanels = bgPanels

    glbPanelAbBel = panAbBel


def destroyBackgroundFrames():
    global glbPanelAbBel
    for i in range(3):
        glbBGPanels[i].place_forget()
        for j in range(2):
            glbPanelAbBel[i][j].place_forget()


glbLines = []
def getLines(lines): #getting lines
    global glbLines

    glbLines = lines

globMainWindow = None
def getMainWindow(mainWindow): #getting mainWindow
    global globMainWindow
    globMainWindow = mainWindow

def createPanelAbove(mainWindow, tk):#, color = "#FFA4A4"):
    global panelAbove1
    panelAbove = tk.Frame( #creates panel above
    mainWindow,
    bg= "#FFA4A4",#color,
    width=1711,
    height=131
    )
    panelAbove.place(x=0, y=0)
    panelAbove1 = panelAbove

def hideScrollThings(canvas, listWithMarks, thumb):
    canvas.place_forget()
    for i in range(16):
        listWithMarks[i].place_forget()
    thumb.place_forget()

def showScrollThings(canvas, listWithMarks, thumb, widthOfWindow, thumbplace):
    canvas.place(x = widthOfWindow - 51, y = 150)
    print("Thumbplace is ", thumbplace)
    thumb.place(x = widthOfWindow - 46, y = thumbplace)
    for i in range(16):
        listWithMarks[i].place(x = widthOfWindow - 46, y = 155 + i*31)
        listWithMarks[i].lower(thumb)



glbDtschTaste = None
glbEngTaste = None
glbRusTaste = None
def languageButtons(mainWindow, tk):
    global glbDtschTaste, glbEngTaste, glbRusTaste
    dtschButton = tk.Button(mainWindow, relief="flat", command = lambda: hideWord(0)) #lambda: somehow assures that I can add parameters to function
    dtschButton.configure(bg = "#a0d3cd")
    dtschButton.place(x = 31, y = 171, width = 191, height = 113)

    engButton = tk.Button(mainWindow, relief="flat", command = lambda: hideWord(1))
    engButton.configure(bg = "#a0d3cd")
    engButton.place(x = 561, y = 171, width = 191, height = 113)

    rusButton = tk.Button(mainWindow, relief="flat", command = lambda: hideWord(2))
    rusButton.configure(bg = "#a0d3cd")
    rusButton.place(x = 1071, y = 171, width = 191, height = 113)

    glbDtschTaste = dtschButton
    glbEngTaste = engButton
    glbRusTaste = rusButton

def hidelanguageButtons():
    glbDtschTaste.place_forget()
    glbEngTaste.place_forget()
    glbRusTaste.place_forget()

def hideWord(wordToHide):
    if globCentLabels[wordToHide].winfo_ismapped(): #checks if button is visible
            globCentLabels[wordToHide].place_forget()
            glbPanelAbBel[wordToHide][0].place_forget()
            glbPanelAbBel[wordToHide][1].place_forget()

            glbBGPanels[wordToHide].config(bg = "#FFA4A4")
    else:
        globCentLabels[wordToHide].place(x = wordToHide*501 + 58, y = 379)

        glbPanelAbBel[wordToHide][0].place(x = barsPositions[wordToHide][0][0], y = barsPositions[wordToHide][0][1])
        glbPanelAbBel[wordToHide][1].place(x = barsPositions[wordToHide][1][0], y = barsPositions[wordToHide][1][1])

        glbBGPanels[wordToHide].config(bg = "#F0E4D3")

barsPositions = [[(0, 300), (0, 480)], [(559, 300), (559, 480)], [(1054, 300), (1054, 480)]]
