'''
Created on 4 mars 2013

un premier programme python pour tester la configuration correcte de pydev sous eclipse

@author: François de Bertrand de Beuvron (INSA Strasbourg)
'''

import sys
import random

def main():
    c = "bonjour toto"
    c = c + "\ntu utilise la version de python : " + str(sys.version)
    print(c)
    print("\n chaine spéciale : " + r""""Il dit \"\u03B1\net \u03C9\"""" + " --> " + "Il dit \"\u03B1\net \u03C9\"")
    intTab = [1,2,3]
    print("type of " + repr(intTab) + " : " + repr(type(intTab)))
    liste = [1,2,3]
    liste.append(4)
    print("liste  :  " + repr(liste))
    print("toto > titi : " + repr("toto" > "titi"))
    print("tête > tete : " + repr("tête" > "tete"))
    print("code(ê) = " + repr(ord("ê")))
    print("code(e) = " + repr(ord("e")))
    alea = random.random()
    print("random : " , alea)
    tests = ["10/4","10/2","10//4","10%4","2**5","2.0**5", \
             "int(3.5)","int(\"3\")","float(3)","float(\"3.5\")"]
    for t in tests :
        res = eval(t)
        print(t + " = " + str(res)+ " type : " + str(type(res)))
        
    


main()


