'''
Created on 16 mars 2013

creation d'une petite voute ogivale

@author: fdebertranddeb01
'''

import mathutils 
import bpy
import math

def selectOnly(obj):
    bpy.ops.object.select_all(action = 'DESELECT')
    obj.select = True
    
def deleteObject(obj):
    selectOnly(obj)
    bpy.ops.object.delete()
    
def booleanIntersection(o1,o2):
    inter = o1.modifiers.new("bool","BOOLEAN")
    inter.operation = "INTERSECT"
    inter.object = o2
    # si l'on veut pouvoir ensuite supprimer/modifier o2
    # sans que le résultat soit modifié
    # note : je n'ai pas trouvé la méthode python travaillant directement
    # sur un objet et/ou un modifier. Je dois donc simuler l'utilisation
    # du bouton "apply" des modifier dans l'interface graphique
    # ce bouton appelle l'opérateur bpy.ops.object.modifier_apply qui
    # travaille sur l'objet actif (donc je dois m'assurer que o1 est actif)
    bpy.context.scene.objects.active = o1
    bpy.ops.object.modifier_apply(modifier='bool')
    
def booleanUnion(o1,o2):
    inter = o1.modifiers.new("bool","BOOLEAN")
    inter.operation = "UNION"
    inter.object = o2
    bpy.context.scene.objects.active = o1
    bpy.ops.object.modifier_apply(modifier='bool')
    
def booleanDiff(o1,o2):
    inter = o1.modifiers.new("bool","BOOLEAN")
    inter.operation = "DIFFERENCE"
    inter.object = o2
    bpy.context.scene.objects.active = o1
    bpy.ops.object.modifier_apply(modifier='bool')
    
    
def creationSphere(centre,rayon):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, size=rayon, \
                                          location=centre)
    return bpy.context.scene.objects.active
    
def creationCylindreZ(centre,rayon,hauteur):
    bpy.ops.mesh.primitive_cylinder_add(vertices=32,  end_fill_type='NGON',\
                                        radius=rayon,depth=hauteur,\
                                        location=[centre[0],centre[1],centre[2]+hauteur/2])
    cyl = bpy.context.scene.objects.active
    return cyl

def creationBoiteXYZ(origine,deltaX,deltaY,deltaZ):
    ''' creation d'une boite dont les arêtes sont alignés
    avec les axes OX,OY,OZ du repère global
    origine : point (minX,minY,minZ) de la boite
    '''
    bpy.ops.mesh.primitive_cube_add(location=(0,0,0), \
                                    rotation=(0, 0, 0))
    cube = bpy.context.scene.objects.active
    cube.scale = [deltaX/2,deltaY/2,deltaZ/2]
    cube.location.x = origine[0] + deltaX/2
    cube.location.y = origine[1] + deltaY/2
    cube.location.z = origine[2] + deltaZ/2
    return cube


def creationOgiv(hauteur,largeur,profondeur):
    '''
    cree une ogive dans le plan XZ : 
    la base de la voute est sur l'axe X
    la hauteur de la voute est sur l'axe Z
    la profondeur est centree sur l'axe Y.
    '''
    # On cree d'abord la voute dans le plan XY
    
    # sommet = [0,hauteur,0] 
    # base du premier cercle de l'ogive p1 = [-largeur/2,0,0]
    # base du second cercle de l'ogive p2 = [largeur/2,0,0]
    # il nous faut calculer les centres des cercles
    # angle (p1,ps) ^ (Ox)
    beta = math.atan(hauteur/(largeur/2))
    # angle centre des arcs d'ogives , OX
    alpha = math.pi/2 - beta
    # distance en X entre milieu arc d'ogive et l'origine
    distanceCentre = hauteur/2 / math.tan(alpha)
    origineArc1 = -largeur/4 + distanceCentre
    origineArc2 = largeur/4 - distanceCentre 
    centreC1 = [origineArc1,0,0]
    centreC2 = [origineArc2,0,0]
    rayonArcs = distanceCentre + largeur/4
    cyl1 = creationCylindreZ(centreC1, rayonArcs,profondeur)
    cyl1.name = "Ogive"  
    cyl2 = creationCylindreZ(centreC2, rayonArcs,profondeur)
    booleanIntersection(cyl1, cyl2)
    
    deleteObject(cyl2)
    # sinon, on pourrait se contenter de rendre cyl2 invisible
    # cyl2.hide = True
    
    # il faut maintenant couper tout ce qui se trouve sous
    # le plan XY. Pour cela, on fait une grande boite, que
    # l'on soustrait
    boiteSousOXY = creationBoiteXYZ([-largeur,-2*hauteur,-2*profondeur],\
                                     2*largeur, 2*hauteur, 4*profondeur)
    booleanDiff(cyl1, boiteSousOXY)
    deleteObject(boiteSousOXY)
    
    # je fais ensuite tourner la voute de 90° autour de l'axe X
    # pour ramener la voute dans le plan XZ
    rotX90 = mathutils.Matrix.Rotation(math.radians(90), 4, "X")
    centrageY = mathutils.Matrix.Translation([0,profondeur/2,0])
    cyl1.matrix_world = centrageY * rotX90 * cyl1.matrix_world
    return cyl1

def creationVouteOgivale(hauteurTot,largeurTotX,largeurTotY,\
                         hauteurVouteX,hauteurVouteY,largeurVouteX,largeurVouteY):
    formeExterieure = creationBoiteXYZ([-largeurTotX/2,-largeurTotY/2,0],\
                                        largeurTotX, largeurTotY, hauteurTot)
    # la profondeur des voutes est la largeur opposée multipliée par 1.5 pour être sur
    # que la voute dépasse de la boite, et qu'il y aura donc bien un trou complet
    # après différence
    # a cause d'un bug du module de calcul des opération booleennes qui 
    # n'aime pas, mais alors pas du tout les surface coplanaires, je décale
    # legerement les voutes
    epsilon = min(hauteurVouteX,hauteurVouteY) * 0.00001
    vouteX = creationOgiv(hauteurVouteX+epsilon, largeurVouteX, largeurTotY * 1.5)
    vouteY = creationOgiv(hauteurVouteY+epsilon, largeurVouteY, largeurTotX * 1.5)
    baisseDeEpsilon = mathutils.Matrix.Translation([0,0,-epsilon])
    vouteX.matrix_world = baisseDeEpsilon * vouteX.matrix_world
    vouteY.matrix_world = baisseDeEpsilon * vouteY.matrix_world
    rotZ90 = mathutils.Matrix.Rotation(math.radians(90), 4, "Z")
    vouteY.matrix_world = rotZ90 * vouteY.matrix_world
    booleanDiff(formeExterieure, vouteX)
    booleanDiff(formeExterieure, vouteY)
    deleteObject(vouteX)
    deleteObject(vouteY)
    return formeExterieure
   
    
def testVouteOgive() :
    creationVouteOgivale(10, 10, 9, 9, 9, 9, 9)
    
if __name__ == "__main__":
    # creationCylindreZ([1,2,3], 3, 5)
    # creationBoiteXYZ([-2,-3,-4], 6 , 7, 8)
    # creationOgiv(5, 6, 2)
    # v1 = creationVouteOgivale(7, 8, 5, 6, 3, 4, 3)
    # v1.matrix_world = mathutils.Matrix.Translation([10,0,0]) * v1.matrix_world
    testVouteOgive()
