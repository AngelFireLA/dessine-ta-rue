from turtle import *
from random import randint, uniform
from tkinter import Tk
from math import *

#Variables utilisées souvent dans le programme et qui sont en haut pour être faciles à modifiées pour des test
nombre_immeubles = 7
sol_y = int(window_height() / 4 * -1)

taille_etage = int((window_height() * 3 / 4 + 230) / 8)
sol_size = window_height() / 2 + sol_y

#Code qui permet de dessiner instantanément le programme, enlevant les délais
screen = Screen()
screen.tracer(False)
screen.delay(0)

#Pemet de créer une fenêtre de la taille de l'écran de l'utilisateur
root = Tk()
screen.setup(width=root.winfo_screenwidth(), height=root.winfo_screenheight())
root.destroy()

#Setup une liste de Turtles et une couleur associées, qui seront utilisées comme "voitures" dans la suite du code"
car_list = []
car_color_list = []
car_number = 10
for loop in range(0, car_number+1):
    if loop == 0:
        hideturtle()
        speed(0)
    else:
        car = Turtle()
        car.hideturtle()
        car.speed(0)
        car_color_list.append((randint(0, 255), randint(0, 255), randint(0, 255)))
        car_list.append(car)


#Générateur de couleur aléatoire pour les immeubles
def couleur_aleatoire():
    colormode(255)
    global r
    global g
    global b
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)


#Code Principal lors de la création des immeubles
def immeuble(immeubles):
    #Distance entre les immeubles pour avoir des immeubles centrées
    im_distance_in_screen = window_width() / (immeubles * 3 + immeubles + 1)
    penup()

    #Remettre la turtle à la gauche de l'écran
    setx(int(window_width() / 2 * -1))

    setx(xcor() + im_distance_in_screen)

    #Boucle qui génère les immeubles
    for immeuble in range(0, immeubles):
        im_width = int(im_distance_in_screen * 3)
        im_etages = randint(3, 5)
        penup()
        couleur_aleatoire()

        #Couleur plus foncée pour le contour
        color((int(r * (3 / 4)), int(g * (3 / 4)), int(b * (3 / 4))))

        starting_x = xcor()

        #Les immeubles sont construits étage par étage et ceci est la boucle qui les gère
        for etages in range(im_etages):
            pendown()
            begin_fill()
            color((int(r * (3 / 4)), int(g * (3 / 4)), int(b * (3 / 4))))
            fillcolor((r, g, b))

            #Rectangle qui est la base de l'étage
            setx(xcor() + im_width)
            sety(ycor() + taille_etage)
            setx(xcor() - im_width)
            sety(ycor() - taille_etage)

            #Si c'est le premier étage, juste faire la porte
            if etages == 0:
                end_fill()
                porte(im_width)

            end_fill()

            #Sinon, faire 3 fenêtre
            if etages != 0:
                fenetres(3, im_width)

            #Permet de mettre la turtle dans le coin en haut à gauche, prête pour le prochain étage
            sety(ycor() + taille_etage)

        toit(im_width)

        #La turtle se met en place pour dessiner le prochain immeuble
        setx(starting_x + im_width)
        setx(xcor() + im_distance_in_screen)
        sety(sol_y*1.1485)


#Fonction qui génère les fenêtres
def fenetres(f_number, im_width):
    penup()
    im_starting_x = xcor()

    #Met en place la turtle pour la première fenêtre
    sety(ycor() + floor(taille_etage / 3))
    setx(int(xcor() + im_width / 16))

    #Taille d'une fenêtre
    window_size = int(im_width / 4)

    #Boucle qui va faire le nombre de fenêtre demander
    for f in range(f_number):

        #Fenêtre Basique, juste un rectangle coloré
        color((0, 0, 0))
        pendown()
        begin_fill()
        setx(int(xcor() + window_size))
        sety(ycor() + taille_etage / 2.5)
        setx(int(xcor() - window_size))
        sety(ycor() - taille_etage / 2.5)
        setx(int(xcor() + window_size))
        fillcolor((153, 255, 255))
        end_fill()
        penup()

        #Détermine le type de la fenêtre ente basique, avec une croix, avec des barres
        f_type = randint(1, 3)

        #Fenêtre avec la croix
        if f_type == 2:
            setx(xcor() - 1)
            setx(ceil(xcor() - window_size / 2))
            pendown()
            sety(ycor() + taille_etage / 2.5)
            sety(ycor() - taille_etage / 5)
            setx(ceil(xcor() - window_size / 2))
            setx(ceil(xcor() + window_size - 1))
            penup()
            sety(ycor() - taille_etage / 5)

        #Fenêtre avec les barres
        if f_type == 3:
            pendown()
            setx(int(xcor() - window_size))
            setx(int(xcor() + window_size / 4))
            sety(ycor() + taille_etage / 2.5)
            setx(int(xcor() + window_size / 4))
            sety(ycor() - taille_etage / 2.5)
            setx(int(xcor() + window_size / 4))
            sety(ycor() + taille_etage / 2.5)
            sety(ycor() - taille_etage / 2.5)
            setx(int(xcor() + window_size / 4) - 3)
            penup()
        setx(int(xcor() + im_width * 1 / 16))

    #Remet la turtle là où elle était avant de dessiner les fenêtres
    setx(im_starting_x)
    sety(ycor() - floor(taille_etage / 3))


