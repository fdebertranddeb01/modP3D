'''
Created on 4 mars 2013

Demande un entier n à l'utilisateur, et afficher une chaîne de caractères constituée de n fois le caractère 'A'
Ex : 5 --> AAAAA

un petit programme python comme exemple de 
correspondance entre pseudo-langage algorithmique (module 1 info INSA Strasbourg)
et le langage python

@author: François de Bertrand de Beuvron (INSA Strasbourg)
'''

# pas de déclaration           # variable n en entier
# de variable en Python        # variable res en chaine
#                              # variable i en entier
n = int(input("entrez n\n"));  # lire n
# comme les variables ne sont pas typées en python,
# il est impossible qu'une conversion soit 
# effectuée automatiquement lors de l'entrée des données
# la fonction input(...) produit toujours une chaîne (str python)
# Si l'on veut un entier, il faut donc ensuite convertir cette chaine 
# en entier à l'aide de la fonction int(...)
res = "";                      # res <- ""
i = 0;                         # i <- 0
while i < n :                  # tant que i < n faire
    res = res + "A"            #     res <- res + "A"
    i = i + 1;                 #     i <- i + 1
#                              # fin tant que
# pas d'équivalent au fin de tant que :
# en python, c'est la tabulation elle même qui défini 
# l'appartenance aux structures algorithmiques

print(res);                 # ecrire res
