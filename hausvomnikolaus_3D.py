#!/usr/bin/env python3

import sys
import math
import numpy as np 
import os

from miney_toolbox import MineyToolbox

if not "MINETEST_USER" in os.environ:
    print("Please specific the player name in the 'MINETEST_USER' env variable.")
    exit(1)
if not "MINETEST_PASSWORD" in os.environ:
    print("Please specific the player name in the 'MINETEST_PASSWORD' env variable.")
    exit(1)

mtb = MineyToolbox("localhost", os.environ['MINETEST_USER'], os.environ['MINETEST_PASSWORD'] )

playername= ""

# playername must be given
if len(sys.argv) > 1:
    playername= sys.argv[1]
else:
    print( "Playername not given, exit" )
    print( "Available players are" )
    for p in mtb.player:
        print( p )
    exit(1)

# haus vom nikolaus
pos= mtb.pos(playername) + [2,0,2]
material= "wool:blue"

a=20
h=a//2

material= "wool:blue"
polygon= []
# nur eine Dimension ändert sich pro Zug
polygon.append( [0,0,0] )
polygon.append( [0,a,0] )
polygon.append( [a,a,0] )
polygon.append( [a,0,0] )
polygon.append( [a,0,a] )
polygon.append( [0,0,a] )
polygon.append( [0,a,a] )
polygon.append( [a,a,a] )

for i in range(len(polygon)-1):
    print(i,polygon[i],polygon[i+1])
    mtb.line( pos, np.array(polygon[i]), np.array(polygon[i+1]), material )

material= "wool:yellow"
polygon= []
# zwei Dimension ändern sich pro Zug
polygon.append( [a,a,a] )
polygon.append( [a,a,0] )
polygon.append( [h,a+h,h] )
polygon.append( [0,a,a] )
polygon.append( [a,0,a] )
polygon.append( [a,a,0] )
polygon.append( [0,0,0] )

for i in range(len(polygon)-1):
    print(i,polygon[i],polygon[i+1])
    mtb.line( pos, np.array(polygon[i]), np.array(polygon[i+1]), material )

material= "wool:orange"
polygon= []
# zwei Dimension ändern sich pro Zug
polygon.append( [0,0,0] )

polygon.append( [0,0,a] )
polygon.append( [a,0,0] )

for i in range(len(polygon)-1):
    print(i,polygon[i],polygon[i+1])
    mtb.line( pos, np.array(polygon[i]), np.array(polygon[i+1]), material )

material= "wool:green"
polygon= []
# zwei Dimension ändern sich pro Zug
polygon.append( [a,0,0] )
polygon.append( [0,0,0] )
polygon.append( [0,a,a] )
polygon.append( [0,a,0] )
polygon.append( [0,0,a] )
polygon.append( [a,a,a] )
polygon.append( [h,a+h,h] )
polygon.append( [0,a,0] )
polygon.append( [a,0,0] )
polygon.append( [a,a,a] )
polygon.append( [a,0,a] )
polygon.append( [0,0,0] )

for i in range(len(polygon)-1):
    print(i,polygon[i],polygon[i+1])
    mtb.line( pos, np.array(polygon[i]), np.array(polygon[i+1]), material )

