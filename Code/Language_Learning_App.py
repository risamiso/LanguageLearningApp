
import tkinter as tk
import tkinter.font as tkFont #adds fonts, I guess?
import starter
import lrnWindow
import redactText
import changeTextGaps
import thirdWheel as tw #if something went wrong with textString then it's probably because of currentMiddleLine in tw or in setNewLabels in UI change
import searchBar
import blinders
import randomRangeSetter
import scrollBar
import scaling as s #tried making it look decent on all resolutions, but it didn't work out quite well.
import ctypes
import os
import sys

#to do
# 1.fix how long words appear in lrnWindow

ctypes.windll.shcore.SetProcessDpiAwareness(2) #prevents Windows from resizing the window automatically 

#passing fonts
def rightPath(path): #returns the right base path depending on whether I run it from here pc or from .exe file
    try:
        base_path = sys._MEIPASS  # PyInstaller temporary folder
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, path)

font_path = rightPath("fonts/LoveDays-2v7Oee.ttf")
ctypes.windll.gdi32.AddFontResourceExW(font_path, 0x10, 0)
font_path = rightPath("fonts/HappySwirly-KVB7l.ttf")
ctypes.windll.gdi32.AddFontResourceExW(font_path, 0x10, 0)
font_path = rightPath("fonts/HappyFestive-MAYVn.ttf")
ctypes.windll.gdi32.AddFontResourceExW(font_path, 0x10, 0)


mainWindow = tk.Tk()
s.init(mainWindow.winfo_screenwidth(), mainWindow.winfo_screenheight())
mainWindow.title("MiuIueie")
mainWindow.geometry(f"{s.scaleSize(1711)}x{s.scaleSize(701)}")
s.init(mainWindow.winfo_screenwidth(), mainWindow.winfo_screenheight())

mainWindow.configure(bg="#FCF9EA") #changes background colour

lrnWindow.getMainWindow(mainWindow)

with open("WordsWordsWords.txt", "r", encoding = "utf-8") as file: #reads .txt document and returns list where each element is one line of text
    tw.lines = file.readlines()

#changeTextGaps.addGaps(tw.lines) #was initially needed to correct gaps between words in .txt file


randomRangeSetter.getLines(tw.lines)

labelsBackgroundColour = "#FCF9EA" #background colour of labels
labels = [[tk.Label(mainWindow, text = f"{i}", bg = labelsBackgroundColour, fg="#5ab2a9", font=("Arial", s.scaleSize(17)), anchor = "w") for i in range(3)] for _ in range(11)] #creating list of 11 lists, each of them contains 4 Labels. It's like a good thing to write _ but x will do too. Anchor makes the text aligned to the left side.
omB = tw.OmnipresentBeing() #manipulations to pass scrollBarFrame to thirdWheel without importing it
scrollBarFrame = scrollBar.scrollBarr(mainWindow)
omB.getScrollBarObject(scrollBarFrame)
scrollBarFrame.actuallyScroll(mainWindow, labels)


blockMainWindowFunctions = False #blocks functions in main menu

wholeStringHighlight = tk.Frame(mainWindow, bg = "#FFBDBD", width = s.scaleSize(1710), height = s.scaleSize(41)) #creating a background for selected string
wholeStringHighlight.place(x = 0, y = s.scaleSize(tw.currentStringHighlightHeight))
wholeStringHighlight.lower()
labelsBackgroundColour = "#FFBDBD"
for i in range(3): #making the first line pink at the beginning
    labels[0][i].config(bg = labelsBackgroundColour)

zebraFrames = [tk.Frame(mainWindow, bg = "#FCF9EA", width = 1710, height = 41) if i % 2 == 0 else tk.Frame(mainWindow, bg = "#F0E4D3", width = 1710, height = 41) for i in range(11)] #creating brows background lines
for i in range(11):
    zebraFrames[i].place(x = 0, y = s.scaleSize(137 + 50*i))
    zebraFrames[i].lower(wholeStringHighlight)


