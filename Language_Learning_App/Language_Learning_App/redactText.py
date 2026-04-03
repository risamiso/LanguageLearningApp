import tkinter as tk
import thirdWheel as tw
import searchBar
import randomRangeSetter


text1 = ""
inputBar1 = None
inputBar2 = None
inputBar3 = None

barFrame1 = None
barFrame2 = None
barFrame3 = None

currentSlot = 0
yPos = 0

isBeingRedacted = False #did my ignorance just manufacture dread?
def redact(event, labels, currentString, mainWindow, wholeStringHighlight):
    global text1, inputBar1, inputBar2, inputBar3, barFrame1, barFrame2, barFrame3, currentSlot, yPos, isBeingRedacted
    if tw.currentUI == "lrnUI" or isBeingRedacted:
        return
    currentSlot = 0
    wholeStringHighlight.config(bg = "#ff7f7f")
    for i in range(3):
        labels[currentString][i].config(bg = "#ff7f7f", fg = "white")
    inputBar1 = tk.Entry(mainWindow, bg="#ff7f7f", fg="white", relief="flat", bd = 0, width = 28, font=("Arial", 17)) #bd is border length
    inputBar2 = tk.Entry(mainWindow, bg="#ff7f7f", fg="white", relief="flat", bd = 0, width = 28, font=("Arial", 17))
    inputBar3 = tk.Entry(mainWindow, bg="#ff7f7f", fg="white", relief="flat", bd = 0, width = 28, font=("Arial", 17))

    barFrame1 = tk.Frame(mainWindow, bg = "white", width = 371, height = 5) # 31 401 771
    barFrame2 = tk.Frame(mainWindow, bg = "white", width = 371, height = 5)
    barFrame3 = tk.Frame(mainWindow, bg = "white", width = 701, height = 5)

    if inputBar1 != None and inputBar2 != None and inputBar3 != None:
        inputBar1.delete(0, tk.END)
        inputBar2.delete(0, tk.END)
        inputBar3.delete(0, tk.END)

    yPos = labels[currentString][0].winfo_y()

    inputBar1.place(x = 31, y = yPos)
    inputBar1.insert(0, labels[currentString][0].cget("text")) #puts text that was in the label in the input bar
    inputBar1.focus_set() #does so that it automatically is selected and you can start typing

    barFrame1.place(x = 31, y = yPos + 27)

    isBeingRedacted = True
    
def applyNewTextRight(event, labels, currentString, lines, wholeStringHighlight): #goes on the right in redacting line
    if tw.currentUI == "lrnUI":
        return
    global inputBar1, inputBar2, inputBar3, barFrame1, barFrame2, barFrame3, currentSlot

    if currentSlot == 2 or isBeingRedacted == False:
        return

    characterNumber = 0 #checks where the cursor is(at the end of a word or somewhere else)

    if currentSlot == 0:
        characterNumber = inputBar1.index("insert") #checks where the cursor is in the Entry field
        print("characterNumber is ", characterNumber)
        print("length is ", len(inputBar1.get()))
        if canGoOn():
            return
        barFrame1.place_forget()
        inputBar1.place_forget()
        inputBar2.place(x = 401, y = yPos)
        inputBar2.insert(0, labels[currentString][1].cget("text"))
        inputBar2.focus_set()
        barFrame2.place(x = 401, y = yPos + 27)

        inputBar1.delete(0, tk.END)
    else:
        inputBar2.place_forget()
        barFrame2.place_forget()
        inputBar3.place(x = 771, y = yPos)
        inputBar3.insert(0, labels[currentString][2].cget("text"))
        inputBar3.focus_set()
        barFrame3.place(x = 771, y = yPos + 27)

        inputBar2.delete(0, tk.END)
    currentSlot += 1


def applyNewTextLeft(event, labels, currentString):
    if tw.currentUI == "lrnUI":
        return
    global inputBar1, inputBar2, inputBar3, barFrame1, barFrame2, barFrame3, currentSlot

    if currentSlot == 0 or isBeingRedacted == False:
        return

    if currentSlot == 1:
        barFrame2.place_forget()
        inputBar2.place_forget()
        inputBar1.place(x = 31, y = yPos)
        inputBar1.insert(0, labels[currentString][0].cget("text"))
        inputBar1.focus_set()
        barFrame1.place(x = 31, y = yPos + 27)

        inputBar2.delete(0, tk.END)
    else:
        inputBar3.place_forget()
        barFrame3.place_forget()
        inputBar2.place(x = 401, y = yPos)
        inputBar2.insert(0, labels[currentString][1].cget("text"))
        inputBar2.focus_set()
        barFrame2.place(x = 401, y = yPos + 27)

        inputBar3.delete(0, tk.END)
    currentSlot -= 1