#Fonctions qui dessine le toit
def toit(im_width):
    color((0, 0, 0))
    fillcolor((0, 0, 0))
    pendown()

    #Permet de rendre le toit un peu plus large que l'immeuble
    setx(int(xcor() - im_width / 20))

    antennes = randint(0, 3)

    #Dessine le rectangle utilisé comme toit
    begin_fill()
    sety(ycor() + 15)
    setx(xcor() + im_width + int(2 * (im_width / 20)))
    sety(ycor() - 15)
    setx(xcor() - im_width + int(2 * (-im_width / 20)))
    end_fill()

    penup()
    sety(ycor() + 15)
    longueur_toit = im_width + int(2 * (im_width / 20))

    #Dessine les antennes de manière aléatoire
    for loop in range(antennes):
        avance_random = randint(0, int(longueur_toit - 10))
        setx(xcor() + avance_random)
        pendown()
        longueur_antennes = randint(20, 50)
        sety(ycor() + longueur_antennes)
        sety(ycor() - longueur_antennes)
        setx(xcor() - avance_random)
    penup()


#Dessine la porte
def porte(im_width):
    penup()

    #Petit effet pour qu'on voit bien la totalité de la porte, que le bas ne se fonde pas avec el sol
    sety(ycor() + 1)

    #Dessine la porte en fonction de la taille de l'étage et de l'immeuble
    setx(xcor() + int(im_width / 3))
    color((0, 0, 0))
    pendown()
    begin_fill()
    fillcolor((randint(0, 255), randint(0, 255), randint(0, 255)))
    setx(xcor() + int(im_width / 3))
    sety(ycor() + int(taille_etage / 1.4))
    setx(xcor() - int(im_width / 3))
    sety(ycor() - int(taille_etage / 1.4))
    end_fill()
    penup()

    #Remet en place la turtle
    sety(ycor() - 1)
    setx(xcor() - int(im_width / 3))
    pendown()
    color((int(r * (3 / 4)), int(g * (3 / 4)), int(b * (3 / 4))))


#Fonction qui dessine l'herbe et la route
def herbe():
    penup()
    colormode(255)
    color((0, 255, 0))

    #Remet la turtle tout à droite de l'écran
    setx(xcor() - int(window_width() / 2))

    pendown()
    pensize(2)

    #Dessin le rectangle utilisé comme herbe
    begin_fill()
    sety(window_height() * -1)
    setx(window_width())
    sety(sol_y)
    setx(window_width() * -1)
    end_fill()

    begin_fill()

    #Couleur pour la route
    fillcolor((33, 47, 60))
    color((33, 47, 60))

    #Dessine le rectangle utilisé comme route
    sety(ycor() - sol_size / 4)
    setx(int(window_width()))
    sety(ycor() - sol_size / 2)
    setx(int(window_width() * -1))
    end_fill()

    #Dessin la ligne blanche au milieu de la route
    color((255, 255, 255))
    sety(ycor() + sol_size / 3.4)
    pensize(10)
    setx(int(window_width()))
    setx(int(window_width() * -1))
    pensize(2)
    penup()

    #Prépare la turtle pour les immeubles
    setx(int(window_width() / 2 * -1))
    sety(sol_y*1.1485)


#Dessine le ciel, le soleil, et le nuage
def ciel():
    #Dessine le rectangle utilisé comme ciel
    color("cyan")
    begin_fill()
    sety(sol_y)
    setx(int(window_width() / 2 * -1))
    sety(window_height())
    setx(int(window_width() / 2))
    sety(sol_y)
    end_fill()

    #Dessine le soleil
    setx(int((window_width() / 2 * (7 / 8) * -1)))
    sety(int(window_height() / 2 * (12 / 16)))
    color("yellow")
    begin_fill()
    dot(80)
    end_fill()
    dessineRayons(50, 40)
    right(45)
    dessineRayons(50, 40)
    left(45)


def dessineRayons(longueur, rayon):
    for i in range(4):
        penup()
        forward(rayon)
        pendown()
        forward(longueur)
        penup()
        backward(longueur + rayon)
        left(90)


