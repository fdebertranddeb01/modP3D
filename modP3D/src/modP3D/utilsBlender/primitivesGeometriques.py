'''
Created on 8 avr. 2013

quelques fonctions permettant de créer des primitives géométriques

@author: francois
'''

import bpy
from modP3D.utilsBlender.selections import getActif

def cylindreZ(origine,rayon,hauteur):
    bpy.ops.mesh.primitive_cylinder_add(vertices=128, \
                                        radius=rayon, depth=hauteur/2,
                                        location=(origine[0],origine[1],origine[2]+hauteur/2))
    cyl = getActif()
    return cyl

def boiteXYZ(minX,minY,minZ,deltaX,deltaY,deltaZ):
    bpy.ops.mesh.primitive_cube_add()
    boite = getActif()
    boite.location = [minX+deltaX/2,minY+deltaY/2,minZ+deltaZ/2]
    boite.scale = [deltaX/2,deltaY/2,deltaZ/2]
    return boite

def testPrimitives() :
    cylindreZ([0,0,0],1,5)
    
if __name__ == "__main__":
    testPrimitives()
