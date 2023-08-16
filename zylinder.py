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
tiefe= 10
material_wand= "mcl_core:glass_white"
material_innen= "air"

# playername must be given
if len(sys.argv) > 1:
    playername= sys.argv[1]
else:
    print( "Playername not given, exit" )
    print( "Available players are" )
    for p in mt.player:
        print( p )
    exit(1)

if len(sys.argv) > 2:
    tiefe= int(sys.argv[2])

# materials can be given optionally
if len(sys.argv) > 3:
    material_wand= sys.argv[3]
if len(sys.argv) > 4:
    material_innen= sys.argv[4]

player= mt.player[playername]


X= np.array([1,0,0])
Y= np.array([0,1,0])
Z= np.array([0,0,1])

# Position des Spielers
P= np.array( mtb.pos_as_int( player ) )
print(P)


# Liste von Blöcken zum generieren
bloecke_wand= []
bloecke_innen= []

# hier die Blöcke ausrechnen

r=70
t=13

for y in range(0,tiefe+1):
    for x in range(-r-1,r+2):
        for z in range(-r-1,r+2):
            d=math.sqrt(x*x+z*z)
            if d<=r+0.5:
                if d<r-0.6:
                    bloecke_innen.append( mtb.conv.ntom(P+x*X+z*Z  -y*Y) )
                else:
                    bloecke_wand.append( mtb.conv.ntom(P+x*X+z*Z  -y*Y) )

    mt.node.set( nodes= bloecke_wand, name= material_wand )
    bloecke_wand= []
    mt.node.set( nodes= bloecke_innen, name= material_innen )
    bloecke_innen= []




