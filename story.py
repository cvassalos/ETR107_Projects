##################################
#	story.py
#
#	Author: Constantinos Vassalos
##################################

import random
import time

print("Slay the Dragon!")
print("")

def weaponChoice():
	choice1 = int(input("Choose your weapon of revenge! \n 1 Sword \n 2 Spear \n 3 Bow and Arrow \n 4 A tea kettle \n"))
	if choice1 == 1:
		playerWeapon = "sword"
	if choice1 == 2:
		playerWeapon = "spear"
	if choice1 == 3:
		playerWeapon = "bow and arrow"
	if choice1 == 4:
		playerWeapon = "teakettle"

def coinPath():
	coinFlip = random.randInt(1,2)
	if coinFlip == 1:
		path = "left"
		coinResult = "heads"
		print("Heads. You begin taking the longer path to the left")
		time(6)
	if coinFlip == 2:
		path = right
		coinResult = "tails"
		print("Tails. You rush into the forest")
		time(3)

def encounter():
	if path == "left":
		print("You come across a stranger on the side of the road. His wagon has a broken axel.")
		choice2 = int(input("Do you stop to help them? \n 1 Yes \n No"))
		if choice2 == 1:
			print("You stop the help the stranger")
			time(5)
			print("The stranger thanks you and joins you on your journey. He, too, has a been the victim of the dragon.")
		if choice2 == 2:
			print("There's no time to help this unfortunate fellow, I have a dragon to defeat.")
	if path == "right":
		print("Struggling through the dense forest, you come across a starving wolf. Your rations are low.")
		choice2 = int(input("Is it a good idea to share your remaining rations with the wolf? \n 1 Yes \n 2 No"))
		if choice2 == 1:
			print("The wolf greedily eats the jerky you give it. When breaking camp, it follows you, seeminly obedient.")
			time(2)
		if choice2 == 2:
			print("You leaving the starving wolf to its doom.")
			time(1)

def dragonLair():
	print("You finally make it to the dragon's lair and with great confidence, you enter. The beast is there, looking expectant of your arrival.")
	choice3 = int(input("What do you do? 1 Fight! 2 Talk"))
	if choice3 == 1:
		print("You charge at the dragon with your " + playerWeapon + " drawn!")
		if playerWeapon == "teakettle":
			print("The teakettle breaks into tiny pieces after being smashed into the dragon's  scales. With an annoyed look, the dragon devours you in one bite.")
		if playerWeapon == "sword" or "spear" or "bow and arrow":
			if choice2 == 1:
				print("With the help of your companion you slay the dragon. Now everyone may live in peace!")
			if choice2 == 2:
				time(5)
				print("It is a long and difficult fight, but all alone the  dragon proves to be too much. If only you had someone, or something to help you in the fight. Your bones are added to the dragon's collection in the lair.")
	if choice3 == 2:
		print("Maybe peace is the best answer. You begin a dialogue with the dragon, who suprisingly speaks the same language as you.")
		if playerWeapon == "teakettle":
			if choice2 == 1:
				print("You and the dragon come to an agreement that any more violence is completely unnecessary and that a cup of tea is the best answer. The dragon heats the teakettle and you and your companion enjoy some tea.")
			if choice1 == 2:
				print("You and the dragon come to an agreement that any more violence is completely unnecessary and that a cup of tea is the best answer. The two of you sit and enjoy some tea and peace.")
		else:
			if choice2 == 1:
				print("The dragon sees you are trustworthy judging by your loyal companion. He trusts you despite your fearsome weapon and agrees to cause no more harm to the village.")
			if choice2 == 2:
				print("The dragon considers your words of peace.")
				time(4)
				print("But in the end he devours you as you are armed and alone. One less hero to try to ruin the dragon's fun.")


def story():
	print("Your village has been attacked by the local Dragon one too many times, and you have decided enough is enough.")
	weaponChoice()
	print("You grab your " + playerWeapon + " and leave the village with the intent of putting a stop to this menace.")
	print("On the village's edge you come to a fork in the road. To the left is a clear road, easier traveling but also much longer.")
	print("To the right is a small path through the wilderness. This is the more direct, but also dangerous path to the awaiting dragon.")
	choosePath()
	print("In any case, it is going to be a difficult journey, so you decide to flip a coin")
	coinPath()
	print("All paths lead eventually lead to the same place, right?")
	time(3)
	encounter()
	print("You continue your journey.")
	time(rand.randomInt(3, 9))
	dragonLair()
	print("I hope you enjoyed your adventure!")


story()





