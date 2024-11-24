#!/usr/bin/env python3

import sys
import math
import numpy as np 
import time
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

print( "Players:")
for p in mt.player:
    print( p )

if len(sys.argv) <= 1:
    exit(0)

playername= sys.argv[1]
player= mt.player[playername]

if len(sys.argv) <= 2:

    print( "pos ", mtb.pos_as_int(player), 
        "\ndir ", player.look_horizontal, 
        "\nquad: ", mtb.quadrant( player ), 
        "\nup/down: ", player.look_vertical )

else: ## second arg given
    if "fly" == sys.argv[2]:
        print ( "Make player %sd fly" % playername )
        player.fly= True

    if "nodes" == sys.argv[2]:
        for node_type in mt.node.type:
            print(node_type)
