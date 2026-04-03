import tkinter as tk
import thirdWheel as tw

def initialSetLabels(labels):
    linesToSet = tw.lines[0: 11]
    for i in range(11): # initially setting labels
        for j in range(3):
            labels[i][j].place(x = 31 + 370*j, y = 141 + i*50)


        linesToSet = tw.lines[0: 11]
        words = []
        if(linesToSet[i] == "\n"):
            words.append("")
        else:
            words.append(linesToSet[i][:25].strip(" "))
        words.append(linesToSet[i][25:53].strip(" "))
        words.append(linesToSet[i][53:].strip(" \n"))

        for word in range(3):
            labels[i][word].config(text = words[word])
            
def initialSetLabelsColour(currentString, labels):
    for i in range(11): #change all label's background to none except for current one
        if i == currentString:
            continue
        if i % 2 == 0:
            for j in range(3):
                labels[i][j].config(bg = "#FCF9EA")
        else:
            for j in range(3):
                labels[i][j].config(bg = "#F0E4D3")

    for i in range(3): #change current label background to string's
        labels[currentString][i].config(bg = "#FFBDBD")


def zebraHide(zebraFrames):
    for i in range(11):
        zebraFrames[i].place_forget()

def zebraPlace(zebraFrames, wholeStringHighlight):
    for i in range(11):
        zebraFrames[i].place(x = 0, y = 137 + 50*i)
        zebraFrames[i].lower(wholeStringHighlight)


panelAbove1 = None
def createPanelAbove(mainWindow, tk):
    global panelAbove1
    panelAbove = tk.Frame( #creates panel above
    mainWindow,
    bg= "#FFA4A4",
    width=1711,
    height=131
    )
    panelAbove.place(x=0, y=0)
    panelAbove1 = panelAbove

def changeColour(colour = "#111111"):
    panelAbove1.config(bg = colour)