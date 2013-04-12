'''
Created on 4 mars 2013

crée une sphere en utilisant l'enregistrement de macro de blender

@author: François de Bertrand de Beuvron (INSA Strasbourg)
'''

import bpy
import random

def main():
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, size=1, view_align=False, enter_editmode=False, \
                                          location=(random.random()*10.0-5.0,random.random()*10.0-5.0, 0.0))
    sp = bpy.context.scene.objects.active
    mat=bpy.data.materials.new('aleaColor')
    mat.diffuse_color = (random.random(),random.random(),random.random())
    sp.data.materials.append(mat)


main()