mainWindow.update_idletasks() #updates parameters of a window(height, width), because they go to 1 after creation for some reason
widthOfWindow = mainWindow.winfo_width() #gets the width of the window
thumbplace = 155
def windowSizeChange(event): #trigers when window is moved or resized so apparantly this thing also runs every time when I click and drag my mouse
    global widthOfWindow
    widthOfWindow = mainWindow.winfo_width() #gets width of a window

def changeUI():
    global blockMainWindowFunctions
    if tw.currentUI == "mainUI":  #going to lrnWindow
        redactText.abruptRedacting(labels, tw.currentString, wholeStringHighlight)
        scrollBarFrame.hideSelf() #this whole thing is just hiding stuff from main UI and creating elements froml lrnWindow
        blockMainWindowFunctions = True
        tw.currentUI = "lrnUI"
        starter.zebraHide(zebraFrames)
        lrnWindow.getLines(tw.lines)
        for i in range(11):
            for j in range(3):
                labels[i][j].place_forget()
        wholeStringHighlight.place_forget()
        lrnWindow.createCenterLabels(mainWindow, tw.lines)
        lrnWindow.createButtonNextWord(mainWindow, tk)
        lrnWindow.createBackgroundFrames(mainWindow, tk)
        lrnWindow.languageButtons(mainWindow, tk)
        blinders.hideBlinders()
        randomRangeSetter.hideClamps()
    else:                                               #going back to main window
        tw.currentUI = "mainUI" #the same but for main UI
        scrollBarFrame.showSelf()
        blockMainWindowFunctions = False
        starter.zebraPlace(zebraFrames, wholeStringHighlight)
        wholeStringHighlight.place(x = 0, y = s.scaleSize(tw.currentStringHighlightHeight))
        starter.initialSetLabels(labels)
        setNewLabels(tw.displayStartLine, tw.displayStartLine + 11)
        lrnWindow.destroyCenterLabels()
        lrnWindow.destroyButtonNextWord()
        lrnWindow.destroyBackgroundFrames()
        lrnWindow.hidelanguageButtons()
        blinders.isDClicked = False
        blinders.isEClicked = False
        blinders.isRClicked = False
        blinders.createBlinders(mainWindow, labels)



currentmode = "deadeyes" # I did not write code for this button
def darkmode():
    global currentmode
    global labelsBackgroundColour
    if currentmode == "deadeyes":
        currentmode = "darkmode"
        modebutton.configure(text = "DO NOT PRESS")
        mainWindow.configure(bg = "#000000")
        starter.changeColour()
        wholeStringHighlight.config(bg = "#C80E0E")
        for i in range(3): #change current label background to string's
            labels[tw.currentString][i].config(bg = "#C80E0E")
        for i in range(11):
            if i % 2 == 0:
                zebraFrames[i].config(bg = "#000000")
                if i == tw.currentString:
                    continue
                for j in range(3):
                    labels[i][j].config(bg = "#000000")
            else:
                zebraFrames[i].config(bg = "#222222")
                if i == tw.currentString:
                    continue
                for j in range(3):
                    labels[i][j].config(bg = "#222222")          

    elif currentmode == "darkmode":
        currentmode = "deadeyes"
        modebutton.configure(text = "save your eyes")
        mainWindow.configure(bg ="#FCF9EA")
        starter.changeColour(colour = "#FFA4A4")
        wholeStringHighlight.config(bg = "#FFBDBD")
        for i in range(3): #change current label background to string's
            labels[tw.currentString][i].config(bg = "#FFBDBD")
        for i in range(11):
            if i % 2 == 0:
                zebraFrames[i].config(bg = "#FCF9EA")
                if i == tw.currentString:
                    continue
                for j in range(3):
                    labels[i][j].config(bg = "#FCF9EA")
            else:
                zebraFrames[i].config(bg = "#F0E4D3")
                if i == tw.currentString:
                    continue
                for j in range(3):
                    labels[i][j].config(bg = "#F0E4D3")



