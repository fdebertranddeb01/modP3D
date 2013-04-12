'''
Created on 8 avr. 2013
appelle toutes les fonctions de tests des autres modules blender
cela fait bien sur un grand bazard dans la scene
destiné seulement à vérifier qu'il n'y a pas d'erreur dans les fichiers

@author: francois
'''
from modP3D.modelesBlender import collier
from modP3D.modelesBlender import jouet
from modP3D.modelesBlender import vouteOgive
from modP3D.utilsBlender import booleanOp
from modP3D.utilsBlender import primitivesGeometriques
from modP3D.utilsBlender import selections

def testAll():
    collier.testCreationCollier()
    jouet.testJouet()
    vouteOgive.testVouteOgive()
    booleanOp.testsBoolean()
    primitivesGeometriques.testPrimitives()
    selections.testSelections()
    
if __name__ == "__main__":
    testAll()
