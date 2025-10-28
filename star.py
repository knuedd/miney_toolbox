#!/usr/bin/env python3

import sys
import math
import numpy as np 
import os

import miney
import miney_toolbox as mtb

if not "MINETEST_USER" in os.environ:
    print("Please specific the player name in the 'MINETEST_USER' env variable.")
    exit(1)
if not "MINETEST_PASSWORD" in os.environ:
    print("Please specific the player name in the 'MINETEST_PASSWORD' env variable.")
    exit(1)

with miney.Luanti("localhost", os.environ['MINETEST_USER'], os.environ['MINETEST_PASSWORD'] ) as mt:

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

    if len(sys.argv) > 2:
        material= sys.argv[2]

    player= mt.players[playername]

    punkte=[ 
        [0,0,10], [2,0,3], [9,0,5], 
        [3,0,0], [9,0,-5], [2,0,-3], 
        [0,0,-10], [-2,0,-3], [-9,0,-5] ,
        [-3,0,0], [-9,0,5], [-2,0,3],
        [0,0,10]
        ]

    for i in range(len(punkte)-1):

        print("A ", punkte[i],punkte[i+1])
        start= np.array(punkte[i])
        end=   np.array(punkte[i+1])
        print("B ", start,end)
        mtb.line( mt, mtb.pos_as_int( player ), start, end, material )
