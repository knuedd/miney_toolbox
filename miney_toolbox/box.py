import sys
import math
import numpy as np 
import time

from miney_toolbox import conv

""" create a horizontal rectangle of size w x h in the quadrant the player is 
looking at with the given material """
def box( mt, pos, w, d, h, material ):

    positions = []

    vx= np.array([1,0,0])
    vy= np.array([0,1,0])
    vz= np.array([0,0,1])


    # bottom and top
    for x in range(0,w+1):
        for z in range(0,d+1):
            f= pos + x*vx + 0*vy + z*vz
            positions.append( conv.ntom( f ) )
            f= pos + x*vx + h*vy + z*vz
            positions.append( conv.ntom( f ) )

    # front and back
    for z in range(0,d+1):
        for y in range(0,h+1):
            f= pos + 0*vx + y*vy + z*vz 
            positions.append( conv.ntom( f ) )
            f= pos + w*vx + y*vy + z*vz 
            positions.append( conv.ntom( f ) )

    # two sides
    for x in range(0,w+1):
        for y in range(0,h+1):
            f= pos + x*vx + y*vy + 0*vz
            positions.append( conv.ntom( f ) )
            f= pos + x*vx + y*vy + d*vz
            positions.append( conv.ntom( f ) )

    mt.node.set( nodes= positions, name= material ) 
