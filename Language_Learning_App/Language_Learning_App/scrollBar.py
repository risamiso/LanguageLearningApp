import tkinter as tk
import thirdWheel as tw
import randomRangeSetter

class scrollBarr(tk.Canvas): #decided to learn classes
    def __init__(self, mainWindow):
        super().__init__(mainWindow, width = 30, height = 511, bg = "#BADFDB", highlightthickness = 0) #up until this part this is essentially a plain Canva.

        print("AAAAA", len(tw.lines))
        self.thumb = None
        self.widthOfWindow = 0
        self.isOn = False

        self.squareInside = self.create_rectangle(0, 0, 28, 509, outline = "#a0d3cd", width = 9)

        mainWindow.update_idletasks()
        self.widthOfWindow = mainWindow.winfo_width()

        self.thumbPlace = 150
        self.place(x = self.widthOfWindow - 51, y = self.thumbPlace)

        self.thumb = tk.Frame(mainWindow, bg = "#FCF9EA", width = 19, height = 30)
        self.thumb.place(x = self.widthOfWindow - 46, y = 155)#625 when down

        self.mousePosition = (0, 0);

        self.checkMousePosition = True #prevents checking mouse position every nanosecond, instead checking it only when it needs to be
        self.isClicked = False

        self.bind("<Button-1>", self.clickOnWidget)
        self.bind("<ButtonRelease-1>", self.unclickTheWidget)

        self.thumb.bind("<Button-1>", self.clickOnWidget)
        self.thumb.bind("<ButtonRelease-1>", self.unclickTheWidget)

    def updatePosition(self, displayStartLine, lines): #passively updates oposition
        ratio = displayStartLine / (len(lines) - 11)
        self.thumbPlace = 155 + (470 * ratio)
        self.thumb.place(x = self.widthOfWindow - 46, y = self.thumbPlace)

    def actuallyScroll(self, mainWindow, labels): #scrolls
        if self.isClicked == False:
            mainWindow.after(25, self.actuallyScroll, mainWindow, labels)
            return

        if self.mousePosition[1] <= 170:
            ratio = 0
        elif self.mousePosition[1] >= 640:
            ratio = 1
        else:
            ratio = (self.mousePosition[1] - 170) / 470

        newDisplayLine = round((len(tw.lines) - 11) * ratio)
        tw.textString = newDisplayLine + tw.currentString
        tw.setLabels(newDisplayLine, newDisplayLine + 11, tw.lines, labels)
        randomRangeSetter.dinamicUpdateClamps()

        self.checkMousePosition = True
        mainWindow.after(25, self.actuallyScroll, mainWindow, labels)





    def gettingMousePos(self, event, mainWindow): #gets mouse position
        if self.checkMousePosition == False:
            return
        self.mousePosition = (event.x_root - mainWindow.winfo_rootx(), event.y_root - mainWindow.winfo_rooty());
        self.checkMousePosition = False


    def clickOnWidget(self, event):
        self.isClicked = True

    def unclickTheWidget(self, event):
        self.isClicked = False

    def hideSelf(self):
        self.place_forget()
        self.thumb.place_forget()

    def showSelf(self):
        self.place(x = self.widthOfWindow - 51, y = 150)
        self.thumb.place(x = self.widthOfWindow - 46, y = self.thumbPlace)
