from random import *

#Variables
juste_prix = randint(1, 1000)
test_prix = 0
nombre_essai = 0

print("Bienvenue au jeu du juste prix !")
print("Le juste prix est un nombre entre 1 et 1000")

while juste_prix != test_prix:
    nombre_essai = nombre_essai + 1
    print("Essai : ", nombre_essai)
    nombre_input = int(input("Devine le prix juste : "))
    test_prix = nombre_input
    if test_prix > juste_prix:
        print("Moins")
    elif test_prix < juste_prix:
        print("Plus")
print("Bravo tu as trouvé le juste prix !")