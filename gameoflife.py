#!/usr/bin/env python3

import sys
import math
import numpy as np 
import os

import miney
import miney_toolbox as mtb
import time


def gameoflife( F, B ):

    assert( F.shape == B.shape )

    # print("pre:")
    # print(F)

    w= F.shape[0]
    d= F.shape[1]

    B[:,:]= 0

    for x in range(1,w-1):
        for z in range(1,d-1):

            neighbors= 0
            neighbors += F[x-1,z-1]
            neighbors += F[x-1,z  ]
            neighbors += F[x-1,z+1]
            neighbors += F[x  ,z-1]
            neighbors += F[x  ,z+1]
            neighbors += F[x+1,z-1]
            neighbors += F[x+1,z  ]
            neighbors += F[x+1,z+1]
            #print(x,z,": ",F[x,z]," # ", neighbors)

            if 1 == F[x,z] : # cell was alive
                #print("    was alive")
                if 2 <= neighbors and neighbors <= 3:
                    B[x,z]= 1
            else: # cell was dead
                #print("    was dead")
                if 3 == neighbors:
                    B[x,z]= 1

    # print("post:")
    # print("    ",B)
    return B


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
material_background= "wool:grey"
material_true= "wool:red"
material_false= "air"
w= 40
d= 40

# playername must be given
if len(sys.argv) > 1:
    playername= sys.argv[1]
else:
    print( "Usage:", sys.argv[0], " <playername|\"help\"> [<width> <deepth>] [<material_true> <material_false> <material_background]" )
    exit(1)

if "help" == playername:
    print( "Available players are" )
    for p in mt.player:
        print( p )
    exit(0)

player= mt.player[playername]

# if start and stop are not given print the players position and direction of view
if len(sys.argv) > 3:

    w= int( sys.argv[2] )
    d= int( sys.argv[3] )

if len(sys.argv) > 4:
    material_true= sys.argv[4]
    material_false= sys.argv[5]
    material_background= sys.argv[6]

P= mtb.pos_as_int( player )

X= np.array([1,0,0]) # forward
Y= np.array([0,1,0]) # up
Z= np.array([0,0,1]) # sideways

P= mtb.pos_as_int( player ) - w//2 * X - d//2 * Z - 10*Y

print( "Player %s" % playername )
print( "    Position  ", mtb.pos_as_int(player) )
print( "    Direction ", player.look_horizontal, player.look_vertical )
print( "    Quadrant  ", mtb.quadrant( player ) )

mtb.rect( mt, P-2*Y, w, d, material_background )

F= np.zeros((w,d),dtype=int) # playing field for game of life
B= np.zeros((w,d),dtype=int) # backbuffer
N= np.zeros((w,d),dtype=int) # new field

# init space glider
F[w//2:w//2+3,d//2]= 1
F[w//2,d//2+1]= 1
F[w//2+1,d//2+2]= 1

# init row
F[w//2+4:w//2+7,d//2+5]= 1

mtb.rect_field( mt, P, F, material_true, material_false )
time.sleep(3)

for t in range(1,60):

    N[:,:]= gameoflife( F, B )

    mtb.rect_field_backbuffer( mt, P, N, F, material_true, material_false )
    time.sleep(0.5)

    F[:,:]= N[:,:]
