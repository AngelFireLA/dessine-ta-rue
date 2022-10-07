# NOM: Marietti  Prénom: Lysandre-Ange

from random import randint

nombre = randint(1, 100)

tentative_joueur = 0
coups = 0

while True:
    tentative_joueur = int(input("Quel est le nombre mystère ? "))
    if tentative_joueur < nombre:
        coups = coups + 1
        print("C'est plus que", tentative_joueur, ".")
    elif tentative_joueur > nombre:
        coups = coups + 1
        print("C'est moins que", tentative_joueur,".")
    elif tentative_joueur == nombre:
        coups = coups + 1
        print("C'est Gagné en ", coups, " coups ! Le nombre mystère était", nombre, "!")
        rejouer = input("Voulez-vous refaire une partie [O/N] ? ")
        if rejouer == ("O" or "oui" or "o" or "Oui"):
            print("C'est l'heure de rejouer !")
            nombre = randint(1, 100)
            coups = 0
        else:
            print("Au revoir.")
            break

