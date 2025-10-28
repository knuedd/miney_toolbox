import sys
import math
import numpy as np 
import time

import miney_toolbox as mtb

""" create a horizontal rectangle of size w x h in the quadrant the player is 
looking at with the given material """
def box( mt, pos, w, d, h, material ):

    nodelist = []

    vx= np.array([1,0,0])
    vy= np.array([0,1,0])
    vz= np.array([0,0,1])

    # bottom and top
    for x in range(0,w+1):
        for z in range(0,d+1):
            f= pos + x*vx + 0*vy + z*vz
            nodelist.append( mtb.ntonode( f, material ) )
            f= pos + x*vx + h*vy + z*vz
            nodelist.append( mtb.ntonode( f, material ) )

    # front and back
    for z in range(0,d+1):
        for y in range(0,h+1):
            f= pos + 0*vx + y*vy + z*vz 
            nodelist.append( mtb.ntonode( f, material ) )
            f= pos + w*vx + y*vy + z*vz 
            nodelist.append( mtb.ntonode( f, material ) )

    # two sides
    for x in range(0,w+1):
        for y in range(0,h+1):
            f= pos + x*vx + y*vy + 0*vz
            nodelist.append( mtb.ntonode( f, material ) )
            f= pos + x*vx + y*vy + d*vz
            nodelist.append( mtb.ntonode( f, material ) )

    mt.nodes.set( nodelist )

