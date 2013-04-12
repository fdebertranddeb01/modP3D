#script to run:
SCRIPT = "/media/KeyBeuvron/beuvron/cours/modP3D/programmes/pyBlenderLinuxWorkspace/testPython/src/collier.py"  
    
#path to your org.python.pydev.debug* folder (it may have different version number, in your configuration):
PYDEVD_PATH='/opt/P3D/eclipse/plugins/org.python.pydev_2.7.1.2012100913/pysrc'

import pydev_debug as pydev

pydev.debug(SCRIPT, PYDEVD_PATH)
