import math
import numpy as np 
import time

from miney_toolbox import conv

""" create a horizontal rectangle of size w x h in the quadrant the player is 
looking at with the given material """
def rect( mt, pos, w, h, material ):

    positions = []

    vx= np.array([1,0,0])
    vz= np.array([0,0,1])

    for x in range(0,w):
        for z in range(0,h):
            f= pos + x*vx + z*vz

            positions.append( conv.ntom( f ) )

    mt.node.set( nodes= positions, name= material ) 
