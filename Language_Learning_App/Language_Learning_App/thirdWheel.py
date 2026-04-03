textString = 0
currentString = 0
currentStringHighlightHeight = 137
currentUI = "mainUI"
displayStartLine = 0
currentMiddleLine = 0
lines = []

class OmnipresentBeing():
    scrollBarObject = None

    def getScrollBarObject(self, scrollBarObject):
        OmnipresentBeing.scrollBarObject = scrollBarObject
        print("omnip is", scrollBarObject)


omnipresentBeing = OmnipresentBeing()



def setLabels(bottomIndex, upperIndex, lines, labels):
    global currentMiddleLine

    global displayStartLine
    print("bottom", bottomIndex)
    print("upper", upperIndex)


    linesToSet = lines[bottomIndex: upperIndex] # list with new lines 

    displayStartLine = bottomIndex

    omnipresentBeing.scrollBarObject.updatePosition(displayStartLine, lines)
    
    

    for string in range(11):
        words = []
        if(linesToSet[string] == "\n"):
            words.append("")
        else:
            words.append(linesToSet[string][:25].strip(" \n")) #18
        words.append(linesToSet[string][25:53].strip(" \n")) #18:39
        words.append(linesToSet[string][53:].strip(" \n")) #39

        for word in range(3):
            labels[string][word].config(text = words[word])


def changeLabelsBackground(labels):
    for i in range(11): #change all label's background to none except for current one
        if i == currentString:
            continue
        if i % 2 == 0:
            for j in range(3):
                labels[i][j].config(bg = "#FCF9EA")#F7EFC7
        else:
            for j in range(3):
                labels[i][j].config(bg = "#F0E4D3")
        for i in range(3): #change current label background to string's
            labels[currentString][i].config(bg = "#FFBDBD")