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

# trunk

h1= 40
r1= 3
h2= 40
r2= 2
h3= 40
r3= 1
h4= 40
r4= 0.5

pos= mtb.pos_as_int( player )
dir= mtb.quadrant( player )

base= pos + r1*dir

for i in range(0,h1):
    mtb.circle( mt, base, r1, i, "default:pine_wood" )

for i in range(h1,h1+h2):
    mtb.circle( mt, base, r2, i, "default:pine_wood" )

for i in range(h1+h2,h1+h2+h3):
    mtb.circle( mt, base, r3, i, "default:pine_wood" )

for i in range(h1+h2+h3,h1+h2+h3+h4):
    mtb.circle( mt, base, r4, i, "default:pine_wood" )


# leaves

step =5
rmin= 1
rmax= 30.0
h0= h1
hh= h2+h3+h4

for i in range(0,hh,step):
    r= rmin + rmax*i/hh
    mtb.circle( mt, base, r, h0+hh-i, "wool:dark_green" )

mtb.circle( mt, base, rmin, h0+hh+1, "wool:dark_green" )
mtb.circle( mt, base, rmin, h0+hh+1, "wool:dark_green" )
mtb.circle( mt, base, 0.5, h0+hh+2, "wool:dark_green" )
mtb.circle( mt, base, 0.5, h0+hh+3, "wool:dark_green" )
mtb.circle( mt, base, 0.5, h0+hh+4, "wool:dark_green" )
mtb.circle( mt, base, 0.5, h0+hh+5, "wool:dark_green" )
