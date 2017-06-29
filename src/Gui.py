import Dice
from Tkinter import * 

root = Tk()
DicePic = PhotoImage(file="../images/D20.png")
w = "press roll"
dType = "d20"

def change():
	w = Dice.roll(dType)
	DiceRoll.config(text = w)
	root.update()

DiceRoll = Label(root, text = w, height = 1)
DiceRoll.grid(row=2, column =0)
D20 = Button(root, text = "D20", height = 1, width = 5).grid(row = 0, column = 1)
D6 = Button(root, text = "D6", height = 1, width = 5).grid(row = 2, column = 1)
D10 = Button(root, text = "D10", height = 1,width = 5).grid(row = 3, column = 1)
D4 = Button(root, text = "D4", height = 1, width = 5).grid(row = 4, column = 1)
Roll = Button(root, text = "roll", command = change, width = 20)
Roll.grid(row = 4, column = 0)

DiceImage = Label(root, image = DicePic).grid(row = 2, column = 3)
root.mainloop()
