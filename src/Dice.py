import sys
from random import randint

def spacing():
	# Function to add spacing as to not clutter the program with print
	# statements.
	print (' ')
	print(' ')
	print(' ')

def diceChange(c):
	# allows you to change dice type to D20, D12, or D6
	if(c == 'd20'):
		print('changed dice to d20')
		return 'd20'
	elif(c == 'd6'):
		print('changed dice to d6')
		return 'd6'
	elif(c == 'd12'):
		print('dice changed to d12')
		return 'd12'
	else:
		print('invalid dice type. Defaulting to d20')
		return 'd20'

def roll(diceType):
	#handles dice rolling through generating random integers
	if(diceType == "d20"):
		x = randint(1,20)
		print('you rolled a {}'.format(x))
		return x
	if(diceType == "d6"):
		x = randint(1,6)
		print('you rolled a {}'.format(x))
		return x
	if(diceType == "d12"):
		x = randint(1,12)
		print('you rolled a {}'.format(x))
		return x
def main():
	#This program rolls digital dice for all your needs. 
	isRun = True
	change = False
	diceType ="d20"

	print('***********************')
	print('Welcome to Dungeon Dice')
	print('***********************')
	while(isRun):
		print('type menu or exit to quit the program')
		r  = raw_input('type the letter r to roll {}: '.format(diceType))
		r = r.lower()
		spacing()
		print('*****************#########*****************')
		print('*****************# o   o #*****************')
		print('*****************#   o   #*****************')
		print('*****************# o   o #*****************')
		print('*****************#########*****************')
		if(r == "c"):
			print('change dice by typing one of the following options:')
			print('d20, d6, or d12')
			c = raw_input('What dice would you like: ')
			diceType = diceChange(c)
		elif(r == 'menu'):	
			print('Dungeon Dice Menu')
			print('r = roll')
			print('c = change')
			print('exit = quit program')
		elif (r == 'r'):
			roll(diceType)
		elif (r == 'exit'):
			print('goodbye')
			isRun = False
		else:
			print('{} is not a command'.format(r))
		spacing()
		print('******************************************')
		print('***************Dungeon Dice***************')
		print('******************************************')


if __name__ == '__main__':
	main()