def goDown(event): #go one line down
    global blockMainWindowFunctions

    if blockMainWindowFunctions:
        return

    global wholeStringHighlight
    global bottomIndex
    global upperIndex

    if tw.textString == len(tw.lines) - 1: #makes sure we don't go past last string in .txt
        return

    redactText.abruptRedacting(labels, tw.currentString, wholeStringHighlight) #if line is being redacted, pressing down would stop it

    tw.textString += 1 #incrementing the line that we're on
    if tw.currentString == 10: #if this is the last string
        bottomIndex = tw.textString - 10
        upperIndex = tw.textString + 1
        setNewLabels(bottomIndex, upperIndex)
        return

    if tw.currentString != 10: #makes sure pink line doesn't go lower than last label's height
        tw.currentStringHighlightHeight += 50 #moves pink string
    wholeStringHighlight.place(x = 0, y = s.scaleSize(tw.currentStringHighlightHeight))

    if tw.currentString != 10: #makes sure currentString doesn't go past 10
        tw.currentString += 1 #currentString is for where the pink string is on the screen (0-10), textString is global one (start of .txt - end of .txt)


    changeLabelsBackground()



def goUp(event): #does the same us goDown, but up...
    global blockMainWindowFunctions
    if blockMainWindowFunctions:
        return

    global wholeStringHighlight

    global bottomIndex
    global upperIndex

    if tw.textString == 0: #makes sure we don't go past last string in .txt
        return

    redactText.abruptRedacting(labels, tw.currentString, wholeStringHighlight)

    tw.textString -= 1

    if tw.currentString == 0: #if this is the last string
        bottomIndex = tw.textString
        upperIndex = tw.textString + 11
        setNewLabels(bottomIndex, upperIndex)
        return

    if tw.currentString != 0: #makes sure it doesn't go lower than last label's height
        tw.currentStringHighlightHeight -= 50
    wholeStringHighlight.place(x = 0, y = s.scaleSize(tw.currentStringHighlightHeight))

    if tw.currentString != 0: #makes sure currentString doesn't go past 10
        tw.currentString -= 1

    changeLabelsBackground()


def scroll(event): #scrolling with a mouse wheel.
    global blockMainWindowFunctions
    if blockMainWindowFunctions:
        return
    if(event.delta == -120):
        goDown(event)
    if event.delta == -240:
        goDown(event)
        goDown(event)
    if(event.delta == 120):
        goUp(event)
    if event.delta == 240:
        goUp(event)
        goUp(event)


bottomIndex = 0 #starting values for setNewLabels() function
upperIndex = 11

def setNewLabels(bottomIndex, upperIndex): #changes words on the screen
    tw.displayStartLine = bottomIndex #displayStart line is the index of a line on the top of a screen

    scrollBarFrame.updatePosition(tw.displayStartLine, tw.lines) #each time I update words I as well update the position of a thumb of a scroll bar

    linesToSet = tw.lines[bottomIndex: upperIndex] # list with new lines to show on the screen
    
    for string in range(11):
        words = [] #for each of 11 lines there are 3 words
        if(linesToSet[string] == "\n"):
            words.append("")
        else:
            words.append(linesToSet[string][:25].strip(" \n"))
        words.append(linesToSet[string][25:53].strip(" \n"))
        words.append(linesToSet[string][53:].strip(" \n"))

        for word in range(3):
            labels[string][word].config(text = words[word])

    randomRangeSetter.dinamicUpdateClamps() #updating the clamps' place




