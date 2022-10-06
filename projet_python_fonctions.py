from turtle import *
from random import *
from tkinter import *
import keyboard

immeuble_x = 0
immeuble_y = 0
sol_y = int(window_height()/4*-1)
r = 0
g = 0
b = 0


root = Tk()

screen = Screen()
screen.setup(width=root.winfo_screenwidth(), height=root.winfo_screenheight())
root.destroy()


def couleur_aleatoire():
    colormode(255)
    global r
    global g
    global b
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)


def sol(y):
    penup()
    sety(y)


def immeuble(immeubles):
    for immeuble in range(1, immeubles):
        im_width = randint(120, 200)
        im_etages = randint(1, 6)
        penup()
        couleur_aleatoire()
        color((int(r*(3/4)), int(g*(3/4)), int(b*(3/4))))
        setx(int((window_width()/2*-1)+window_width()/20))
        for etages in range(im_etages):
            pendown()
            begin_fill()
            color((int(r*(3/4)), int(g*(3/4)), int(b*(3/4))))
            fillcolor((r, g, b))
            setx(xcor()+im_width)
            sety(ycor() + 100)
            setx(xcor()-im_width)
            sety(ycor() - 100)
            if etages == 0:
                end_fill()
                porte(im_width)
            end_fill()
            if etages != 0:
                fenetres(3, im_width)
            setheading(90)
            forward(100)
        toit(im_width)


def fenetres(f_number, im_width):
    penup()
    im_starting_x = xcor()
    sety(ycor()+30)
    #im_width = im_width_full-im_width_full*1/10
    setx(int(xcor() + (im_width*1/7)-(im_width*1/10)))
    window_size = int((im_width*1/7)+(im_width*1/10))
    for f in range(f_number):
        color((0, 0, 0))
        pendown()
        begin_fill()
        setx(int(xcor()+window_size))
        sety(ycor() + 40)
        setx(int(xcor()-window_size))
        sety(ycor()-40)
        setx(int(xcor()+window_size))
        fillcolor((153, 255, 255))
        end_fill()
        penup()
        f_type = randint(1, 3)
        if f_type == 2:
            setx(xcor() - 1)
            setx(int(xcor()-(window_size/2)))
            pendown()
            sety(ycor() + 40)
            sety(ycor() - 20)
            setx(int(xcor()-(window_size/2)))
            setx(int(xcor()+(window_size-1)))
            penup()
            sety(ycor() - 20)
        if f_type == 3:
            pendown()
            setx(int(xcor()-window_size))
            setx(int(xcor() + window_size/3))
            sety(ycor() + 40)
            setx(int(xcor() + window_size/3))
            sety(ycor() - 40)
            setx(int(xcor() + window_size/3 - 1))
            penup()
        setx(int(xcor()+(im_width*1/7)-(im_width*1/20)))
    setx(im_starting_x)
    sety(ycor()-30)


def toit(im_width):
    color((0, 0, 0))
    fillcolor((0, 0, 0))
    t_type = randint(1, 1)
    im_starting_x = xcor()
    pendown()
    setx(int(xcor()-im_width/20))
    antennes = randint(1, 3)
    if t_type == 1:
        begin_fill()
        speed(1)
        sety(ycor() + 15)
        setx(xcor() + im_width + int(2*(im_width/20)))
        sety(ycor() - 15)
        setx(xcor() - im_width + int(2*(-im_width/20)))
        end_fill()
        penup()
        sety(ycor() + 15)
        # longueur du toit --> im_width + int(2*(im_width/20))




def porte(im_width):
    setheading(0)
    penup()
    sety(ycor()+1)
    forward(int(im_width/3))
    color((0, 0, 0))
    pendown()
    begin_fill()
    if r*(5/4) <= 255 and g*(5/4) <= 255 and b*(5/4) <= 255:
        fillcolor((int(r*(5/4)), int(g*(5/4)), int(b*(5/4))))
    elif r*(5/4) <= 255 and g*(5/4) <= 255 and b*(5/4) > 255:
        fillcolor((int(r*(5/4)), int(g*(5/4)), b))
    elif r*(5 / 4) <= 255 and g * (5 / 4) > 255 >= b * (5 / 4):
        fillcolor((int(r*(5/4)), g, int(b*(5/4))))
    elif r * (5 / 4) > 255 >= b * (5 / 4) and g*(5 / 4) <= 255:
        fillcolor((r, int(g*(5/4)), int(b*(5/4))))
    elif r*(5/4) <= 255 < g*(5 / 4) and b*(5 / 4) > 255:
        fillcolor((int(r*(5/4)), g, b))
    elif r * (5 / 4) > 255 >= b * (5 / 4) and g*(5 / 4) > 255:
        fillcolor((r, g, int(b*(5/4))))
    elif r*(5/4) > 255 and g*(5/4) <= 255 and b*(5/4) > 255:
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
    
    
def herbe():
    penup()
    colormode(255)
    color((0, 255, 0))
    setx(xcor() - int((window_width()/2)))
    pendown()
    pensize(2)
    begin_fill()
    sety((window_height()*-1))
    setx(window_width())
    sety(sol_y)
    setx(int(window_width()*-1))
    end_fill()

    
def ville():
    speed(1000)
    sol(sol_y)
    herbe()

    immeuble(2)


ville()

while True:
    if keyboard.is_pressed("Space"):
        clear()
        ville()
