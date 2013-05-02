'''
Created on 2 mai 2013

ajout d'un interface graphique à un module Blender

le module sans interface graphique : moduleSansGUI

les modifications (significatives) par rapport à moduleSansGUI sont signalée dans 
le code à l'aide du commentaire long "GUI"

le but est que blender ouvre un petit panneau permettant à l'utilisateur
de modifier la taille du cube en cours de création

voir : 
http://airplanes3d.net/downloads/pydev/pydev-blender-en.pdf
http://www.blender.org/documentation/blender_python_api_2_66_release/info_tutorial_addon.html
http://en.wikibooks.org/wiki/Blender_3D:_Noob_to_Pro/Advanced_Tutorials/Python_Scripting/Addon_Anatomy

@author: francois
'''

""" 
tout module doit commencer par la définition de cette variable globale qui
contient une description du module
"""

import bpy

bl_info = {
    "name": "cubeSansGUI",  # le nom du module 
    "author": "François de Beuvron",
    "version": (1, 0),
    "blender": (2, 66 , 0),  # version de blender pour laquelle le scrypt a été écrit
    "location": "View3D > Add > Mesh",  # zone des menus où le module sera placé
    "category": "Add Mesh",  # les addOn sont classés par catégorie voir onglet addOns des préférences (ctrl alt u)
    # voir http://wiki.blender.org/index.php/Dev:2.5/Py/Scripts/Guidelines/Addons pour une liste de catégories
    "description": "ajoute un cube de taille 5 a l'origine",
    "warning": "",  
    "wiki_url": "",  # pour faire éventuellement un lien vers une doc du module
    "tracker_url": ""  # pour faire éventuellement un lien vers un serveur gérant les bugs
    }

"""
je recopie ici la fonction de base pour que le module soit indépendant
le changement de nom n'est pas indispensable, mais c'est pour éviter les confusions
"""
def cubeModuleAvecGUI(taille):
    bpy.ops.mesh.primitive_cube_add()
    boite = bpy.context.scene.objects.active
    boite.scale = [taille,taille,taille]


""" 
ici commence la définition du module proprement dite
"""

# un module doit être une classe python sous-classe de la classe prédéfinie bpy.types.Operator
# nous ne verrons pas la programmation orientée objet en python durant ce module
# prenez cette définition telle quelle et adaptez la en modifiant simplement le nom du module
class ModuleAvecGui(bpy.types.Operator):
    """ crée un cube avec sa taille comme propriété """   # une documentation pour la classe
    bl_idname = "modp3d.cubeproptaille"   
    # bl_idname : un nom unique pour le module
    # !!! attention : ce nom ne doit pas comporter de majuscule !!! 
    # (je ne sais pas pourquoi, et je me suis cassé la tête un moment avant de comprendre où était le problème)
    # le module pourra être invoqué depuis la console par :
    # bpy.ops.modp3d.cubeproptaille()
    bl_label = "Cube taille variable"  
    # nom affiché dans l'interface
    # ce nom, lui peut comporter des majuscules et des espaces
    bl_options = {'REGISTER','UNDO'}
    # bl_options : fixe le mode de fonctionnement du module
    # REGISTER : permet un type le fonctionnement Object→Action→Settings standard en blender 2.5+
    # UNDO : permet à Blender de gérer automatiquement le undo/redo
    
    """GUI"""
    # il nous faut définir les propriétés que l'utilisateur pourra modifier dans l'interface graphique
    # voir http://www.blender.org/documentation/blender_python_api_2_66_6/bpy.props.html#module-bpy.props
    # une fois qu'elle est définie, la propriété pourra être accédée par self.taille dans le reste de la classe
    taille = bpy.props.FloatProperty(name="Taille",description="taille du cube",default=5.0,subtype='UNSIGNED',unit='LENGTH')
    
    def execute(self, context):        # cette methode est appelée automatiquement par blender.
        # c'est donc ici que vous devez placer le code effectif de votre module
        # ici, nous créons simplement un cube de taille 5
        cubeModuleAvecGUI(self.taille)
        # pour indiquer à blender que tout s'est bien passé, la méthode execute doir retourner 
        return {'FINISHED'}
    
# fin de la classe

"""
ci-dessous les fonctions permettant à Blender d'ajouter / supprimer votre module
il vous suffit de remplacer ModuleSansGui par le nom de votre module
"""
def register():
    bpy.utils.register_class(ModuleAvecGui)


def unregister():
    bpy.utils.unregister_class(ModuleAvecGui)
    
# le nom est __main__ si le script est executé directement 
# dans ce cas, on enregistre notre module (il n'est pas executé, simplement enregistré)
# pour l'exécuter effectivement, tapez sur la barre espace qui ouvre le dialogue d'execution d'operateur
# vous pouvez ensuite chercher votre module par nom DE LABEL en tapant les premièreslettres
if __name__ == "__main__":
    register()
    