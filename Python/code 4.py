# Alexander Tran
# 3/25/24
# Make some lasagna for your very hungry cat (i was really hungry when i made the idea)


import turtle

def drawSteam (t,c,x,y):
	t.setheading(0)
	t.pensize(1)
	t.color(c)
	t.penup()
	t.setpos(x,y)
	t.pendown() #set up the turtle to its position
	for waves in range(2): #draw steam
		t.circle(10,180)
		t.right(180)
		t.circle(10,-180)
		t.right(180)
	
def drawPasta(t,c,x,y):
	t.color(c)
	t.penup()
	t.setpos(x,y)
	t.pensize(10)
	t.pendown() #set up the turtle to its position
		#draw pasta
	t.setheading(-22.5)
	t.right(90)
	for waves in range(4): #draw front part of pasta
		t.circle(10,180)
		t.right(180)
		t.circle(10,-180)
		t.right(180)
	t.right(210)
	t.forward(100)
		#reset heading and turtle
	t.pensize(1)
	t.setheading(0)
	

def main():
	#make variables
	height = int(input("How high would you like his lasagna to be?"))
	xPosPasta = -100
	yPosPasta = -50
	
	#the holy creation of garf (make the turtle)
	garf = turtle.Turtle()
	garf.speed(25)
	
	#draw the red sauce thats in lasagna idk
	garf.penup()
	garf.setpos(xPosPasta + 5,yPosPasta - 5)
	garf.pendown() #set up garf
	garf.setheading(-22.5)
	garf.color("maroon")
	garf.begin_fill() #set up turtle
		#draw red stuff
	garf.forward(150)
	garf.left(60)
	garf.forward(100)
	garf.left(52.5)
	garf.forward((height * 40) - 15)
	garf.left(126)
	garf.forward(100)
	garf.right(60)
	garf.forward(150)
	garf.left(112.5)
	garf.forward((height * 40) - 15)
	garf.end_fill()
	
	#draw the layers of lasagna
	for layers in range(height):
		drawPasta(garf,"gold",xPosPasta,yPosPasta)
		garf.penup()
		yPosPasta = yPosPasta + 40
		
	#draw cheese
	garf.penup()
	garf.pensize(3)
	garf.color("khaki")
	garf.left(90)
	garf.forward(20)
	garf.pendown()
	garf.begin_fill()
	 #draw the cheese
	garf.left(62.5)
	garf.forward(160)
	garf.left(65)
	garf.forward(110)
	garf.left(118)
	garf.forward(160)
	garf.left(60)
	garf.forward(100)
	garf.end_fill()
	
	#add green herbs
	garf.penup()
	garf.color("dark green")
	garf.left(153)
	garf.setposition(xPosPasta + 50,yPosPasta)
	garf.stamp()
	garf.left(40)
	garf.setposition(xPosPasta + 170,yPosPasta - 20)
	garf.stamp()
	garf.left(20)
	garf.setposition(xPosPasta + 94,yPosPasta + 20)
	garf.stamp()
	garf.right(70)
	garf.setposition(xPosPasta + 120,yPosPasta - 28)
	garf.stamp()
	
	#draw steam
	drawSteam(garf,"gray",xPosPasta,yPosPasta)
	drawSteam(garf,"gray",xPosPasta + 100,yPosPasta + 40)
	drawSteam(garf,"gray",xPosPasta + 170,yPosPasta + 20)
	
	#print name
	print("A steaming lasagna for my orange cat!")
main()
	