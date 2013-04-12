'''
Created on 15 mars 2013

petits utilitaires de création de courbes

@author: francois
'''

import bpy

''' creation d'une courbe de Bezier à partir d'un ensemble de points de controles
  typeControles possible dans blender : ‘FREE’, ‘VECTOR’, ‘ALIGNED’, ‘AUTO’
  ici : VECTOR --> polyligne
        AUTO --> courbe
'''
def creationBezier(sommets,typeControles,fermee=False):
    if typeControles == "VECTOR" :
        nom = "polygone"
    else :
        nom = "courbe"
    # create curve
    newCurve = bpy.data.curves.new(nom, type = "CURVE")
    newBezier = newCurve.splines.new(type = "BEZIER") 
    newBezier.use_cyclic_u = fermee
    newBezier.bezier_points.add(len(sommets)-1)
    for i in range(0,len(sommets)) :
        p = bpy.types.BezierSplinePoint
        p = newBezier.bezier_points[i]
        p.co = sommets[i]
        p.handle_left_type = typeControles
        p.handle_right_type = typeControles
    
    # place la courbe dans un object et rend cet objet selectionné et actif
    new_obj = bpy.data.objects.new(nom, newCurve)
    scene = bpy.context.scene
    scene.objects.link(new_obj) # place in active scene
    new_obj.select = True # set as selected
    scene.objects.active = new_obj # set as active
    return new_obj

def creationPolyligne(sommets):
    return creationBezier(sommets, 'VECTOR', False)
 
def creationPolygone(sommets):
    return creationBezier(sommets, 'VECTOR', True)
 
def creationCourbeOuverte(sommets):
    return creationBezier(sommets, 'AUTO', False)
 
def creationCourbeFermee(sommets):
    return creationBezier(sommets, 'AUTO', True)
 
def testsBezier() :
    sommets = [[0, 0, 0], [1, 1, 0], [2, 1, 0], [3, 0, 0], [2, -1, 0]]
    creationPolyligne(sommets)
    for s in sommets :
        s[0] = s[0] + 5
    creationPolygone(sommets)
    for s in sommets :
        s[0] = s[0] + 5
    creationCourbeOuverte(sommets)
    for s in sommets :
        s[0] = s[0] + 5
    creationCourbeFermee(sommets)
 
if __name__ == "__main__":
    testsBezier()
    