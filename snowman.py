#!/usr/bin/python3

import sys
import math
import numpy as np 
import os

import miney
import miney_toolbox as mtb

if not miney.is_miney_available():
    raise miney.MinetestRunError("Please start Minetest with the miney game")

if not "MINETEST_USER" in os.environ:
    print("Please specific the player name in the 'MINETEST_USER' env variable.")
    exit(1)
if not "MINETEST_PASSWORD" in os.environ:
    print("Please specific the player name in the 'MINETEST_PASSWORD' env variable.")
    exit(1)

#mt = mt.Minetest( "localhost", "playername", "password", port= 29999 )
mt = miney.Minetest("localhost", 
    os.environ['MINETEST_USER'], os.environ['MINETEST_PASSWORD'] )

playername= ""
material= "wool:black"

# playername must be given
if len(sys.argv) > 1:
    playername= sys.argv[1]
else:
    print( "Playername not given, exit" )
    print( "Available players are" )
    for p in mt.player:
        print( p )
    exit(1)

player= mt.player[playername]

r1= 20
r2= 18
r3= 15

r4=21
r5=10

pos= mtb.pos_as_int( player )
dir= mtb.quadrant( player )


# lowest ball
base= pos + r2*dir
up= np.array([0,1,0])
base= base + (r1)*up
mtb.sphere( mt, base, r1, 0, "default:snowblock" )

# second ball
base= base + (r1-1)*up
base= base + (r2)*up
mtb.sphere( mt, base, r2, 0, "default:snowblock" )

# third ball
base= base + (r2-1)*up
base= base + (r3)*up
mtb.sphere( mt, base, r3, 0, "default:snowblock" )

# flat circle for hat
mtb.circle( mt, base, r4, r3-3, "wool:black" )

# cylinder for hat
for i in range(1,15):
    mtb.circle( mt, base, r5, r3-3+i, "wool:black" )

# nose
s2= np.sqrt(0.5)
front= np.array([-s2,0,-s2])
n= 12
for i in range(0,n):
    mtb.sphere( mt, base + (r3+i)*front, 2.0/n*(n-i), 0, "wool:orange" )

# eyes
lr= np.array([-s2,0,s2])
base= base + 6*up + (r3-2)*front
mtb.sphere( mt, base + 4*lr, 1, 0, "wool:black" )
mtb.sphere( mt, base - 4*lr, 1, 0, "wool:black" )
