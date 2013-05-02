'''
Created on 2 mai 2013

la fonction de base que l'on veut faire enseuite transformer en module "addOn" Blender

Pour l'instant, c'est un script de base qui doit être executé normalement dans blender
Voir les fichier 
  . moduleSansGUI pour la même fonction sous forme de module sans interface graphique
  . moduleSansGUI pour la même fonction avec interface graphique pour entrer le paramètre
  
@author: francois
'''

import bpy

def cubeDeTailleVariable(taille):
    bpy.ops.mesh.primitive_cube_add()
    boite = bpy.context.scene.objects.active
    boite.scale = [taille,taille,taille]
    
if __name__ == "__main__":
    cubeDeTailleVariable(3)
