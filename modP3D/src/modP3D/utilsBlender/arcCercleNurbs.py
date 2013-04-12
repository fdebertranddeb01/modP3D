'''
Created on 5 avr. 2013

creation d'un arc de cercle sous forme de nurbs

le menu add de blender permet de créer un cercle (en fait une nurbs egale à un cercle) mais pas
un arc de cercle.


une explication simple de creation d'arc de cercle sous forme de nurbs :
http://www.cs.mtu.edu/~shene/COURSES/cs3621/NOTES/spline/NURBS/RB-circles.html

Le problème est que blender ne donne pas acces directement au "knots" : ils sont calculés
automatiquement. L'utilisateur a tout de même un controle limité des knots avec les parametres
use_endpoint_u et use_bezier_u

je n'ai pas trouvé de documentation claire sur la représentation des nurbs en blender, et en particulier
le mode précis de calcul des spline. Je vais partir sur les hypothèses : 

A FINIR !!!

@author: francois
'''
