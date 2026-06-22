import turtle

# Create screen
screen = turtle.Screen()
screen.title("Turtle Square - VS Code")

# Create turtle
pen = turtle.Turtle()
pen.speed(3)
pen.pensize(3)
pen.color("blue")

# Draw square
for _ in range(4):
    pen.forward(150)
    pen.right(90)

# Finish drawing
turtle.done()