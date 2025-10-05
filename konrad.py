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
        print( f"call as {sys.argv[0]} <playername> [total width/2] [width of tower] [height of tower] [width of wall] [height of wall]" )
        print( "Available players are" )
        for p in mt.players:
            print( p )
        exit(1)

    player= mt.players[playername]

    # if start and stop are not given print the players position and direction of view
    if len(sys.argv) > 1:

        a= 36 # Gesamtbreite /2
        b= 12 # Turmbreite
        c= 10 # Höhe des Turms
        d= 6 # Breite der Mauer
        e= 5 # Höhe der Mauer

        if len(sys.argv) > 2:
            a= int( sys.argv[2] )
        if len(sys.argv) > 3:
            b= int( sys.argv[3] )
        if len(sys.argv) > 4:
            c= int( sys.argv[4] )
        if len(sys.argv) > 5:
            d= int( sys.argv[5] )
        if len(sys.argv) > 6:
            e= int( sys.argv[6] )


        if b >= a:
            print(f"Warning: b={b} >= a={a}")

        if len(sys.argv) > 5:
            material= sys.argv[5]

        nodelist= []

        playerpos= mtb.pos_as_int(player)

        y= -1
                    #turm
        for x in range(b+1):
            for z in range(b+1):

                for sx in [-1,1]:

                    ox= 0 if sx > 0 else -1

                    for sz in [-1,1]:

                        oz= 0 if sz > 0 else -1

                        pos= playerpos + [sx*(a-x)+ox,y,sz*(a-z)+oz]
                        nodelist.append( mtb.ntonode( pos, material ) ) # jeden Block mit diesem Befehl zum zeichnen vormerken
        mt.nodes.set( nodelist)
        nodelist= []

        for y in range(c):
            for i in range(b+1):

                for sx in [-1,1]:

                    ox= 0 if sx > 0 else -1

                    for sz in [-1,1]:

                        oz= 0 if sz > 0 else -1

                        pos= playerpos + [sx*(a-i)+ox,y,sz*a    +oz]
                        nodelist.append( mtb.ntonode( pos, material ) ) 
                        pos= playerpos + [sx*(a-i)+ox,y,sz*(a-b)+oz]
                        nodelist.append( mtb.ntonode( pos, material ) ) 
                        pos= playerpos + [sx*a    +ox,y,sz*(a-i)+oz]
                        nodelist.append( mtb.ntonode( pos, material ) ) 
                        pos= playerpos + [sx*(a-b)+ox,y,sz*(a-i)+oz]
                        nodelist.append( mtb.ntonode( pos, material ) ) 

            mt.nodes.set( nodelist)
            nodelist= []
                            #Mauer
        for y in range(e):

            for sx in [-1,1]:

                ox= 0 if sx > 0 else -1

                for sz in [-1,1]:

                    oz= 0 if sz > 0 else -1

                    step= 2 # Mauer einrücken von der Außenkante des Turms aus gezählt
                    for i in range(1,a-b):

                        pos= playerpos + [sx*(a-b-i)+ox,y,sz*(a-step)+oz]#x,y,z
                        nodelist.append( mtb.ntonode( pos, material ) ) 
                        pos= playerpos + [sx*(a-b-i)+ox,y,sz*(a-step-d)+oz]
                        nodelist.append( mtb.ntonode( pos, material ) ) 
                        
                        pos= playerpos + [sx*(a-step)+ox,y,sz*(a-b-i)+oz]
                        nodelist.append( mtb.ntonode( pos, material ) ) 
                        pos= playerpos + [sx*(a-step-d)+ox,y,sz*(a-b-i)+oz]
                        nodelist.append( mtb.ntonode( pos, material ) ) 

                        if 0 == i%6:
                            for ee in range(3):
                                step += 1

                                pos= playerpos + [sx*(a-b-i)+ox,y,sz*(a-step)+oz]
                                nodelist.append( mtb.ntonode( pos, material ) ) 
                                pos= playerpos + [sx*(a-b-i)+ox,y,sz*(a-step-d)+oz]
                                nodelist.append( mtb.ntonode( pos, material ) ) 

                                pos= playerpos + [sx*(a-step)+ox,y,sz*(a-b-i)+oz]
                                nodelist.append( mtb.ntonode( pos, material ) ) 
                                pos= playerpos + [sx*(a-step-d)+ox,y,sz*(a-b-i)+oz]
                                nodelist.append( mtb.ntonode( pos, material ) ) 

                    i = a-b

                    pos= playerpos + [sx*(a-b-i)+ox,y,sz*(a-step)+oz]
                    nodelist.append( mtb.ntonode( pos, material ) ) 
                    pos= playerpos + [sx*(a-b-i)+ox,y,sz*(a-step-d)+oz]
                    nodelist.append( mtb.ntonode( pos, material ) ) 

                    pos= playerpos + [sx*(a-step)+ox,y,sz*(a-b-i)+oz]
                    nodelist.append( mtb.ntonode( pos, material ) ) 
                    pos= playerpos + [sx*(a-step-d)+ox,y,sz*(a-b-i)+oz]
                    nodelist.append( mtb.ntonode( pos, material ) ) 


                    mt.nodes.set( nodelist)
                    nodelist= []


    else:
        print( f"call as {sys.argv[0]} {sys.argv[1]} [a] [b] [c]" )
        print( "" )
        print( f"Info: Player {playername}" )
        print( "    Position  ", mtb.pos_as_int(player) )
        print( "    Direction ", player.look_horizontal, player.look_vertical )
        print( "    Quadrant  ", mtb.quadrant( player ) )

