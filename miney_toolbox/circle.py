import math
import numpy as np 
import time

from miney_toolbox import conv

""" create a horizontal circle with radius r filled in with the given material,
the base is placed one step below the given position """
def circle( mt, pos, r, h, material ):

    positions = []

    vx= np.array([1,0,0])
    vy= np.array([0,1,0])
    vz= np.array([0,0,1])

    midpoint= pos + h*vy

    for x in range(0,int(r)+2):
        for z in range(0,int(r)+2):

                d= x*vx + z*vz
                a= np.linalg.norm( d )
                if a < r + 0.5 :
                    positions.append( conv.ntom( midpoint + x*vx + z*vz ) )
                    positions.append( conv.ntom( midpoint + x*vx - z*vz ) )
                    positions.append( conv.ntom( midpoint - x*vx + z*vz ) )
                    positions.append( conv.ntom( midpoint - x*vx - z*vz ) )

    mt.node.set( nodes= positions, name= material )
