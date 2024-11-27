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

mt = miney.Minetest("localhost", 
    os.environ['MINETEST_USER'], os.environ['MINETEST_PASSWORD'] )

playername= ""


# playername must be given
if len(sys.argv) > 2:
    player_src_name= sys.argv[1]
    player_dst_name= sys.argv[2]
else:
    print( "Playernames not given, exit" )
    print( "Available players are" )
    for p in mt.player:
        print( p )
    exit(1)

player_src= mt.player[player_src_name]
player_dst= mt.player[player_dst_name]

# if start and stop are not given print the players position and direction of view
if len(sys.argv) >= 5:

    w= int( sys.argv[3] )
    d= int( sys.argv[4] )
    h= int( sys.argv[5] )

    fields= mtb.copy( mt, mtb.pos_as_int( player_src ), w, d, h )
    mtb.paste( mt, mtb.pos_as_int( player_dst ), fields )

else:
    print( "Need to specify 2 players and w, h, d, abort" )

