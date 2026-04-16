def addGaps(lines):
    newLines = []
    for line in lines:
        if line != "\n":
            newLine = line[:18] + (" " * 7) + line[18:39] + (" " * 7) + line[39:] #46
        else:
            newLine = "\n"
        newLines.append(newLine)

    textWrite = ""
    for i in newLines:
        textWrite += i

    with open("WordsWordsWords.txt", "w", encoding = "utf-8") as f:
        f.write(textWrite)
