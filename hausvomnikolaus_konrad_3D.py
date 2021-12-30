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

# haus vom nikolaus

pos= mtb.pos_as_int( player )

a=12
h= 6

material= "wool:black"
polygon= []

# eine dimension ändert sich
polygon.append( [0,0,0] )
polygon.append( [0,a,0] )
polygon.append( [a,a,0] )
polygon.append( [a,0,0] )
polygon.append( [a,0,a] )
polygon.append( [a,a,a] )
polygon.append( [0,a,a] )
polygon.append( [0,0,a] )
 
for i in range(len(polygon)-1):
    print(i,polygon[i],polygon[i+1])
    mtb.line( mt, pos, np.array(polygon[i]), np.array(polygon[i+1]), material )
 
material= "wool:yellow"
polygon= []
 
# zwei dimensionen ändert sich
polygon.append( [0,0,a] )
polygon.append( [0,a,0] )
polygon.append( [h,a+h,h] )
polygon.append( [a,a,a] )
polygon.append( [a,0,0] )
polygon.append( [0,a,0] )

for i in range(len(polygon)-1):
    print(i,polygon[i],polygon[i+1])
    mtb.line( mt, pos, np.array(polygon[i]), np.array(polygon[i+1]), material )

material= "wool:green"
polygon= []
 
# zwei dimensionen ändert sich
polygon.append( [0,a,0] )
polygon.append( [0,a,a] )
polygon.append( [0,0,0] )
polygon.append( [a,a,0] )


for i in range(len(polygon)-1):
    print(i,polygon[i],polygon[i+1])
    mtb.line( mt, pos, np.array(polygon[i]), np.array(polygon[i+1]), material )

