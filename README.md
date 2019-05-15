# ScrabbleHelper
A handy tool to help you in your game of Scrabble!

This program simulates a Scrabble Helper (Scrabbler) that has the following features:

1. Lists all words that start with a “Q” but are not followed by a “u”.
2. Displays all 2-letter words.
3. Asks user for a letter and then show all the 3-letter words containing that given input
  tile.
4. Word verifier: Asks user for input and then verify that it exists within the Scrabble
  dictionary.
5. Asks user to enter one or more letters and then show all words that end with that group
  of letters.
6. Asks user to enter one or more letters and then show all words that begin with that
  group of letters.
7. Asks user to enter a letter and then show all words containing the letters “X” or “Z” and
  the input tile.
8. Implements a GUI-based Scrabbler Helper.

The program is comprised of three files:
 - Scrabbler.py
 - ScrabblerGUI.py
 - words.txt, which contains words that the Scrabbler program refers to.

 The 'Scrabbler.py' file contains a class ('Scrabbler') that reads the 'words.txt' file and stores each word into a list.
 It also contains seven functions that implement features 1-7 listed above. Feature 8 is implemented in the 'ScrabblerGUI.py'
 file, which should be run in order to initiate the program. The file generates a graphical user interface (with tkinter as
 a platform) that provides a neat and organized way for the user to utilize the functions inherited from the Scrabbler class.
 In total, there are seven buttons for features 1-7, five of which have entry boxes, that the user can select from. When
 running the program, for those options that have an entry box next to them, the user should input their letter(s) of interest
 before clicking on the button.
