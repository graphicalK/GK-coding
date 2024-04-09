# Alexander Tran
# 3/11/24
# tf2 logo

import turtle

def main():

	hoovy = turtle.Turtle() #declare turtle to be hoovy
	hoovy.setheading(-20) #offset turtle 
	
	#create background circle
	hoovy.color("black")
	hoovy.penup()
	hoovy.begin_fill()
	hoovy.setposition(-15.13,-26.951)
	hoovy.right(70)
	hoovy.forward(130)
	hoovy.left(90)
	hoovy.pendown()
	hoovy.circle(130)
	hoovy.end_fill()
	
	
	hoovy.setposition(0,0) #set hoovy back to 0,0 to draw quadrants
	hoovy.setheading(-20)
	hoovy.pendown()
	
	#quadrant 1
	hoovy.color("chocolate")
	hoovy.begin_fill()
	for innerSide in range(10): #make inner arc of the quadrant
		hoovy.forward(4)
		hoovy.right(10)
	hoovy.left(100)
	hoovy.forward(76.4) #make a side
	hoovy.left(90) 
	for outerSide in range(10): #make outer arc of the quadrant
		hoovy.forward(16)
		hoovy.left(10)
	hoovy.left(80)
	hoovy.forward(76.4) #make the other side of the quadrant
	hoovy.left(90)
	hoovy.end_fill()
	
	#quadrant 2
	hoovy.color("sienna")
	hoovy.penup()
	for innerSide in range(10): #move hoovy to the next quadrant
		hoovy.forward(4)
		hoovy.right(10)
	hoovy.right(-10) #counteract previous loop by 10 degrees
	hoovy.forward(10)
	hoovy.pendown()
	hoovy.begin_fill()
		#make 2nd quadrant
	for innerSide in range(10): #make inner arc of the quadrant
		hoovy.forward(4)
		hoovy.right(10)
	hoovy.left(100)
	hoovy.forward(76.4) #make a side
	hoovy.left(90) 
	for outerSide in range(10): #make outer arc of the quadrant
		hoovy.forward(16)
		hoovy.left(10)
	hoovy.left(80)
	hoovy.forward(76.4) #make the other side of the quadrant
	hoovy.left(90)
	hoovy.end_fill()
	
	#quadrant 3
	hoovy.color("sienna")
	hoovy.penup()
	for innerSide in range(10): #move hoovy to the next quadrant
		hoovy.forward(4)
		hoovy.right(10)
	hoovy.right(-10) #counteract previous loop by 10 degrees
	hoovy.forward(10)
	hoovy.pendown()
	hoovy.begin_fill()
		#make 2nd quadrant
	for innerSide in range(10): #make inner arc of the quadrant
		hoovy.forward(4)
		hoovy.right(10)
	hoovy.left(100)
	hoovy.forward(76.4) #make a side
	hoovy.left(90) 
	for outerSide in range(10): #make outer arc of the quadrant
		hoovy.forward(16)
		hoovy.left(10)
	hoovy.left(80)
	hoovy.forward(76.4) #make the other side of the quadrant
	hoovy.left(90)
	hoovy.end_fill()
	
	#quadrant 4
	hoovy.color("darkgoldenrod")
	hoovy.penup()
	for innerSide in range(10): #move hoovy to the next quadrant
		hoovy.forward(4)
		hoovy.right(10)
	hoovy.right(-10) #counteract previous loop by 10 degrees
	hoovy.forward(10)
	hoovy.pendown()
	hoovy.begin_fill()
		#make 2nd quadrant
	for innerSide in range(10): #make inner arc of the quadrant
		hoovy.forward(4)
		hoovy.right(10)
	hoovy.left(100)
	hoovy.forward(76.4) #make a side
	hoovy.left(90) 
	for outerSide in range(10): #make outer arc of the quadrant
		hoovy.forward(16)
		hoovy.left(10)
	hoovy.left(80)
	hoovy.forward(76.4) #make the other side of the quadrant
	hoovy.left(90)
	hoovy.end_fill()
	hoovy.hideturtle()
	
	print("TF2 Logo")
	
main()
