'''
Created on 16 mars 2013

un petit scipt pour créer un "jouet" d'enfant constitué d'un
ensemble de cylindres empilés, et d'une sphère au dessus.

@author: François de Bertrand de Beuvron (INSA Strasbourg)
'''
import bpy
import random

def creationCylindreZ(centre,rayon,hauteur) :
    centre[2] = centre[2] + hauteur/2
    bpy.ops.mesh.primitive_cylinder_add(vertices=32,\
                                    radius=rayon,\
                                    depth=hauteur,location=centre)
    cyl =  bpy.context.scene.objects.active
    bpy.ops.object.shade_smooth()
    return cyl

def creeSphere(origine,rayon):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, size=rayon, \
                                          location=origine)
    res = bpy.context.scene.objects.active
    bpy.ops.object.shade_smooth()
    return res

def colorieAleatoirement(obj):
    mat=bpy.data.materials.new("aleaColor")
    rouge = random.random()
    vert = random.random()
    bleu = random.random()
    mat.diffuse_color = (rouge,vert,bleu)
    obj.data.materials.append(mat)
     
    
def creationJouet(posX = 0.0,posY = 0.0,rayonInitial = 10.0,\
                  rayonFinal = 3.0,hauteurDisque = 1.0,\
                  nbrDisques = 6) :
    deltaR = (rayonFinal - rayonInitial) / nbrDisques
    
    i = 0
    hCourante = 0
    rCourant = rayonInitial
    while i < nbrDisques :
        cylCourant = creationCylindreZ([posX,posY,hCourante], rCourant, hauteurDisque)
        colorieAleatoirement(cylCourant)
        hCourante = hCourante + hauteurDisque
        rCourant = rCourant + deltaR
        i = i + 1
    tete = creeSphere([posX,posY,hCourante+rayonFinal*2], rayonFinal*2)
    colorieAleatoirement(tete)

def testJouet():
    creationJouet(0,0,5.0,1.0,hauteurDisque = 1.0,nbrDisques = 6)

if __name__ == "__main__":
    testJouet()
