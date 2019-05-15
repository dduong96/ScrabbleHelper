# Description: This program defines the functions of the Scrabbler.

# Opens words.txt file and stores values in a list
class Scrabbler(object):
    def __init__(self):
        wList = []
        with open("words.txt", "r") as words:
            for line in words:
                wList.append(line.strip("\n"))
        self.words = wList

    # Displays all two-letter words in file
    def twoLetter(self):
        twList = []
        for word in self.words:
            if len(word) != 2:
                continue
            else:
                twList.append(word)
        displayList = "\n".join(twList)
        return displayList

    # Displays all words ending in user-inputted letters.
    def endWith(self, letters):
        endList = []
        for word in self.words:
            if word.endswith(letters):
                endList.append(word)
        if endList == []:
            msg = "No words ending in those letters."
        else:
            msg = "\n".join(endList)
        return msg

    # Displays all words starting with user-inputted letters.
    def startWith(self, letters):
        startList = []
        for word in self.words:
            if word.startswith(letters):
                startList.append(word)
        if startList == []:
            msg = "No words starting with those letters."
        else:
            msg = "\n".join(startList)
        return msg

    # Checks if user-inputted word exists in the Scrabble dictionary.
    def wordVerifier(self, word):
        if word.lower() in self.words:
            msg = "The word " + word.lower() + " exists."
        else:
            msg = "The word " + word.lower() + " does not exist."
        return msg

    # Checks if any three-letter words contain user-inputted letter
    def threeLetter(self, letter):
        tList = []
        for word in self.words:
            wordList = list(word) # Turns each word into a list to check each letter.
            if letter in wordList and len(word) == 3: # If word is 3 letters and contains user letter, add to new list.
                tList.append(word)
            else:
                continue
        tDisplay = "\n".join(tList)
        return tDisplay

    # Checks for words that start with the letter "q" but not followed by the letter "u".
    def qWithoutU(self):
        qList = []
        for word in self.words:  # Adds all words starting with "q" to list
            if word.startswith("q"):
                qList.append(word)

        uList = []
        for qWord in qList: # Adds words starting with "q" but not followed by "u" to new list
            qwList = list(qWord) # Turns each word into a list to check each letter.
            if qwList[1] != "u":
                uList.append(qWord)
        qDisplay = "\n".join(uList)
        return qDisplay

    # Checks for words that contain "x" or "z" and the user-inputted letter.
    def xzWord(self, letter):
        xzList = []
        for word in self.words:  # Adds all words containing "x" or "z" to list.
            wList = list(word)
            if "x" in wList or "z" in wList:
                xzList.append(word)

        lList = []
        for xzWord in xzList:  # Adds words from xzList to new list if they contain the input letter.
            xzwList = list(xzWord) # Turns each word into a list to check each letter.
            if letter in xzwList:
                lList.append(xzWord)
        xzDisplay = "\n".join(lList)
        return xzDisplay











