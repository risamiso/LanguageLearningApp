import tkinter as tk
import tkinter.font as tkFont
import random
import randomRangeSetter
import scaling as s

yPlace = 379
globCentLabels = []
def createCenterLabels(mainWindow, lines):
    global globCentLabels
    centerLabels = [tk.Label(mainWindow, text = f"{i}", bg = "white", fg="black", font=("Arial", s.scaleSize(17)), anchor = "w", wraplength=533) for i in range(3)] #wraplength does so that after 700 px of text it starts a new line
    globCentLabels = centerLabels
    for i in range(3):
        centerLabels[i].place(x = s.scaleSize(i*501 + 58), y = s.scaleSize(yPlace))
    x = random.randint(randomRangeSetter.clampOne, randomRangeSetter.clampTwo)

    rndStr = lines[x]


    words = []
    words.append(rndStr[:25].strip(" 1234567890.\n"))
    words.append(rndStr[25:53].strip(" "))
    words.append(rndStr[53:].strip(" \n"))

    while words[0] == "" and words[1] == "" and words[2] == "":
        x = random.randint(randomRangeSetter.clampOne, randomRangeSetter.clampTwo)
        rndStr = lines[x]

        words[0] = rndStr[:25].strip(" 1234567890.\n")
        words[1] = rndStr[25:53].strip(" ")
        words[2] = rndStr[53:].strip(" \n1234567890")



    
    for string in range(3):
        centerLabels[string].config(text = words[string], font=("Arial", s.scaleSize(25), "bold"), bg = "#F0E4D3")

def destroyCenterLabels():
    for i in range(3):
        globCentLabels[i].place_forget()


globNextButton = None #next random word Button
def createButtonNextWord(mainWindow, tk): #creating next random word Button
    global globNextButton

    nxtButton = tk.Button(mainWindow, relief="flat", command = rndWord)
    nxtButton.configure(bg = "#a0d3cd")
    nxtButton.place(x = s.scaleSize(1391), y = s.scaleSize(550), width = s.scaleSize(171), height = s.scaleSize(93))

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
        words[0] += " " + glbLines[x + 1][:25]
        words[1] += " " + glbLines[x + 1][25:53]
        if "----" not in glbLines[x + 1]:
            words[2] += " " + glbLines[x + 1][53:]
            words[2] = words[2].strip("-")
        else:
            break

    while words[0] == "" and words[1] == "" and words[2] == "":
        x = random.randint(randomRangeSetter.clampOne, randomRangeSetter.clampTwo)
        rndStr = glbLines[x]

        words[0] = rndStr[:25].strip(" 1234567890.\n")
        words[1] = rndStr[25:53].strip(" ")
        words[2] = rndStr[53:].strip(" \n1234567890")


    
    for string in range(3):
        globCentLabels[string].config(text = words[string], font=("Arial", s.scaleSize(25), "bold"), bg = "#F0E4D3")

glbPanelAbBel = [[], [], []]
glbBGPanels = []
def createBackgroundFrames(mainWindow, tk):
    global glbPanelAbBel, glbBGPanels
    pan1 = tk.Frame(mainWindow, bg = "#F0E4D3", width = 559, height = 191)
    pan1.place(x = 0, y = s.scaleSize(300))
    panAb1 = tk.Frame(mainWindow, bg = "#d6b688", width = 559, height = 11)
    panAb1.place(x = 0, y = s.scaleSize(300))
    panBel1 = tk.Frame(mainWindow, bg = "#d6b688", width = 559, height = 11)
    panBel1.place(x = 0, y = s.scaleSize(480))
    pan1.lower()

    pan2 = tk.Frame(mainWindow, bg = "#F0E4D3", width = 495, height = 191)
    pan2.place(x = s.scaleSize(559), y = s.scaleSize(300))
    panAb2 = tk.Frame(mainWindow, bg = "#d6b688", width = 495, height = 11)
    panAb2.place(x = s.scaleSize(559), y = s.scaleSize(300))
    panBel2 = tk.Frame(mainWindow, bg = "#d6b688", width = 495, height = 11)
    panBel2.place(x = s.scaleSize(559), y = s.scaleSize(480))
    pan2.lower()

    pan3 = tk.Frame(mainWindow, bg = "#F0E4D3", width = 701, height = 191)
    pan3.place(x = s.scaleSize(1054), y = s.scaleSize(300))
    panAb3 = tk.Frame(mainWindow, bg = "#d6b688", width = 701, height = 11)
    panAb3.place(x = s.scaleSize(1054), y = s.scaleSize(300))
    panBel3 = tk.Frame(mainWindow, bg = "#d6b688", width = 701, height = 11)
    panBel3.place(x = s.scaleSize(1054), y = s.scaleSize(480))
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

def createPanelAbove(mainWindow, tk):
    global panelAbove1
    panelAbove = tk.Frame(
    mainWindow,
    bg= "#FFA4A4",
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
    canvas.place(x = s.scaleSize(widthOfWindow - 51), y = s.scaleSize(150))
    thumb.place(x = s.scaleSize(widthOfWindow - 46), y = s.scaleSize(thumbplace))
    for i in range(16):
        listWithMarks[i].place(x = s.scaleSize(widthOfWindow - 46), y = s.scaleSize(155 + i*31))
        listWithMarks[i].lower(thumb)



glbDtschTaste = None
glbEngTaste = None
glbRusTaste = None
def languageButtons(mainWindow, tk):
    global glbDtschTaste, glbEngTaste, glbRusTaste
    dtschButton = tk.Button(mainWindow, relief="flat", command = lambda: hideWord(0))
    dtschButton.configure(bg = "#a0d3cd")
    dtschButton.place(x = s.scaleSize(31), y = s.scaleSize(171), width = s.scaleSize(191), height = s.scaleSize(113))

    engButton = tk.Button(mainWindow, relief="flat", command = lambda: hideWord(1))
    engButton.configure(bg = "#a0d3cd")
    engButton.place(x = s.scaleSize(561), y = s.scaleSize(171), width = s.scaleSize(191), height = s.scaleSize(113))

    rusButton = tk.Button(mainWindow, relief="flat", command = lambda: hideWord(2))
    rusButton.configure(bg = "#a0d3cd")
    rusButton.place(x = s.scaleSize(1071), y = s.scaleSize(171), width = s.scaleSize(191), height = s.scaleSize(113))

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
        globCentLabels[wordToHide].place(x = s.scaleSize(wordToHide*501 + 58), y = s.scaleSize(379))

        glbPanelAbBel[wordToHide][0].place(x = s.scaleSize(barsPositions[wordToHide][0][0]), y = s.scaleSize(barsPositions[wordToHide][0][1]))
        glbPanelAbBel[wordToHide][1].place(x = s.scaleSize(barsPositions[wordToHide][1][0]), y = s.scaleSize(barsPositions[wordToHide][1][1]))

        glbBGPanels[wordToHide].config(bg = "#F0E4D3")

barsPositions = [[(0, 300), (0, 480)], [(559, 300), (559, 480)], [(1054, 300), (1054, 480)]]
