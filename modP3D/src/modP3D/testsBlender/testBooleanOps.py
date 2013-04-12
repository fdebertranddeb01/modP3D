'''
Created on 12 mars 2013

petit essai blender d'utilisation des modifieurs booléen (union, intersection...)

@author: francois
'''

import bpy

bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, size=1, location=(0,0,0))
s1 = bpy.context.scene.objects.active
bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, size=1, location=(1,0,0))
s2 = bpy.context.scene.objects.active
bpy.ops.object.modifier_add(type='BOOLEAN')
mod = bpy.types.BooleanModifier
mod = s2.modifiers[0]
mod.object = s1
mod.operation = "DIFFERENCE"
s1.hide = True
