import math
import numpy as np 
import miney
from miney import Minetest
import time

""" transform numpy vector of len 3 to minetest position """
def ntom( f ):

    return { "x": float(f[0]), "y": float(f[1]), "z": float(f[2]) }