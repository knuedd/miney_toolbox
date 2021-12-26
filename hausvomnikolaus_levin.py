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

# haus vom nikolaus
pos= mtb.pos_as_int( player )
material= "wool:blue"

a=20
b=20
c=10

start= np.array([1,1,1])
end=   np.array([1+a,1,1])
mtb.line( mt, pos, start, end, material )
start= np.array([1+a,1,1])
end=   np.array([1,1+b,1])
mtb.line( mt, pos, start, end, material )
start= np.array([1,1+b,1])
end=   np.array([1+a//2,1+b+c,1])
mtb.line( mt, pos, start, end, material )

start= np.array([1+a//2,1+b+c,1])
end=   np.array([1+a,1+b,1])
mtb.line( mt, pos, start, end, material )
start= np.array([1+a,1+b,1])
end=   np.array([1,1,1])
mtb.line( mt, pos, start, end, material )
start= np.array([1,1,1])
end=   np.array([1,1+b,1])
mtb.line( mt, pos, start, end, material )

start= np.array([1,1+b,1])
end=   np.array([1+a,1+b,1])
mtb.line( mt, pos, start, end, material )
start= np.array([1+a,1+b,1])
end=   np.array([1+a,1,1])
mtb.line( mt, pos, start, end, material )