def changeLabelsBackground():#upades background of labels. Because it can not be made transparent in tkinter you have to update it manually to match background
    global currentmode
    if currentmode == "deadeyes": 
        for i in range(11): #change all label's background to none except for current one
            if i == tw.currentString: #skip if it's pink line
                continue
            if i % 2 == 0: #for every even nuber make the background 
                for j in range(3):
                    labels[i][j].config(bg = "#FCF9EA") #beige colour
            else:
                for j in range(3):
                    labels[i][j].config(bg = "#F0E4D3") #light brown colour
        for i in range(3): #change current label background to pink
            labels[tw.currentString][i].config(bg = "#FFBDBD")

    elif currentmode == "darkmode": #not responsible for this one
        for i in range(11): #change all label's background to none except for current one
            if i == tw.currentString:
                continue
            if i % 2 == 0:
                for j in range(3):
                    labels[i][j].config(bg = "#000000")#F7EFC7
            else:
                for j in range(3):
                    labels[i][j].config(bg = "#222222")
        for i in range(3): #change current label background to string's
            labels[tw.currentString][i].config(bg = "#C80E0E")


starter.initialSetLabels(labels) # initially setting labels
starter.initialSetLabelsColour(tw.currentString, labels) # initially setting labels' colours
starter.createPanelAbove(mainWindow, tk) #creating the thing above
searchBar.createSearchBar(mainWindow) #creating searchBar
searchBar.createSquareBehindSearchBar(mainWindow) #creating pink frame for search bar
blinders.createBlinders(mainWindow, labels) #creating buttons for blinders
randomRangeSetter.createClampButton(mainWindow) #creating clamps Button



rndWordsButton = tk.Button(mainWindow, bg = "#FCF9EA", relief="flat", command = changeUI) #for going to lrnUI
rndWordsButton.place(x = s.scaleSize(21), y = s.scaleSize(17), width = s.scaleSize(93), height = s.scaleSize(93))

modebutton = tk.Button(mainWindow, command = darkmode)         #darkmode changer
modebutton.configure(bg = "#FF0000", text = "save your eyes")
modebutton.place(x = s.scaleSize(150), y = s.scaleSize(17), width = s.scaleSize(93), height = s.scaleSize(93))


mainWindow.bind("<Down>", goDown) #this whole section is just binding functions to keys
mainWindow.bind("<Up>", goUp)
mainWindow.bind("<MouseWheel>", scroll)

mainWindow.bind("<Configure>", windowSizeChange) #triggers every time window size is changed

def redact(event): #needed this to trigger it for both latin R and cyrillic K
    if event.char in ("R", "К"):
        redactText.redact(event, labels, tw.currentString, mainWindow, wholeStringHighlight)
        
mainWindow.bind("<Key>", redact)

mainWindow.bind_all("<Right>", lambda event: (redactText.applyNewTextRight(event, labels, tw.currentString, tw.lines, wholeStringHighlight), searchBar.confirm(tw.lines, labels, wholeStringHighlight, redactText.isBeingRedacted)))
mainWindow.bind_all("<Left>", lambda event: (redactText.applyNewTextLeft(event, labels, tw.currentString), searchBar.confirmLeft(tw.lines, labels, wholeStringHighlight, redactText.isBeingRedacted)))

mainWindow.bind("<Return>", lambda event: redactText.confirm(event, labels, wholeStringHighlight))
mainWindow.bind("<Shift-Return>", lambda event: redactText.newLine(event, tw.lines, labels, tw.currentString))

mainWindow.bind("<BackSpace>", lambda event: redactText.delLine(event, tw.lines, labels))

mainWindow.bind("<Shift-Button-1>", lambda event: randomRangeSetter.setNewClampersFirst(event)) #shift leftclick
mainWindow.bind("<Shift-Button-3>", lambda event: randomRangeSetter.setNewClampersSecond(event)) #shift rightclick

mainWindow.bind("<Motion>", lambda event: scrollBarFrame.gettingMousePos(event, mainWindow)) #trigers every time mouse moves

mainWindow.mainloop()


#pyinstaller --onefile --noconsole --add-data "fonts;fonts" Language_Learning_App.py