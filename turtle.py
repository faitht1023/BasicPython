#this is Faith's turtle 

import turtle

def turtle_movements():

	bob = turtle.Turtle();

	turtle.Screen().bgcolor("pink")

	while True:
		bob.forward(200)
		bob.left(170)
		bob.forward(50)
		bob.right(100)

	bob.end_fill()
	bob.done()

turtle_movements()

turtle.Screen().exitonclick()
