#this is Faith's turtle 

import turtle

def turtle_movements():

	bob = turtle.Turtle();

	turtle.Screen().bgcolor("pink")

	while True:
		bob.forward(200)
		bob.left(150)
		bob.forward(20)
		bob.right(100)

	bob.end_fill()
	bob.done()
	
def second_turtle():

	brenda = turtle.Turtle();

	turtle.Screen().bgcolor("pink")

	while True:
		brenda.forward(200)
		brenda.right(150)
		brenda.forward(20)
		brenda.left(100)
		

	brenda.end_fill()
	brenda.done()

turtle_movements()
second_turtle()

turtle.Screen().exitonclick()
