#Finding Nemo: Family comedy, Animated, main character animal, main character fish
#KungFu Panda: Family Comedy, animated, main character animal, main character likes kungfu
#Secret life of pets: family comedy, animated, main character animal
#Coco: family comedy, animated, main character sings
#Frozen: family comedy, animated, main character sings, singing snowman
#Toy Story: family comedy, animated, main character toy, belongs to andy
#Lego Movie: family comedy, animated, main character toy
#Despicable Me: family comedy, animated
#Home alone: family comedy, non animated, christmas movie
#Daddy daycare: family comedy, non animated
#Avengers: scifi action, marvel
#Thor: scifi action, marvel, main character uses hammer
#Spiderman: scifi action, marvel, character has suit (red)
#Ironman: scifi action, marvel, character has suit (red), uses jarvis
#Black panther: scifi action, marvel, character has suit
#Doctor Strange: scifi action, marvel, character controls time
#Joker: scifi action, dc, movie in gotham, released in 2019
#Batman: scifi action, dc, movie in gotham, drives batmobile
#Suicide Squad: scifi action, dc, movie in gotham
#Wonderwoman: scifi action, dc

def ins():
	instruction = input("Do you need instructions for this game? ")

	if instruction == "YES" or instruction == "yes" or instruction == "Yes" or instruction == "y" or instruction == "Y":
		print("Here are the instructions...\nChoose a subgenre (either family comedies or scifi action) and choose a movie. Answer the questions with a yes or a no until the system (hopefully) determines the movie.")

