'''
Created on 4 mars 2013

Resoudre une équation du second degré dans R

un petit programme python comme exemple de 
correspondance entre pseudo-langage algorithmique (module 1 info INSA Strasbourg)
et le langage python

@author: François de Bertrand de Beuvron (INSA Strasbourg)
'''

# pas de déclaration                    # variable a,b,c en flottant
# de variable en Python                 # variable delta,x1,x2 en flottant
a = float(input("a ?"))                 # lire a
b = float(input("b ?"))                 # lire b
c = float(input("c ?"))                 # lire c
delta = b * b - 4 * a * c               # delta <- b*b - 4*a*c
if delta < 0 :                          # si delta < 0 alors
    print("pas de solution");           #    ecrire "pas de solution"
else :                                  # sinon
    if delta == 0 :                     #    si delta = 0 alors
        x1 = -b / (2*a);                #       x1 <- -b/(2*a)
        print("une solution :")         #       ecrire "une solution"
        print("x = " + str(x1))        #       ecrire "x = " + x1
        # il n'y a pas de conversion automatique en chaine de caractère
        # lors de la concaténation en python. C'est pourquoi il faut
        # explicitement appeler la fonction str() qui calcule une
        # représentation d'une valeur sous forme de chaine de caractère
        # voir aussi la fonction repr() qui calcule une représentation canonique
        # voir aussi le formatage (methode .format() des str) pour aller plus loin
    else :                               #    sinon
        x1 = (-b + delta**0.5) / (2*a)   #       x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)   #       x2 = (-b - sqrt(delta)) / (2*a)
        print("deux solutions :")        #       ecrire "deux solutions :"
        print("x1 = " + str(x1));       #       ecrire "x1 = " + x1
        print("x2 = " + str(x2));       #       ecrire "x2 = " + x2
# pas d'équivalent au fin de si          #    fin de si
#                                        # fin de si

