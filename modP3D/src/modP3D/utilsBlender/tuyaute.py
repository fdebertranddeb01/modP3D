'''
Created on 6 mai 2013

création d'un tuyau solide à partir d'une courbe fermée 2D (section) et d'une courbe quelconque (chemin)

!!!! problème dans blender 2.66a : les solides créés par l'extrusion d'une courbe sont
parfois incompatibles avec les opération booleenne (intersection, différence, union)
Pour contourner le problème, il faut recalculer le polyhedre

@author: francois de Bertrand de Beuvron (INSA Strasbourg)
'''

import bpy
from modP3D.utilsBlender.createCurves import creationCourbeOuverte
from modP3D.utilsBlender.createCurves import creationPolygone
from modP3D.utilsBlender.selections import selectOnly, setActif

def tuyaute(chemin,section):
    section.data.dimensions = '2D'
    chemin.data.bevel_object = section
    chemin.data.use_fill_caps = True
    # je converti la courbe en polyhedre
    selectOnly(chemin)
    setActif(chemin)
    bpy.ops.object.convert(target='MESH', keep_original=False)

    
def testTuyaute():
    chemin = creationCourbeOuverte([[0,0,0],[10,10,0]])
    section = creationPolygone([[1,0,0],[0,-1,0],[-1,0,0],[0,1,0]])
    tuyaute(chemin, section)
    
if __name__ == "__main__":
    testTuyaute()

    