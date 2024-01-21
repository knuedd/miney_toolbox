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
hoehe_turm= 22
hoehe_dach= 10
hoehe_etage= 5
material_wand= "mcl_walls:stonebrick_0"
material_dach= "mcl_nether:nether_brick"

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
    hoehe_turm= int(sys.argv[2])
if len(sys.argv) > 3:
    hoehe_dach= int(sys.argv[3])
if len(sys.argv) > 4:
    hoehe_etage= int(sys.argv[4])

# materials can be given optionally
if len(sys.argv) > 5:
    material_wand= sys.argv[5]
if len(sys.argv) > 6:
    material_dach= sys.argv[6]

player= mt.player[playername]


X= np.array([1,0,0])
Y= np.array([0,1,0])
Z= np.array([0,0,1])

# Position des Spielers
P= np.array( mtb.pos_as_int( player ) )
print(P)


# Liste von Blöcken zum generieren
bloecke_wand= []
bloecke_innen= []


breite=10
tiefe=10

# Wände hochmauern als Schleife, mit Etage alle soundso viel Reihen

for y in range(0,hoehe_turm):

    A= + X*breite//2 + Z*tiefe//2 + Y*y
    B= + X*breite//2 - Z*tiefe//2 + Y*y
    C= - X*breite//2 - Z*tiefe//2 + Y*y
    D= - X*breite//2 + Z*tiefe//2 + Y*y

    mtb.line( mt, P, A, B, material_wand )
    mtb.line( mt, P, B, C, material_wand )
    mtb.line( mt, P, C, D, material_wand )
    mtb.line( mt, P, D, A, material_wand )

    if 0 == y%hoehe_etage:

        for x in range(-breite//2,breite//2):

            E= X*x - Z*tiefe//2 + Y*y
            F= X*x + Z*tiefe//2 + Y*y
            mtb.line( mt, P, E, F, material_wand )

# Dach hochmauern

breite_dach= breite+4
S= Y*(hoehe_turm+hoehe_dach)

for l in range(-breite_dach//2,breite_dach//2+1):

    A= + X*breite_dach//2 + Z*l + Y*(hoehe_turm)
    B= - X*breite_dach//2 + Z*l + Y*(hoehe_turm)

    C= + X*l - Z*breite_dach//2 + Y*(hoehe_turm)
    D= + X*l + Z*breite_dach//2 + Y*(hoehe_turm)


    mtb.line( mt, P, A, S, material_dach )
    mtb.line( mt, P, B, S, material_dach )
    mtb.line( mt, P, C, S, material_dach )
    mtb.line( mt, P, D, S, material_dach )