#Fonction qui dessine la voiture
def voiture(taille, car_color: tuple, car):
    car_starting_x = car.xcor()
    car_starting_y = car.ycor()
    car.pendown()

    #Forme de base de la voiture
    colormode(255)
    car.fillcolor(car_color)
    car.begin_fill()
    car.setx(car.xcor() + 75 * taille)
    car.sety(car.ycor() + 20 * taille)
    car.setx(car.xcor() - 63 * taille)
    car.setx(car.xcor() + 38 * taille)
    car.sety(car.ycor() + 20 * taille)
    car.setx(car.xcor() - 30 * taille)
    car.goto(car_starting_x + 11.7*taille, car_starting_y + 20*taille)
    car.setx(car.xcor() - 11.7*taille)
    car.sety(car.ycor() - 20*taille)
    car.end_fill()

    #Roues
    car.fillcolor('black')
    car.penup()
    car.begin_fill()
    car.setx(car.xcor() + 12 * taille)
    car.setheading(0)
    for i in range(2):
        car.sety(car.ycor() - 10 * taille)
        car.circle(9 * taille)
        car.sety(car.ycor() + 10 * taille)
        if i == 0:
            car.setx(car.xcor() + 52 * taille)
    car.setx(car.xcor() - 52 * taille)
    car.setx(car.xcor() - 12 * taille)
    car.end_fill()

    #Dessin la fenêtre de la voiture
    car.penup()
    car.setx(car.xcor() + 21.76*taille)
    car.sety(car.ycor() + 21.76*taille)
    car.begin_fill()
    car.pendown()
    car.fillcolor((153, 255, 255))
    car.setheading(0)
    for i in range(2):
        car.right(90)
        car.forward(-15.88*taille)
        car.right(90)
        car.forward(-25.294*taille)
    car.end_fill()
    car.setx(car.xcor() + floor(25.294*taille / 2))
    car.sety(car.ycor() + floor(15.88*taille/2)*2)
    car.sety(car.ycor() - floor(15.88*taille/2))
    car.setx(car.xcor() + floor(25.294*taille / 2))
    car.setx(car.xcor() - floor(25.294*taille / 2)*2)
    car.sety(car.ycor() - floor(15.88*taille/2))
    car.penup()
    car.setx(car.xcor() - 21.76 * taille)
    car.sety(car.ycor() - 21.76 * taille)
    car.setx(car_starting_x + 75 * taille)
    car.sety(car_starting_y + 20 * taille)

    #Dessine le phare de la voiture
    #le nombre 1.1764 est utilisé car de base j'avais mis 2 mais pour rajouter le multiplicateur "taille" j'ai diviser 2/1.7 qui est le multiplicateur de taille
    car.sety(car.ycor() - 1.17647*taille)
    car.setx(car.xcor() - 1.17647*taille)
    car.pendown()
    car.begin_fill()
    car.fillcolor('yellow')
    car.setx(car.xcor() - 14.7*taille)
    car.sety(car.ycor() - 5.9*taille)
    car.setx(car.xcor() + 14.7*taille)
    car.sety(car.ycor() + 5.9*taille)
    car.end_fill()
    car.penup()

    #Remet la turtle a sa position initiale
    car.sety(car.ycor() + 1.1764*taille)
    car.setx(car.xcor() + 1.1764*taille)
    car.penup()
    car.setx(car_starting_x)
    car.sety(car_starting_y)


#Fonction pour faire bouger la voiture et faire que la voiture ne disparaisse pas de l'écran en la remettant tout à gauche
def voiture_infini(car, car_color):
    car.clear()
    voiture(1.7, car_color, car)
    car.setheading(0)
    car.forward(3)
    if car.xcor() >= window_width() / 2:
        car.setx((window_width() / 2) * -1)
    screen.update()


#Fonction principale qui détermine l'ordre des fonctions dans lequel le programme se déroule
def ville():
    global sol_y
    sety(sol_y)
    herbe()
    ciel()
    #Valeur trouver avec une division car avant c'était une valeur fixe et non une valeur selon l'écran
    sety(sol_y*1.1485)
    immeuble(int(nombre_immeubles))

    #Boucle pour placer les voitures à leur position de départ
    for loop in range(car_number):
        car_list[loop].sety(sol_y)
        car_list[loop].setx(int(-1*window_width()/2)+window_width()/car_number*loop)
        if loop % 2 == 0:
            car_list[loop].sety(car_list[loop].ycor() - sol_size / round(uniform(1.6, 2.1), 1))
        else:
            car_list[loop].sety(car_list[loop].ycor() - sol_size / round(uniform(2.9, 4.2), 1))

    #Démarrage du mouvement des voitures
    while True:
        for loop in range(car_number):
            voiture_infini(car_list[loop], car_color_list[loop])


ville()
done()
