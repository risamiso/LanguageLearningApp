import tkinter as tk
import thirdWheel
import randomRangeSetter
import scaling as s


def createSquareBehindSearchBar(mainWindow):
    squareBehind = tk.Frame(mainWindow, bg = "#ff8ea9", width = s.scaleSize(374), height = s.scaleSize(37))
    squareBehind.place(x = s.scaleSize(626), y = s.scaleSize(41))
    squareBehind.lower(wordFinderGlob)

wordFinderGlob = None
def createSearchBar(mainWindow):
    global wordFinderGlob
    wordFinder = tk.Entry(mainWindow, bg="#FCF9EA", fg="#69b9b1", relief="flat", bd = 0, width = s.scaleSize(28), font=("Arial", s.scaleSize(17)))
    wordFinder.place(x = s.scaleSize(630), y = s.scaleSize(45), width = s.scaleSize(365), height = s.scaleSize(29))

    wordFinderGlob = wordFinder

currentLookedUpWordIndex = 0
currentSearchBarText = ""
def confirm(lines, labels, wholeStringHighlight, isBeingRedacted):
    if thirdWheel.currentUI == "lrnUI":
        return
    global currentLookedUpWordIndex, currentSearchBarText
    if wordFinderGlob.get() == "" or isBeingRedacted:
        return

    if wordFinderGlob.get() != currentSearchBarText:
        currentSearchBarText = wordFinderGlob.get()
        currentLookedUpWordIndex = 0

    for index, line in enumerate(lines):
        if wordFinderGlob.get().lower() in line.lower():
            if index < currentLookedUpWordIndex:
                continue
            currentLookedUpWordIndex = index + 1
            thirdWheel.textString = index
            if index <= 4:
                thirdWheel.currentString = index
                thirdWheel.currentStringHighlightHeight = 137 + (50 * index)
            
                bottomIndex = 0
                upperIndex = 11
            elif index >= len(lines) - 5:
                thirdWheel.currentString = 11 - (len(lines) - index)
                thirdWheel.currentStringHighlightHeight = 137 + (50 * (11 - (len(lines) - index)))

                bottomIndex = len(lines) - 11
                upperIndex = len(lines)
            else:
                thirdWheel.currentString = 5
                thirdWheel.currentStringHighlightHeight = 387
            
                bottomIndex = index - 5
                upperIndex = index + 7

            wholeStringHighlight.place(x = 0, y = s.scaleSize(thirdWheel.currentStringHighlightHeight))

            thirdWheel.changeLabelsBackground(labels)
            thirdWheel.setLabels(bottomIndex, upperIndex, lines, labels)
            randomRangeSetter.dinamicUpdateClamps()
            return

def confirmLeft(lines, labels, wholeStringHighlight, isBeingRedacted):
    if thirdWheel.currentUI == "lrnUI":
        return
    global currentLookedUpWordIndex
    if wordFinderGlob.get() == "" or isBeingRedacted:
        return
    wordsUntilCurrentLookedUp = lines[:currentLookedUpWordIndex]
    reversedLines = lines[::-1]
    reversedIndexList = []
    for i in range(0, len(lines)):
        reversedIndexList.append(len(lines) - i - 1) #i'm not an imbicile, I just wanted to try two ways to reverse a list

    for index, line in list(zip(reversedIndexList, reversedLines)):
        if wordFinderGlob.get().lower() in line.lower():
            if index + 2 > currentLookedUpWordIndex:
                continue
            currentLookedUpWordIndex = index + 1
            thirdWheel.textString = index
            if index <= 4:
                thirdWheel.currentString = index
                thirdWheel.currentStringHighlightHeight = 137 + (50 * index)
            
                bottomIndex = 0
                upperIndex = 11
            elif index >= len(lines) - 5:
                thirdWheel.currentString = 11 - (len(lines) - index)
                thirdWheel.currentStringHighlightHeight = 137 + (50 * (11 - (len(lines) - index)))

                bottomIndex = len(lines) - 11
                upperIndex = len(lines)
            else:
                thirdWheel.currentString = 5
                thirdWheel.currentStringHighlightHeight = 387
            
                bottomIndex = index - 5
                upperIndex = index + 7

            wholeStringHighlight.place(x = 0, y = s.scaleSize(thirdWheel.currentStringHighlightHeight))

            thirdWheel.changeLabelsBackground(labels)
            thirdWheel.setLabels(bottomIndex, upperIndex, lines, labels)
            return