def confirm(event, labels, wholeStringHighlight):
    if tw.currentUI == "lrnUI":
        return
    global inputBar1, inputBar2, inputBar3, barFrame1, barFrame2, barFrame3, currentSlot, isBeingRedacted

    if isBeingRedacted == False:
        searchBar.confirm(tw.lines, labels, wholeStringHighlight, isBeingRedacted)
        return

    if inputBar1 == None or inputBar2 == None or inputBar3 == None:
        return

    throwAwayLine = ""
    throwAwayLine2 = ""
    textToWriteInTXT = ""
    if inputBar1.winfo_ismapped(): #changing first word
        throwAwayLine = tw.lines[tw.textString] #copies the string that is about to be changed
        throwAwayLine =  (" " * (25 - len(inputBar1.get()))) + throwAwayLine[25:]           #XXX

        tw.lines[tw.textString] = inputBar1.get() + throwAwayLine
        labels[tw.currentString][0].config(text = inputBar1.get())
        applyNewTextRight(event, labels, tw.currentString, tw.lines, wholeStringHighlight)

        for i in tw.lines:
            textToWriteInTXT += i
        with open("WordsWordsWords.txt", "w", encoding = "utf-8") as f:
            f.write(textToWriteInTXT)

    elif inputBar2.winfo_ismapped():
        throwAwayLine = tw.lines[tw.textString][:25] #left part of a string
        throwAwayLine2 = tw.lines[tw.textString] #right part of a string
        throwAwayLine2 =  (" " * (28 - len(inputBar2.get()))) + throwAwayLine2[53:] #it was 21 instead of 28

        tw.lines[tw.textString] = throwAwayLine + inputBar2.get() + throwAwayLine2
        labels[tw.currentString][1].config(text = inputBar2.get())
        applyNewTextRight(event, labels, tw.currentString, tw.lines, wholeStringHighlight)

        for i in tw.lines:
            textToWriteInTXT += i
        with open("WordsWordsWords.txt", "w", encoding = "utf-8") as f:
            f.write(textToWriteInTXT)
    elif inputBar3.winfo_ismapped():
        throwAwayLine = tw.lines[tw.textString][:53]
        
        tw.lines[tw.textString] = throwAwayLine + inputBar3.get() + "\n"
        labels[tw.currentString][2].config(text = inputBar3.get())

        randomRangeSetter.getLines(tw.lines)
        abruptRedacting(labels, tw.currentString, wholeStringHighlight)

        for i in tw.lines:
            textToWriteInTXT += i
        with open("WordsWordsWords.txt", "w", encoding = "utf-8") as f:
            f.write(textToWriteInTXT)


def abruptRedacting(labels, currentString, wholeStringHighlight):
    if tw.currentUI == "lrnUI":
        return
    global isBeingRedacted
    if isBeingRedacted == True:
        isBeingRedacted = False
        for i in range(3):
            labels[currentString][i].config(fg = "#5ab2a9", bg = "#FFBDBD")
        inputBar1.place_forget()
        inputBar2.place_forget()
        inputBar3.place_forget()

        barFrame1.place_forget()
        barFrame2.place_forget()
        barFrame3.place_forget()

        wholeStringHighlight.config(bg = "#FFBDBD")



def newLine(event, lines, labels, currentString):
    if tw.currentUI == "lrnUI":
        return

    textToWriteInTXT = ""
    last = False

    if tw.textString == len(lines) - 1:
        tw.textString += 1
        tw.lines.insert(tw.textString, "\n")
        last = True 
    else:
        tw.lines.insert(tw.textString, "\n")

    for i in tw.lines:
        textToWriteInTXT += i
    with open("WordsWordsWords.txt", "w", encoding = "utf-8") as f:
        f.write(textToWriteInTXT)

    if last:
        bottomIndex = tw.textString - 10
        upperIndex = tw.textString + 1
    else:
        bottomIndex = tw.textString + (currentString * (-1))
        upperIndex = tw.textString + (11 - currentString)


    tw.setLabels(bottomIndex, upperIndex, tw.lines, labels)

    if(randomRangeSetter.clampOne >= tw.textString):
        randomRangeSetter.clampOne += 1
    if(randomRangeSetter.clampTwo >= tw.textString):
        randomRangeSetter.clampTwo += 1

    randomRangeSetter.dinamicUpdateClamps()

    randomRangeSetter.getLines(tw.lines)

def delLine(event, lines, labels):
    if tw.currentUI != "mainUI":
        return

    textToWriteInTXT = ""


    if(lines[tw.textString] == "\n"):
        print("yes")
        del tw.lines[tw.textString]

        for i in tw.lines:
            textToWriteInTXT += i

        with open("WordsWordsWords.txt", "w", encoding = "utf-8") as f:
            f.write(textToWriteInTXT)

        if tw.displayStartLine < len(tw.lines) - 11:
            bottomIndex = tw.displayStartLine
            upperIndex = tw.displayStartLine + 11
        else:
            bottomIndex = tw.displayStartLine - 1
            upperIndex = tw.displayStartLine + 11
            tw.textString -= 1

        tw.setLabels(bottomIndex, upperIndex, tw.lines, labels)

        if(randomRangeSetter.clampOne >= tw.textString):
            randomRangeSetter.clampOne -= 1
        if(randomRangeSetter.clampTwo >= tw.textString):
            randomRangeSetter.clampTwo -= 1
            if(randomRangeSetter.clampTwo == randomRangeSetter.clampOne):
                randomRangeSetter.clampTwo = randomRangeSetter.clampOne + 1

        randomRangeSetter.dinamicUpdateClamps()
    else:
        print("no")


def canGoOn():
    if inputBar1.index("insert") == inputBar1.get():
        return True
    else:
        return False
