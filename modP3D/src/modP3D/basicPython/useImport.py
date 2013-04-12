'''
Created on 4 mars 2013
 test des packages python
@author: francois
'''

from modP3D.basicPython.testImport import inTestImport
from modP3D.basicPython.testImport.subPackage.inSubPackage import coucou

def mainMod():
    inTestImport.coucou()
    coucou()

mainMod()
