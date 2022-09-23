from turtle import *
from random import *
import math

immeuble_x = 0
immeuble_y = 0
sol_y = -100

screen = Screen()
screen.setup(width=600, height=600)
screen._root.resizable(False, False)

def couleur_aleatoire():
    colormode(255)
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)

def sol(y):
    penup()
    sety(y)


def immeuble(immeubles):
    for immeuble in range(1,immeubles):
        im_width = randint(100,200)
        im_etages = 2
        penup()
        color = couleur_aleatoire()
        color(color)
        setx(-250)
        pendown()
        angle = 0
        begin_fill()
        for etages in range(im_etages):
            setx(xcor()+im_width)
            sety(ycor() +100)
            setx(xcor()-im_width)
            sety(ycor() -100)
            if etages != im_etages-1:
                setheading(90)
                forward(100)
            if etages == 0:
                penup()
                setheading(0)
                forward(int(im_width/3))
        print(fillcolor())
##        end_fill()

def fenetres():
    f_type = randint(1,3)
    
    

def herbe(y):
    penup()
    colormode(255)
    color((0,255,0))
    setx(-300)
    pendown()
    pensize(8)
    begin_fill()
    sety((window_height()*-1)+20)
    setx(window_width()-20)
    sety(sol_y)
    setx(-300)
    end_fill()

    

def ville():
    sol(sol_y)
    herbe(sol_y)
    immeuble(2)

ville()
