'''
Created on 8 avr. 2013

utilitaires sur les transformation.

on utilisera les matrices 4*4 de la géometrie projective pour définir les transformation 
les utilitaires pour créer les transformations de bases sont déjà prédéfinis dans mathutils.Matrix

pour appliquer une transformation, il faut l'appliquer au champ matrix_world de l'objet
(la matrice locale dépend de la position du repère local de l'objet, matrix_world non)

!!!! NE FONCTIONNE PAS ENCORE !!!!

@author: francois
'''
from mathutils import Matrix
import math
from modP3D.utilsBlender.primitivesGeometriques import boiteXYZ
from modP3D.utilsBlender.selections import dupliqueCopie

def transform(obj,matrixTransform):
    obj.matrix_world = matrixTransform * obj.matrix_world
    
def testTransformations():
    b1 = boiteXYZ(-5, -5, 0, 10, 20, 8)
    b2 = dupliqueCopie(b1)
    trans = Matrix.Translation([10,10,0])
    transform(b2, trans)
    #rot = Matrix.Rotation(math.radians(45), 4, 'Z')
    #transform(b2, rot)
                                
if __name__ == "__main__":
    testTransformations()

    