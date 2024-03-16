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

""" make a rectangle of the dimensions of 2 dim field F with a pattern
where F[,] is != 0 use 'material_full', otherwise 'material_empty' """
def rect_field( mt, pos, F, material_full, material_empty ):

    positions_full = []
    positions_empty = []

    vx= np.array([1,0,0])
    vz= np.array([0,0,1])

    w= F.shape[0]
    h= F.shape[1]

    for x in range(0,w):
        for z in range(0,h):

            f= pos + x*vx + z*vz
            if F[x,z] :
                positions_full.append( conv.ntom( f ) )
            else:
                positions_empty.append( conv.ntom( f ) )

    mt.node.set( nodes= positions_full, name= material_full )
    mt.node.set( nodes= positions_empty, name= material_empty )


""" make a rectangle of the dimensions of 2 dim field F with a pattern
where F[,] is != 0 use 'material_full', otherwise 'material_empty',
in addition use backbuffer B and only update fields where F[,] != B[,]
"""
def rect_field_backbuffer( mt, pos, F, B, material_full, material_empty ):

    positions_full = []
    positions_empty = []

    vx= np.array([1,0,0])
    vz= np.array([0,0,1])

    w= F.shape[0]
    h= F.shape[1]

    for x in range(0,w):
        for z in range(0,h):

            if F[x,z] == B[x,z]:
                continue

            f= pos + x*vx + z*vz
            if F[x,z] :
                positions_full.append( conv.ntom( f ) )
            else:
                positions_empty.append( conv.ntom( f ) )

    mt.node.set( nodes= positions_full, name= material_full )
    mt.node.set( nodes= positions_empty, name= material_empty )
