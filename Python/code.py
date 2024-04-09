

# Alexander Tran
# 2/19/24
# A game where you have to figure out how big a conical ice cream cone at a wacky ice cream shop

from math import *

def main():
	
	# variables
	points = 0
	
	# starting text
	print("___________________________________________________")
	print("Welcome to Huuuey's Wacky Emporium of Frozen Treats!")
	print("====================================================")
	print("We serve many types of weird ice cream flavors, but we're more known for our odd ice cream cones!")
	print("They come small, wide, tall, or anything really!")
	print("___________________________________________________")
	print("Huuuey: Hey, you! We're gonna open in a couple minutes.")
	print("Huuuey: Normally, we would have to do hand calculations to find how big they want their cones...")
	print("Huuuey: But thankfully we have the Math Module!")
	print("Huuuey: Oh! Here's our first customer!")
	print(" ")
	
	#customer numero 1
	print("Jill: Hello, my name's Jill. I would like an ice cream cone that is wide")
	print("Jill: Preferably 3 inches in height and 5 inches in width.")
	print("Jill: Thing is, I don't know how much ice cream it can hold!")
	input("Jill would like to have an ice cream cone that is 3 inches tall and 5 inches wide. [Press ENTER to continue]") # done so the user can see the dimensions of the cone (in idle at least)
		# ask the user for dimensions
	height1 = int(input("What is the height of the cone Jill wants? (in inches)"))
	width1 = int(input("What is the width of the cone Jill wants? (in inches)"))
		# perform calculations
	radius1 = width1 / 2 #find radius
	volume1 = (1.0/3.0) * (3.14) * pow(radius1,2) * height1 #volume
	surfaceArea1 = (3.14 * radius1) * (radius1 + (sqrt((pow(radius1,2)+pow(height1,2))))) #surface area
	scoops1 = int(volume1/7.22)
		# print results
	print(" ")
	print("Calculator: Volume - " + str(volume1) + " cubic inches")
	print("Calculator: Surface Area - " + str(surfaceArea1) + " inches squared")
	print("Fun Fact: The average size of an ice cream scoop is 4 ounces, or about 7.22 cubic inches!")
	print(" ")
	print("You: Your ice cream cone can have about " + str(scoops1) + " scoops inside it.")
	print("Jill: Okay! Thank you!")
		#update points
	points = points + 1
	print("___________________________________________________")
	print("POINTS: " + str(points))
	print("___________________________________________________")
	print(" ")
	
	#customer 2
	print("Martin: Hello! I would like a tall ice cream cone thats one foot long!")
	print("Martin: I would like it to be 2 inches wide also.")
	input("Martin would like to have an ice cream cone that is one foot tall and 2 inches wide. [Press ENTER to continue]")
		#ask the user for dimensions
	height2 = int(input("How tall does Martin want his ice cream cone in inches?"))
	width2 = int(input("How wide does Martin want his ice cream cone?"))
		#perform calculations
	radius2 = width2/2
	volume2 = (1.0/3.0) * (3.14) * pow(radius2,2) * height2
	surfaceArea2 = (3.14 * radius2) * (radius2 + (sqrt((pow(radius2,2)+pow(height2,2)))))
	scoops2 = int(volume2/7.22)
		#output results
	print(" ")
	print("Calculator: Volume - " + str(volume2) + " cubic inches")
	print("Calculator: Surface Area - " + str(surfaceArea2) + " inches squared")
	print(" ")
	print("You: Your ice cream cone can have about " + str(scoops2) + " scoops inside it.")
	print("Martin: Alright!")
			#update points
	points = points + 1
	print("___________________________________________________")
	print("POINTS: " + str(points))
	print("___________________________________________________")
	print(" ")
	
	#customer tree
	print("Whestly: Hey there! I LOVE waffle cones!")
	print("Whestly: I would like a cone that is 7 inches tall and 4 inches wide.")
	print("Whestly: How much ice cream cone would I get?")
	input("Whestly would like to have an ice cream cone that is 7 inches tall and 4 inches wide. [Press ENTER to continue]")
		#ask user for dimensions
	height3 = int(input("How tall does Whestly want his ice cream cone?"))
	width3 = int(input("How wide does Whestly want his ice cream cone?"))
		#perform calculations
	radius3 = width3/2
	volume3 = (1.0/3.0) * (3.14) * pow(radius3,2) * height3
	surfaceArea3 = (3.14 * radius3) * (radius3 + (sqrt((pow(radius3,2)+pow(height3,2)))))
	scoops3 = int(volume3/7.22)
		#display results
	print(" ")
	print("Calculator: Volume - " + str(volume3) + " cubic inches")
	print("Calculator: Surface Area - " + str(surfaceArea3) + " inches squared")
	print(" ")
	print("You: You will have " + str(surfaceArea3) + " square inches of our famous waffle cone recipe.")
	print("Whestly: YAYY!! Thank you!")
		#update points
	points = points + 1
	print("___________________________________________________")
	print("POINTS: " + str(points))
	print("___________________________________________________")
	print(" ")
main()
