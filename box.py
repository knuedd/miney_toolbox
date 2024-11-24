#!/usr/bin/env python3

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
material= "mcl_wool:red"

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

# if start and stop are not given print the players position and direction of view
if len(sys.argv) > 3:

    w= int( sys.argv[2] )
    d= int( sys.argv[3] )
    h= int( sys.argv[4] )

    if len(sys.argv) > 5:
        material= sys.argv[5]

    mtb.box( mt, mtb.pos_as_int( player ), w, d, h, material )

else:
    print( "Player %s" % playername )
    print( "    Position  ", mtb.pos_as_int(player) )
    print( "    Direction ", player.look_horizontal, player.look_vertical )
    print( "    Quadrant  ", mtb.quadrant( player ) )