ins()		
def main():
	genre = str(input("Please choose a movie sub genre (please enter genre in lowercase) "))
	if genre == "family comedies" or genre == "family":
		animated = str(input("Is your movie animated? "))
		if animated == "YES" or animated == "yes" or animated == "Yes" or animated == "y" or animated == "Y":
			animal = str(input("Is the main character an animal? "))
			if animal == "YES" or animal == "yes" or animal == "Yes" or animal == "y" or animal == "Y":
				fish = input ("Is your main character a fish? ")
				if fish == "YES" or fish == "yes" or fish == "Yes"or fish == "y" or fish == "Y":
					print("Your movie is Finding Nemo\n")
					restart = input("Would you like to play again? ")
					if restart == "YES" or restart == "yes" or restart == "Yes" or restart == "y" or restart == "Y":
						main()
					else:
						quit()
				else:
					kungfu = input("Does your main character like kung fu? ")
					if kungfu == "YES" or kungfu == "yes" or kungfu == "Yes":						
						print("Your movie is Kung Fu Panda\n")
						restart = input("Would you like to play again? ")
						if restart == "YES" or restart == "yes" or restart == "Yes":
							main()
						else:
							quit()
					else:
						print("Your movie is Secret life of pets\n")
						restart = input("Would you like to play again? ")
						if restart == "YES" or restart == "yes" or restart == "Yes":
							main()
						else:
							quit()
			else:
				sing = input("Does the main character sing? ")
				if sing == "YES" or sing == "yes" or sing == "Yes":
					snowman = input("Is there a singing snowman in your movie? ")
					if snowman == "YES" or snowman == "yes" or snowman == "Yes":
						print("Your movie is Frozen\n")
						restart = input("Would you like to play again? ")
						if restart == "YES" or restart == "yes" or restart == "Yes":
							main()
						else:
							quit()
					else:
						print("your movie is Coco\n")
						restart = input("Would you like to play again? ")
						if restart == "YES" or restart == "yes" or restart == "Yes":
							main()
						else:
							quit()
				else:
					toy = input("are the main characters toys? ")
					if toy == "YES" or toy== "yes" or toy == "Yes":
						andy = input("Does the main character belong to Andy? ")
						if andy == "YES" or andy == "yes" or andy == "Yes":
							print("Your movie is Toy Story\n")
							restart = input("Would you like to play again? ")
							if restart == "YES" or restart == "yes" or restart == "Yes":
								main()
							else:
								quit()
						else:
							print("Your movie is The Lego Movie\n")
							restart = input("Would you like to play again? ")
							if restart == "YES" or restart == "yes" or restart == "Yes":
								main()
							else:
								quit()
					else:
						print("Your movie is Despicable me\n")
						restart = input("Would you like to play again? ")
						if restart == "YES" or restart == "yes" or restart == "Yes":
							main()
						else:
							quit()	

		else:
			chrst = input("Is your movie popular during christmas? ")
			if chrst == "YES" or chrst == "yes" or chrst == "Yes":
				print("Your movie is Home Alone\n")
				restart = input("Would you like to play again? ")
				if restart == "YES" or restart == "yes" or restart == "Yes":
					main()
				else:
					quit()
			else:
				print("Your movie is Daddy Daycare\n")
				restart = input("Would you like to play again? ")
				if restart == "YES" or restart == "yes" or restart == "Yes":
					main()
				else:
					quit()


	elif genre == "scifi action" or genre == "scifi" or genre == "scifi" or genre == "scifi action":
		marvel = input("Is your movie produced my marvel? ")
		if marvel == "YES" or marvel == "yes" or marvel == "Yes":
			suit = input("Does the main character wear a suit? ")
			if suit == "YES" or suit == "yes" or suit == "Yes":
				red = input("Is the suit red? ")
				if red == "YES" or red == "yes" or red == "Yes":
					jarvis = input("Does the main character rely on JARVIS? ")
					if jarvis == "YES" or jarvis == "yes" or jarvis == "Yes":
						print("Your movie is Iron Man\n")
						restart = input("Would you like to play again? ")
						if restart == "YES" or restart == "yes" or restart == "Yes":
							main()
						else:
							quit()
					else:
						print("Your movie is Spiderman\n")
						restart = input("Would you like to play again? ")
						if restart == "YES" or restart == "yes" or restart == "Yes":
							main()
						else:
							quit()

				else:
					print("Your movie is Black Panther\n")
					restart = input("Would you like to play again? ")
					if restart == "YES" or restart == "yes" or restart == "Yes":
						main()
					else:
						quit()
			else:
				time = input("Does the main character control time? ")
				if time == "YES" or time == "yes" or time == "Yes":
					print("Your movie is Doctor Strange\n")
					restart = input("Would you like to play again? ")
					if restart == "YES" or restart == "yes" or restart == "Yes":
						main()
					else:
						quit()
				else: 
					hammer = input("Does the main character use a hammer? ")
					if hammer == "YES" or hammer == "yes" or hammer == "Yes":
						print("Your movie is Thor\n")
						restart = input("Would you like to play again? ")
						if restart == "YES" or restart == "yes" or restart == "Yes":
							main()
						else:
							quit()
					else:
						print("Your movie is The Avengers\n")
						restart = input("Would you like to play again? ")
						if restart == "YES" or restart == "yes" or restart == "Yes":
							main()
						else:
							quit()	
		else:
			gotham = input("Does you movie take plce in Gotham? ")
			if gotham == "YES" or gotham == "yes" or gotham == "Yes":
				release = input("Was your movie released in 2019? ")
				if release == "YES" or release == "yes" or release == "Yes":
					print("Your movie is The Joker\n")
					restart = input("Would you like to play again? ")
					if restart == "YES" or restart == "yes" or restart == "Yes":
						main()
					else:
						quit()
				else:
					bat = input("Does the main character drive the batmobile? ")
					if bat == "YES" or bat == "yes" or bat == "Yes":
						print("Your movie is Batman\n")
						restart = input("Would you like to play again? ")
						if restart == "YES" or restart == "yes" or restart == "Yes":
							main()
						else:
							quit()
					else:
						print("Your movie is Suicide Squad\n")
						restart = input("Would you like to play again? ")
						if restart == "YES" or restart == "yes" or restart == "Yes":
							main()
						else:
							quit()
			else:
				print("Your movie is Wonderwoman\n")
				restart = input("Would you like to play again? ")
				if restart == "YES" or restart == "yes" or restart == "Yes":
					main()
				else:
					quit()

	else:
		quit()
main()



