'''
Created on 12 mars 2013

creation d'un collier : un ensemble de cercles
jointifs dont les centres se trouvent eux-mêmes sur
un grand cercle

Pour un angle alpha d'un cercle de rayon r,
la longueur de la corde correspondante vaut : 
l = 2*r*sin(alpha/2)

pour un pol

@author: fdebertranddeb01
'''

import math
import bpy

def creationCollier(nombreDePerle,rayonColier):
    collier = bpy.data.groups.new("collier")
    longueurCote = 2*rayonColier*math.sin(math.pi/nombreDePerle)
    numPerle = 0
    while numPerle < nombreDePerle :
        angle = math.pi * 2 / nombreDePerle * numPerle
        centreX = math.cos(angle)*rayonColier
        centreY = math.sin(angle)*rayonColier
        bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, size=longueurCote/2, \
                                              location=(centreX,centreY, 0.0))
        sp = bpy.context.scene.objects.active
        collier.objects.link(sp)
        numPerle = numPerle + 1

def testCreationCollier():
    creationCollier(20,10)

if __name__ == "__main__":
    testCreationCollier()



