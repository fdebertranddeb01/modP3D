'''
Created on 9 avr. 2013

quelques utilitaires de calcul sur les cercles

@author: francois
'''

import math

def cercleXY(p1,p2,p3):
    '''
    cercle 2D sur le plan XY passant par 3 points
    retourne le centre et le rayon du cercle
    
    Les formules ont été obtenues dans mathematica par la résolution "bete" : 
        eqc = (x - cx)^2 + (y - cy)^2 == r2
        eqEnP1 = eqc /. {x -> p1x, y -> p1y}
        eqEnP2 = eqc /. {x -> p2x, y -> p2y}
        eqEnP3 = eqc /. {x -> p3x, y -> p3y}
        allEqs = {eqEnP1, eqEnP2, eqEnP3}
        
        FortranForm[Solve[allEqs, {cx, cy, r2}]]
    Une formulation plus simple est sans doute possible
    
    retourne une liste de trois flottant [cx,xy,r]
    
    note : nous n'avons pas vu les paires, mais cela auraient été bien pratique dans ce cas 
    puisque python aurait permis d'écrire : 
       centre , rayon = cercleXY(p1,p2,p3)
    pour affecter en même temps les variable centre et rayon
    '''
    p1x = p1[0]
    p1y = p1[1]
    p2x = p2[0]
    p2y = p2[1]
    p3x = p3[0]
    p3y = p3[1]
    if (-p1x + p2x)*(-p1y + p3y) == (-p1y + p2y)*(-p1x + p3x) :
        # les points sont colinéaire ou confondus
        raise Exception("les points sont colinéaires :" + str(p1) + " ; " + str(p2) + " ; " + str(p3))
    r2=p3x**2 + p3y**2 - \
          (p3y*(p1x**2*p2x + p1y**2*p2x - p1x*p2x**2 - p1x*p2y**2 - \
               p1x**2*p3x - p1y**2*p3x + p2x**2*p3x + p2y**2*p3x + \
               p1x*p3x**2 - p2x*p3x**2 + p1x*p3y**2 - p2x*p3y**2))/ \
           (p1y*p2x - p1x*p2y - p1y*p3x + p2y*p3x + p1x*p3y - p2x*p3y) \
            + (p1x**2*p2x + p1y**2*p2x - p1x*p2x**2 - p1x*p2y**2 - \
              p1x**2*p3x - p1y**2*p3x + p2x**2*p3x + p2y**2*p3x + \
              p1x*p3x**2 - p2x*p3x**2 + p1x*p3y**2 - p2x*p3y**2)**2/ \
           (4.*(p1y*p2x - p1x*p2y - p1y*p3x + p2y*p3x + p1x*p3y - \
                p2x*p3y)**2) + \
          (p3x*(-(p1y*p2x**2) + p1x**2*p2y + p1y**2*p2y - \
               p1y*p2y**2 + p1y*p3x**2 - p2y*p3x**2 - p1x**2*p3y - \
               p1y**2*p3y + p2x**2*p3y + p2y**2*p3y + p1y*p3y**2 - \
               p2y*p3y**2))/ \
           (p1y*p2x - p1x*p2y - p1y*p3x + p2y*p3x + p1x*p3y - p2x*p3y) \
            + (-(p1y*p2x**2) + p1x**2*p2y + p1y**2*p2y - p1y*p2y**2 + \
              p1y*p3x**2 - p2y*p3x**2 - p1x**2*p3y - p1y**2*p3y + \
              p2x**2*p3y + p2y**2*p3y + p1y*p3y**2 - p2y*p3y**2)**2/ \
           (4.*(p1y*p2x - p1x*p2y - p1y*p3x + p2y*p3x + p1x*p3y - \
                p2x*p3y)**2)
    ox = -(-(p1y*p2x**2) + p1x**2*p2y + p1y**2*p2y - \
             p1y*p2y**2 + p1y*p3x**2 - p2y*p3x**2 - p1x**2*p3y - \
             p1y**2*p3y + p2x**2*p3y + p2y**2*p3y + p1y*p3y**2 - \
             p2y*p3y**2)/ \
          (2.*(p1y*p2x - p1x*p2y - p1y*p3x + p2y*p3x + p1x*p3y - \
              p2x*p3y))
    oy = (p1x**2*p2x + p1y**2*p2x - p1x*p2x**2 - p1x*p2y**2 - \
            p1x**2*p3x - p1y**2*p3x + p2x**2*p3x + p2y**2*p3x + \
            p1x*p3x**2 - p2x*p3x**2 + p1x*p3y**2 - p2x*p3y**2)/ \
          (2.*(p1y*p2x - p1x*p2y - p1y*p3x + p2y*p3x + p1x*p3y - \
              p2x*p3y))
    return [ox,oy,math.sqrt(r2)]

def testCercleXY(p1,p2,p3):
    res = cercleXY(p1, p2, p3)
    print("cercle passant par " + str(p1) + " ; " + str(p2) + " ; " + str(p3) + " : " + str(res))
    print("verif : dist(c,p1) - r = " + str(math.sqrt((res[0]-p1[0])**2 + (res[1]-p1[1])**2 )-res[2]))
    print("verif : dist(c,p2) - r = " + str(math.sqrt((res[0]-p2[0])**2 + (res[1]-p2[1])**2 )-res[2]))
    print("verif : dist(c,p3) - r = " + str(math.sqrt((res[0]-p3[0])**2 + (res[1]-p3[1])**2 )-res[2]))
    
    
if __name__ == "__main__":
    testCercleXY([1,0],[0,1],[-1,0])
    testCercleXY([8,4],[7,11],[-3,4])
    # la ligne suivante générerait une exception si elle n'était pas commentée
    # testCercleXY([0,0],[1,1],[2,2])


                                        


