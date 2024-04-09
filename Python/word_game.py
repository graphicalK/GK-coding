#Alexander Tran
#2/7/24
#A word guessing game that contains an easter egg if you input the right words.

def main():
	#Start up text
	print("================================================")
	print("Hello! My name is Wyrd, and welcome to my game!")
	print("===============================================")
	
	#Ask the user for their name and assign it to 'name'
	print("Wyrd: May I know your name?")
	name = input("What is your name?")
	print(name + ": my name is " + name)
	print("Wyrd: Hello, " + name + "!")
	
	#Display a word bank for the game
	print(" ")
	print("Wyrd: Here is a word bank for the following questions:")
	print("Flounder | Starfish | Tuna")
	print("Dome | Arches | Bridge")
	print("Round | Squishy | Sharp")
	print("Flower | Plant | Tree")
	print("Yellow | Purple | Red")
	print(" ")

	#Question 1
	print("Wyrd: I'm thinking of an aquatic animal that has fins, and is really yummy!") 
	answer1 = input("What is an aquatic animal that has fins and is really yummy?")
	print(name + ": " + answer1 + "!")
	print("Wyrd: If you answered tuna, you're right! Though, flounder also works ;)")
	print(" ")
	
	#Question 2
	print("Wyrd: I'm thinking of a building feature that is commonly used in doorways...")
	answer2 = input("What is a building feature that is commonly used in doorways?")
	print(name + ": " + answer2 + "!")
	print("Wyrd: If you guessed arches, you're correct!")
	print(" ")
	
	#Question 3
	print("Wyrd: I'm thinking of a word that describes a circle!")
	answer3 = input("What is a word that describes a circle?")
	print(name + ": I think its the word " + answer3 + "!")
	print("Wyrd: If you thought the word was round, you're correct!")
	print(" ")
	
	#Question 4
	print("Wyrd: I'm thinking of a plant that is tall, has branches, and has leaves.")
	answer4 = input("What is a plant that is tall, has branches, and has leaves?")
	print(name + ": A " + answer4 + "!")
	print("Wyrd: If you answered with tree, you're correct!")
	print(" ")
	
	#Question 5
	print("Wyrd: I'm thinking of a warm color that is a mix of green and red.")
	answer5 = input("What is a warm color that is a mix of green and red?")
	print(name + ": Is it " + answer5 + "?")
	print("Wyrd: If you answered with yellow, you're right!")
	print(" ")
	
	#show the final answers (insert funny poop joke)
	print("Wyrd: You answered with " + answer1 + ", " + answer2 + ", " + answer3 + ", " + answer4 + ", and " + answer5 + "!")
	print("Did you know that if you put them all into an acronym, it would spell '" + answer1[0] + answer2[0] + answer3[0] + answer4[0] + answer5[0] + "'? Haha!")
main()
