#Alexander Tran
#4/4/24
#A cool game where you have to get Jumping Gurt into the target zone. (Even has working hit detection!)

import turtle
from math import *

#make variables
turtleXpos = -200
hitTarget = 0
directionCoefficient = 0
counter = 0

#set up game
gurt = turtle.Turtle()
gurt.shape("turtle")
gurt.speed(10)
    #print out the menu
print("_______________________________________________________________")
print("Bouncing Turtle")
print("Help jumping Gurt get to the target area in red!")
print("=======================================================")
print("> L = Boost to the left")
print("> R = Boost to the right")
print("> Angles can be an integer between 0 to 90 degrees")
print("     > 0 degrees = Launch straight forward")
print("     > 90 degrees = Launch straight upwards")
print("> Input a positive floating point number for boost power!")
print("		> Numbers between 1-5 are recommended")
print("_______________________________________________________________")
    #make sky
gurt.color("sky blue")
gurt.begin_fill()
gurt.setposition(-250,250)
for sky in range (4):
    gurt.forward(500)
    gurt.right(90)
gurt.end_fill()
	#make sun
gurt.penup()
gurt.setposition(140,140)
gurt.color("yellow")
gurt.begin_fill()
gurt.circle(30)
gurt.end_fill()

    #make ground
gurt.color("green")
gurt.penup()
gurt.setposition(-200,-100)
gurt.pendown()
gurt.begin_fill()
for n in range (2):
    gurt.forward(400)
    gurt.right(90)
    gurt.forward(100)
    gurt.right(90)
gurt.end_fill()
    #make target
gurt.color("red")
gurt.pensize(10)
gurt.penup()
gurt.forward(230)
gurt.pendown()
gurt.forward(50)
    #move and set up gurt
gurt.penup()
gurt.color("dark orange")
gurt.setposition(-200,-100)
gurt.pensize(3)
gurt.pendown()
gurt.speed(2)

#start the game
while (hitTarget == 0):
	#ask user for inputs
	power = float(input("How powerful should Gurt jump?"))
	angle = int(input("What angle should Gurt jump at?"))
	angleRad = radians(angle)
	direction = input("Should Gurt jump left or right? (R/L)")

	#process user direction input
	if (direction == "L"):
		directionCoefficient = -1
	elif (direction == "R"):
		directionCoefficient = 1
	else:
		print("thats not a menu item man")
		
	#perform calculations
	distance = (directionCoefficient * 360 * power * sin(angleRad))/3.14
	turtleXpos = turtleXpos + distance
	arcMax = 2 * angle

	gurt.setheading(90) #face gurt upwards

	#determine launch direction
	if (direction == "R"):
		gurt.right(90 - angle)
	else:
		gurt.left(90 - angle)

	#draw the arc
	for n in range (arcMax):
		gurt.forward(power)
		gurt.right(1 * directionCoefficient)
	gurt.left(angle * directionCoefficient)
	
	#check if the turtle is in range of the target
	if (turtleXpos >= 30):
		if (turtleXpos <= 80):
			hitTarget = 1 #end the while loop
	#print a statement telling the user where Gurt is at
	print("Gurt is currently at " + str(turtleXpos) + ". Get him to the zone!")
	counter = counter + 1

print("============================================")
print("You landed Gurt in the Zone! You win!") #winner winner chicken dinner
print("Gurt took " + str(counter) + " jumps. See if you can get less!")
	
