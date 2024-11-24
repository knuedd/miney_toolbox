import sys
import math
import numpy as np 
import time
import json

from miney_toolbox import conv

""" read the positions in the box at pos +/- (w,d,h) """
def read( mt, pos, w, d, h ):

    vx= np.array([1,0,0])
    vy= np.array([0,1,0])
    vz= np.array([0,0,1])

    pos1= pos - w*vx - h*vy - d*vz
    pos2= pos + w*vx + h*vy + d*vz

    # fields= mt.node.get( pos1, pos2, relative= True )
    # print( fields )

    fields= mt.node.get( conv.ntom(pos1), conv.ntom(pos2), relative= True )
    print(  json.dumps(fields, indent= 4) )


""" copy the positions in the box from pos +/- (w,d,h) """
def copy( mt, pos, w, d, h ):

    vx= np.array([1,0,0])
    vy= np.array([0,1,0])
    vz= np.array([0,0,1])

    pos1= pos - w*vx - h*vy - d*vz
    pos2= pos + w*vx + h*vy + d*vz

    # fields= mt.node.get( pos1, pos2, relative= True )
    # print( fields )

    return mt.node.get( conv.ntom(pos1), conv.ntom(pos2), relative= True )

""" past the positions in the box at pos +/- (w,d,h), field is the 
contents as copied from copy() with relative= True """
def paste( mt, pos, field ):

    vx= np.array([1,0,0])
    vy= np.array([0,1,0])
    vz= np.array([0,0,1])

    return mt.node.set( nodes= field, offset= conv.ntom(pos) )
