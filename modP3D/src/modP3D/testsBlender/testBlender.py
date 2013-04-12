'''
Created on 4 mars 2013

un premier programme python pour tester la configuration correcte de pydev pour blender

ce programme doit être executé dans blender dans un projet contenant un objet s'appelant "cube"
par exemple, dans le projet par défaut lors du démarage de blender 2.65

@author: François de Bertrand de Beuvron (INSA Strasbourg)
'''

import bpy

def main():
    # la première affectation ci-dessous permet à pydev d'inférer le type de l'objet
    # et donc de fournir le "code completion" si pratique lorsque l'on tape le programme
    # Witold Jaworski conseille de la commenter quand on a fini de taper le code
    # Il n'y aurait pas besoin de ce "truc" dans un langage fortement typé

    cube = bpy.types.Object
    cube = bpy.data.objects["Cube"]
    cube.scale = [3.0,2.0,1.0]
    cube.location = [4.0,3.0,2.0]

main()