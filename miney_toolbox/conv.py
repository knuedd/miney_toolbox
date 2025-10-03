import math
import numpy as np 
import miney 
import time

""" transform numpy vector of len 3 to minetest position """
def ntom( f ):

    return { "x": float(f[0]), "y": float(f[1]), "z": float(f[2]) }

def ntonode( f, material="mcl_wool:red" ):

    return miney.node.Node( float(f[0]), float(f[1]), float(f[2]), name=material )