'''
Created on 8 avr. 2013

quelques fonctions utilitaires pour trouver/modifier l'objet actif,
et pour modifier l'ensemble des objets selectionnés

@author: francois
'''

import bpy

'''
retourne l'objet actif
'''
def getActif() :
    return bpy.context.scene.objects.active

'''
obj devient le nouvel objet actif
'''
def setActif(obj):
    bpy.context.scene.objects.active = obj

'''
deselectionne tous les objets actuellement selectionnés
'''
def deselectAll():
    bpy.ops.object.select_all(action = 'DESELECT')
    
'''
deselectionne tous les objets actuellement selectionnés
'''
def selectAll():
    bpy.ops.object.select_all(action = 'SELECT')
    
'''
obj devient le seul objet selectionné
'''
def selectOnly(obj):
    deselectAll()
    obj.select = True
    bpy.context.object = obj
    bpy.context.selected_objects = [obj]
    
''' 
supprime l'objet
'''
def deleteObject(obj):
    selectOnly(obj)
    bpy.ops.object.delete()

'''
supprime tous les objets !!!
'''
def supprimeTousLesObjets():
    selectAll()
    bpy.ops.object.delete()
    
'''
cree un nouvel objet qui partage ses donnée avec l'objet de base
il est ensuite possible d'appliquer une transformation pour que les
objets ne soient pas confondus
retourne la nouvelle instance
'''
def dupliqueInstance(obj):
    selectOnly(obj)
    bpy.ops.object.duplicate(linked=True)
    return getActif()

'''
cree un nouvel objet en copiant également les données de l'objet de base
ainsi, les géométries des deux objets peuvent être modifiées indépendament

retourne la nouvelle copie
'''
def dupliqueCopie(obj):
    selectOnly(obj)
    bpy.ops.object.duplicate(linked=False)
    return getActif()

def boiteXYZPourTest(minX,minY,minZ,deltaX,deltaY,deltaZ):
    bpy.ops.mesh.primitive_cube_add()
    boite = getActif()
    boite.location = [minX+deltaX/2,minY+deltaY/2,minZ+deltaZ/2]
    boite.scale = [deltaX/2,deltaY/2,deltaZ/2]
    return boite

def testSelections():
    b1 = boiteXYZPourTest(-5, -5, 0, 10, 20, 8)
    b2 = dupliqueInstance(b1)
    b3 = dupliqueCopie(b1)
    deleteObject(b1)
    deleteObject(b2)
    deleteObject(b3)
#    supprimeTousLesObjets()
    
if __name__ == "__main__":
    testSelections()


