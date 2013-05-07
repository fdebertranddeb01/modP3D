'''
Created on 26 mars 2013

@author: fdebertranddeb01
'''

import bpy
from modP3D.utilsBlender.selections import setActif
from modP3D.utilsBlender.primitivesGeometriques import cylindreZ

'''
calcule une opération booléenne entre deux objets blender.
Les opération booléenne sont des modificateurs dans blender.
Ici, le modificateur est systématiquement appliqué : l'objet o1 est
modifié par l'opération booléenne, l'objet o2 est supprimé
'''
def booleanOp(o1,o2,booleanType):
    setActif(o1)
    bpy.ops.object.modifier_add(type='BOOLEAN')
    modi = bpy.types.BooleanModifier
    modi = o1.modifiers[-1]  # le modifier le plus récent est en fin de liste
    print("----------------------------------coucou-----------------------------------------------")
    modi.operation = booleanType
    modi.object = o2
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
    setActif(o2)
    bpy.ops.object.delete(use_global=False)
    setActif(o1)
    return o1
    
def intersection(o1,o2):
    return booleanOp(o1,o2,"INTERSECT")
    
def union(o1,o2):
    return booleanOp(o1,o2,"UNION")
    
def diff(o1,o2):
    return booleanOp(o1,o2,"DIFFERENCE")
    


def testsBoolean():
    c1 = cylindreZ([-1,0,0], 2, 1)
    c2 = cylindreZ([1,0,0], 2, 1)
    intersection(c1,c2)

if __name__ == "__main__":
    testsBoolean()
                                        

