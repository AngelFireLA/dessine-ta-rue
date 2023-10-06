import turtle
from tkinter import Tk

screen = turtle.Screen()
screen.tracer(False)
screen.delay(0)

root = Tk()
screen.setup(width=root.winfo_screenwidth(), height=root.winfo_screenheight())
root.destroy()


turtle.colormode(255)
tree = turtle.Turtle()
tree.penup()
tree.sety(-200)


#tronc
tree.pendown()
tree.color((153, 76, 0))
tree.begin_fill()
tree.setx(tree.xcor() + 100)
tree.sety(tree.ycor() + 200)
tree.setx(tree.xcor() - 100)
tree.sety(tree.ycor() - 200)
tree.end_fill()
tree.penup()
tree.sety(tree.ycor() + 200)

#Feuille
tree.color("green")
tree.setheading(0)
tree.setx(tree.xcor() - 50)
tree.begin_fill()
for loop in range(3):
    for loop in range(4):
        tree.dot(75)
        tree.forward(50)
    tree.left(120)
tree.end_fill()

tree.penup()
tree.setx(tree.xcor() + 500)
tree.setheading(0)
for loop in range(3):
    tree.dot(120)
    tree.forward(100)
    tree.left(120)

turtle.done()
