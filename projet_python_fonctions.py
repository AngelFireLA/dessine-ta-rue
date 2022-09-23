from turtle import *
from random import *
import math

immeuble_x = 0
immeuble_y = 0
sol_y = -100
r = 0
g = 0
b = 0

screen = Screen()
screen.setup(width=600, height=600)
screen._root.resizable(False, False)

def couleur_aleatoire():
    colormode(255)
    global r
    global g
    global b
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

def sol(y):
    penup()
    sety(y)


def immeuble(immeubles):
    for immeuble in range(1,immeubles):
        im_width = randint(125,175)
        im_etages = 2
        penup()
        couleur_aleatoire()
        color((int(r*(3/4)), int(g*(3/4)), int(b*(3/4))))
        setx(-250)
        pendown()
        angle = 0
        for etages in range(im_etages):
            begin_fill()
            fillcolor((r, g, b))
            setx(xcor()+im_width)
            sety(ycor() +100)
            setx(xcor()-im_width)
            sety(ycor() -100)
            if etages == 0:
                end_fill()
                porte(im_width)
            if etages != im_etages-1:
                setheading(90)
                forward(100)
            end_fill()
            if etages != 0:
                fenetres(randint(1,5), im_width)

def fenetres(f_number, im_width):
    penup()
    sety(ycor()+25)
    for f in range(f_number):
        f_type = randint(1,1)
        if f_type == 1:
            color((0,0,0))
            setx(int(xcor()+(im_width*1/4)/f_number))
            pendown()
            setx(int(xcor()+(im_width*2/4)/f_number))
            sety(ycor()+ (im_width*2/4)/f_number)
            setx(int(xcor()-(im_width*2/4)/f_number))
            sety(ycor()- (im_width*2/4)/f_number)
            setx(int(xcor()+(im_width*2/4)/f_number))
            penup()
            
                

def porte(im_width):
    setheading(0)
    penup()
    sety(ycor()+1)
    forward(int(im_width/3))
    color((0,0,0))
    pendown()
    begin_fill()
    if r*(5/4)<=255 and g*(5/4)<=255 and b*(5/4)<=255:
        fillcolor((int(r*(5/4)), int(g*(5/4)), int(b*(5/4))))
    elif r*(5/4)<=255 and g*(5/4)<=255 and b*(5/4)>255:
        fillcolor((int(r*(5/4)), int(g*(5/4)), b))
    elif r*(5/4)<=255 and g*(5/4)>255 and b*(5/4)<=255:
        fillcolor((int(r*(5/4)), g, int(b*(5/4))))
    elif r*(5/4)>255 and g*(5/4)<=255 and b*(5/4)<=255:
        fillcolor((r, int(g*(5/4)), int(b*(5/4))))
    elif r*(5/4)<=255 and g*(5/4)>255 and b*(5/4)>255:
        fillcolor((int(r*(5/4)), g, b))
    elif r*(5/4)>255 and g*(5/4)>255 and b*(5/4)<=255:
        fillcolor((r, g, int(b*(5/4))))
    elif r*(5/4)>255 and g*(5/4)<=255 and b*(5/4)>255:
        fillcolor((r, int(g*(5/4)), b))
    else:
        fillcolor((r, g, b))
    forward(int(im_width/3))
    sety(ycor()+(int((im_width/3)*1.5)))
    setx(xcor()-int(im_width/3))
    sety(ycor()-(int((im_width/3)*1.5)))
    end_fill()
    penup()
    sety(ycor()-1)
    forward(int((im_width/3)*-1))
    pendown()
    color((int(r*(3/4)), int(g*(3/4)), int(b*(3/4))))
    
    

def herbe(y):
    penup()
    colormode(255)
    color((0,255,0))
    setx(-300)
    pendown()
    pensize(2)
    begin_fill()
    sety((window_height()*-1))
    setx(window_width())
    sety(sol_y)
    setx(-300)
    end_fill()

    

def ville():
    sol(sol_y)
    herbe(sol_y)
    immeuble(2)

ville()
