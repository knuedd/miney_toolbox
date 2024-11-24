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
hoehe_default= 15
material_wand= "basic_materials:brass_block"
material_innen= "air"

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
    hoehe_default= int(sys.argv[2])

# materials can be given optionally
if len(sys.argv) > 3:
    material_wand= sys.argv[3]
if len(sys.argv) > 4:
    material_innen= sys.argv[4]

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

# hier die Blöcke ausrechnen


hoehe= hoehe_default
breite=45
tiefe=45
wandbreite=5

# Wände hochmauern als Schleife

for y in range(0,hoehe):

    A= + X*breite//2 + Z*tiefe//2 + Y*y
    B= + X*breite//2 - Z*tiefe//2 + Y*y
    C= - X*breite//2 - Z*tiefe//2 + Y*y
    D= - X*breite//2 + Z*tiefe//2 + Y*y

    mtb.line( mt, P, A, B, material_wand )
    mtb.line( mt, P, B, C, material_wand )
    mtb.line( mt, P, C, D, material_wand )
    mtb.line( mt, P, D, A, material_wand )

    A2= + X*(breite//2+wandbreite) + Z*(tiefe//2+wandbreite) + Y*y
    B2= + X*(breite//2+wandbreite) - Z*(tiefe//2+wandbreite) + Y*y
    C2= - X*(breite//2+wandbreite) - Z*(tiefe//2+wandbreite) + Y*y
    D2= - X*(breite//2+wandbreite) + Z*(tiefe//2+wandbreite) + Y*y

    mtb.line( mt, P, A2, B2, material_wand )
    mtb.line( mt, P, B2, C2, material_wand )
    mtb.line( mt, P, C2, D2, material_wand )
    mtb.line( mt, P, D2, A2, material_wand )

    A3= P + X*(breite//2+wandbreite//2) + Z*(tiefe//2+wandbreite//2) + Y*y
    B3= P + X*(breite//2+wandbreite//2) - Z*(tiefe//2+wandbreite//2) + Y*y
    C3= P - X*(breite//2+wandbreite//2) - Z*(tiefe//2+wandbreite//2) + Y*y
    D3= P - X*(breite//2+wandbreite//2) + Z*(tiefe//2+wandbreite//2) + Y*y

    mtb.circle( mt, A3, 10, 0, "air" )
    mtb.circle( mt, B3, 10, 0, "air" )
    mtb.circle( mt, C3, 10, 0, "air" )
    mtb.circle( mt, D3, 10, 0, "air" )
    mtb.circle_empty( mt, A3, 10, 0, material_wand )
    mtb.circle_empty( mt, B3, 10, 0, material_wand )
    mtb.circle_empty( mt, C3, 10, 0, material_wand )
    mtb.circle_empty( mt, D3, 10, 0, material_wand )

# Oberste Schicht geschlossen

y= hoehe

for w in range(-1,wandbreite+2):

    A2= + X*(breite//2+w) + Z*(tiefe//2+w) + Y*y
    B2= + X*(breite//2+w) - Z*(tiefe//2+w) + Y*y
    C2= - X*(breite//2+w) - Z*(tiefe//2+w) + Y*y
    D2= - X*(breite//2+w) + Z*(tiefe//2+w) + Y*y

    mtb.line( mt, P, A2, B2, material_wand )
    mtb.line( mt, P, B2, C2, material_wand )
    mtb.line( mt, P, C2, D2, material_wand )
    mtb.line( mt, P, D2, A2, material_wand )

A3= P + X*(breite//2+wandbreite//2) + Z*(tiefe//2+wandbreite//2) + Y*y
B3= P + X*(breite//2+wandbreite//2) - Z*(tiefe//2+wandbreite//2) + Y*y
C3= P - X*(breite//2+wandbreite//2) - Z*(tiefe//2+wandbreite//2) + Y*y
D3= P - X*(breite//2+wandbreite//2) + Z*(tiefe//2+wandbreite//2) + Y*y

mtb.circle( mt, A3, 11, 0, material_wand )
mtb.circle( mt, B3, 11, 0, material_wand )
mtb.circle( mt, C3, 11, 0, material_wand )
mtb.circle( mt, D3, 11, 0, material_wand )

# Geländer auf der obersten Schicht

for y in range(hoehe+1,hoehe+3):

    A= + X*(breite//2-1) + Z*(tiefe//2-1) + Y*y
    B= + X*(breite//2-1) - Z*(tiefe//2-1) + Y*y
    C= - X*(breite//2-1) - Z*(tiefe//2-1) + Y*y
    D= - X*(breite//2-1) + Z*(tiefe//2-1) + Y*y

    mtb.line( mt, P, A, B, material_wand )
    mtb.line( mt, P, B, C, material_wand )
    mtb.line( mt, P, C, D, material_wand )
    mtb.line( mt, P, D, A, material_wand )

    A2= + X*(breite//2+wandbreite+1) + Z*(tiefe//2+wandbreite+1) + Y*y
    B2= + X*(breite//2+wandbreite+1) - Z*(tiefe//2+wandbreite+1) + Y*y
    C2= - X*(breite//2+wandbreite+1) - Z*(tiefe//2+wandbreite+1) + Y*y
    D2= - X*(breite//2+wandbreite+1) + Z*(tiefe//2+wandbreite+1) + Y*y

    mtb.line( mt, P, A2, B2, material_wand )
    mtb.line( mt, P, B2, C2, material_wand )
    mtb.line( mt, P, C2, D2, material_wand )
    mtb.line( mt, P, D2, A2, material_wand )

    A3= P + X*(breite//2+wandbreite//2) + Z*(tiefe//2+wandbreite//2) + Y*y
    B3= P + X*(breite//2+wandbreite//2) - Z*(tiefe//2+wandbreite//2) + Y*y
    C3= P - X*(breite//2+wandbreite//2) - Z*(tiefe//2+wandbreite//2) + Y*y
    D3= P - X*(breite//2+wandbreite//2) + Z*(tiefe//2+wandbreite//2) + Y*y

    mtb.circle( mt, A3, 11, 0, "air" )
    mtb.circle( mt, B3, 11, 0, "air" )
    mtb.circle( mt, C3, 11, 0, "air" )
    mtb.circle( mt, D3, 11, 0, "air" )
    mtb.circle_empty( mt, A3, 11, 0, material_wand )
    mtb.circle_empty( mt, B3, 11, 0, material_wand )
    mtb.circle_empty( mt, C3, 11, 0, material_wand )
    mtb.circle_empty( mt, D3, 11, 0, material_wand )


