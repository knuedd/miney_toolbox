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

try:
    with miney.Luanti("localhost", os.environ['MINETEST_USER'], os.environ['MINETEST_PASSWORD'] ) as mt:

        playername= ""
        material= "mcl_wool:orange"

        # playername must be given
        if len(sys.argv) > 1:
            playername= sys.argv[1]
        else:
            print( "Playername not given, exit" )
            print( f"call as {sys.argv[0]} <playername> <width> <depth> <height>" )
            print( "Available players are" )
            for p in mt.players:
                print( p )
            exit(1)

        player= mt.players[playername]

        # if start and stop are not given print the players position and direction of view
        if len(sys.argv) > 2:

            a= 33
            b= 12
            c= 50

            if len(sys.argv) > 2:
                a= int( sys.argv[2] )
            if len(sys.argv) > 3:
                b= int( sys.argv[3] )
            if len(sys.argv) > 4:
                c= int( sys.argv[4] )
            if b >= a:
                print(f"Warning: b={b} >= a={a}")

            if len(sys.argv) > 5:
                material= sys.argv[5]

            nodelist= []

            playerpos= mtb.pos_as_int(player)

            y= -1

            for x in range(b+1):
                for z in range(b+1):

                    pos= playerpos + [z+a,y,x+a]
                    nodelist.append( mtb.ntonode( pos, material ) ) # jeden Block mit diesem Befehl zum zeichnen vormerken
                    pos= playerpos + [z-a,y,x+a]
                    nodelist.append( mtb.ntonode( pos, material ) ) 
                    pos= playerpos + [z+a,y,x-a]
                    nodelist.append( mtb.ntonode( pos, material ) )
                    pos= playerpos + [z-a,y,x-a]
                    nodelist.append( mtb.ntonode( pos, material ) ) 

            for i in range(b+1):

                pos= playerpos + [+a  ,y+1,+a+i]
                nodelist.append( mtb.ntonode( pos, material ) ) 
                pos= playerpos + [+a+b,y+1,+a+i]
                nodelist.append( mtb.ntonode( pos, material ) ) 
                pos= playerpos + [+a+i,y+1,+a  ]
                nodelist.append( mtb.ntonode( pos, material ) ) 
                pos= playerpos + [+a+i,y+1,+a+b]
                nodelist.append( mtb.ntonode( pos, material ) ) 

                pos= playerpos + [-a  ,y+1,+a+i]
                nodelist.append( mtb.ntonode( pos, material ) ) 
                pos= playerpos + [-a+b,y+1,+a+i]
                nodelist.append( mtb.ntonode( pos, material ) ) 
                pos= playerpos + [-a+i,y+1,+a  ]
                nodelist.append( mtb.ntonode( pos, material ) ) 
                pos= playerpos + [-a+i,y+1,+a+b]
                nodelist.append( mtb.ntonode( pos, material ) ) 

                pos= playerpos + [+a  ,y+1,-a+i]
                nodelist.append( mtb.ntonode( pos, material ) ) 
                pos= playerpos + [+a+b,y+1,-a+i]
                nodelist.append( mtb.ntonode( pos, material ) ) 
                pos= playerpos + [+a+i,y+1,-a  ]
                nodelist.append( mtb.ntonode( pos, material ) ) 
                pos= playerpos + [+a+i,y+1,-a+b]
                nodelist.append( mtb.ntonode( pos, material ) ) 

                pos= playerpos + [-a  ,y+1,-a+i]
                nodelist.append( mtb.ntonode( pos, material ) ) 
                pos= playerpos + [-a+b,y+1,-a+i]
                nodelist.append( mtb.ntonode( pos, material ) ) 
                pos= playerpos + [-a+i,y+1,-a  ]
                nodelist.append( mtb.ntonode( pos, material ) ) 
                pos= playerpos + [-a+i,y+1,-a+b]
                nodelist.append( mtb.ntonode( pos, material ) ) 

            mt.nodes.set( nodelist)

        else:
            print( f"call as {sys.argv[0]} {sys.argv[1]} <width> <depth> <height>" )
            print( "" )
            print( f"Info: Player {playername}" )
            print( "    Position  ", mtb.pos_as_int(player) )
            print( "    Direction ", player.look_horizontal, player.look_vertical )
            print( "    Quadrant  ", mtb.quadrant( player ) )

except Exception as e:
        print(f"An unexpected error occurred: {e}")
