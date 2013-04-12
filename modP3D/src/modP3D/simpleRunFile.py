'''
Created on 8 avr. 2013

lit un fichier et l'execute

inspiré de : http://stackoverflow.com/questions/13617395/real-alternatives-to-execfile-in-python3-3
et du pydev_debug fourni par Witold Jaworski comme compagnon de son livre internet :  pydev-blender-en.pdf
     http://airplanes3d.net/pydev-000_e.xml

@author: francois
'''

MAINPATH = "/media/KeyBeuvron/beuvron/cours/modP3D/programmes/pyBlenderLinuxWorkspace/modP3D/src/"

# SCRIPT = "modP3D/testAll.py"  
SCRIPT = "modP3D/utilsBlender/transformations.py"  

import sys

if sys.path.count(MAINPATH) < 1: sys.path.append(MAINPATH)

def runRel(relativePath):
    filepath = MAINPATH+relativePath
    runAbsolutePath(filepath)
    
def runAbsolutePath(filepath):
    global_namespace = {"__file__": filepath, "__name__": "__main__"}
    file = open(filepath, 'rb')
    exec(compile(file.read(), filepath, 'exec'), global_namespace)
    file.close()
    
if __name__ == "__main__":
    runRel(SCRIPT)

