# Description: This program simulates a Scrabbler GUI.

from Scrabbler import Scrabbler
from tkinter import *

class Application(Frame):

    def __init__(self, root):
        super().__init__(root)
        self.grid()

        self.label = Label(self, text="Welcome to the Scrabbler!")
        self.label.grid(row=0)
        self.instruct = Label(self, text="Please select one of the following options below:")
        self.instruct.grid(row=1, sticky=W)

        # Button to display two-letter words
        self.twoL = StringVar()
        self.twoButton = Button(self, text="Display all two-letter words", command=self.two)
        self.twoButton.grid(row=2, column=0, sticky=W)

        # Button to display words that start with Q but not followed by U.
        self.quL = StringVar()
        self.quButton = Button(self, text="Display words that begin with 'q' but not followed by a 'u'.",
                               command=self.qu)
        self.quButton.grid(row=3, column=0, sticky=W)

        # Button to display words that end in user-inputted tiles.
        self.endButton = Button(self, text="Display words that end with:", command=self.end)
        self.endButton.grid(row=4, column=0, sticky=W)

        # Entry box for user to input tiles for displaying words that end in tiles.
        self.endIn = Entry(self, width=8)
        self.endIn.grid(row=4, column=1, sticky=W)
        self.endIn.config(state="normal")

        # Button to display words that starts with user-inputted tiles.
        self.startButton = Button(self, text="Display words that start with:", command=self.start)
        self.startButton.grid(row=5, column=0, sticky=W)

        # Entry box for user to input tiles for displaying words that start with tiles.
        self.startIn = Entry(self, width=8)
        self.startIn.config(state="normal")
        self.startIn.grid(row=5, column=1, sticky=W)

        # Button for Word Verifier
        self.wCheckButton = Button(self, text="Verify a word:", command=self.wordVerify)
        self.wCheckButton.grid(row=6, column=0, sticky=W)

        # Entry box for user to input word to verify.
        self.wordIn = Entry(self, width=8)
        self.wordIn.config(state="normal")
        self.wordIn.grid(row=6, column=1, sticky=W)


        # Button to display three-letter words that include user tile.
        self.threeButton = Button(self, text="Display three-letter words that include the letter:", command=self.three)
        self.threeButton.grid(row=7, column=0, sticky=W)

        # Entry box for use to enter tile in three-letter words.
        self.threeIn = Entry(self, width=8)
        self.threeIn.config(state="normal")
        self.threeIn.grid(row=7, column=1, sticky=W)

        # Button to display words containing X or Z and the input tile.
        self.xzButton = Button(self, text="Display words that contain 'x' or 'z', and the letter:", command=self.xz)
        self.xzButton.grid(row=8, column=0, sticky=W)

        # Entry box for user to enter tile to check for words that contain it, along with X and Z.
        self.xzIn = Entry(self, width=8)
        self.xzIn.config(state="normal")
        self.xzIn.grid(row=8, column=1, sticky=W)

        # Box that displays results
        self.display = Text(self, width=50, height=20)
        self.display.grid(row=9, column=0, columnspan=3)
        self.display.config(state="disabled")

        self.s = Scrabbler() # Variable to refer to Scrabbler class in the methods below.

    def two(self): # Calls twoWord function from Scrabbler class
        check = self.s.twoLetter()
        self.display.config(state="normal")
        self.display.delete(1.0, END)
        self.display.insert(0.0, check)
        self.display.config(state="disabled")

    def end(self): # Calls endIn function from Scrabbler class
        endInput = self.endIn.get()
        check = self.s.endWith(endInput)
        self.display.config(state="normal")
        self.display.delete(1.0, END)
        self.display.insert(0.0, check)
        self.display.config(state="disabled")

    def start(self): # Calls startWith function from Scrabbler class
        startInput = self.startIn.get()
        check = self.s.startWith(startInput)
        self.display.config(state="normal")
        self.display.delete(1.0, END)
        self.display.insert(0.0, check)
        self.display.config(state="disabled")

    def wordVerify(self): # Calls wordVerifier function from Scrabbler class
        wInput = self.wordIn.get()
        check = self.s.wordVerifier(wInput)
        self.display.config(state="normal")
        self.display.delete(1.0, END)
        self.display.insert(0.0, check)
        self.display.config(state="disabled")

    def three(self): # Calls threeLetter function from Scrabbler class
        tInput = self.threeIn.get()
        check = self.s.threeLetter(tInput)
        self.display.config(state="normal")
        self.display.delete(1.0, END)
        self.display.insert(0.0, check)
        self.display.config(state="disabled")


    def qu(self): # Calls qWithoutU function from Scrabbler class.
        check = self.s.qWithoutU()
        self.display.config(state="normal")
        self.display.delete(1.0, END)
        self.display.insert(0.0, check)
        self.display.config(state="disabled")

    def xz(self): # Calls xzWord function from Scrabbler class.
        linput = self.xzIn.get()
        check = self.s.xzWord(linput)
        self.display.config(state="normal")
        self.display.delete(1.0, END)
        self.display.insert(0.0, check)
        self.display.config(state="disabled")


def main():
    root = Tk()
    myApp = Application(root)
    root.title("Scrabbler")
    root.geometry("600x600")
    root.mainloop()

main()
