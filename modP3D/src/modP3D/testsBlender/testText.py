'''
Created on 12 mars 2013

manipulation élémentaire de texte en Blender

@author: francois
'''

import bpy

bpy.ops.object.text_add(location=(0,0,0))
txt = bpy.context.scene.objects.active
txt.data.body = "coucou"
 

