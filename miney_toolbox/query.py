import math
import numpy as np 
import miney
import time

## return position of player as numpy array
def pos( player ) -> np.array:

    p= player.position

    ret= np.array([ p['x'], p['y'], p['z'] ])

    return ret

## return position of player as numpy array
def pos_as_int( player ) -> np.array:

    p= player.position

    ret= np.array([ int(p['x']), int(p['y']), int(p['z']) ])

    return ret

## return the quadrant the player is looking at as an vector of len 3
## x and z coordinates are -1 or +1, the y coordinate (vertical is always 0)
def quadrant( player ) -> np.array:

    ret= np.array([0,0,0])

    h= player.look_horizontal

    if 0 <= h and h < math.pi:
        ret[0]= -1
    else:
        ret[0]= +1

    if math.pi*0.5 <= h and h < math.pi*1.5:
        ret[2]= -1
    else:
        ret[2]= +1

    return ret
