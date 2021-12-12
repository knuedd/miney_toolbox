import math
import numpy as np 
import time

from miney_toolbox import conv

""" create a sphere with radius r, the base is placed in position pos
looking at with the given material """
def sphere( mt, pos, r, h, material ):

    positions = []

    vx= np.array([1,0,0])
    vy= np.array([0,1,0])
    vz= np.array([0,0,1])

    midpoint= pos + h*vy 

    for x in range(0,int(r)+2):
        for z in range(0,int(r)+2):
            for y in range(0,int(r)+2):

                d= x*vx + y*vy + z*vz
                a= np.linalg.norm( d )
                if r - 0.5 <= a and a < r + 0.5 :
                    positions.append( conv.ntom( midpoint + x*vx + y*vy + z*vz ) )
                    positions.append( conv.ntom( midpoint + x*vx + y*vy - z*vz ) )
                    positions.append( conv.ntom( midpoint + x*vx - y*vy + z*vz ) )
                    positions.append( conv.ntom( midpoint + x*vx - y*vy - z*vz ) )
                    positions.append( conv.ntom( midpoint - x*vx + y*vy + z*vz ) )
                    positions.append( conv.ntom( midpoint - x*vx + y*vy - z*vz ) )
                    positions.append( conv.ntom( midpoint - x*vx - y*vy + z*vz ) )
                    positions.append( conv.ntom( midpoint - x*vx - y*vy - z*vz ) )

    mt.node.set( nodes= positions, name= material )
