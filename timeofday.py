#!/usr/bin/env python3

import sys
import math
import time
import os

import miney

if not "MINETEST_USER" in os.environ:
    print("Please specific the player name in the 'MINETEST_USER' env variable.")
    exit(1)
if not "MINETEST_PASSWORD" in os.environ:
    print("Please specific the player name in the 'MINETEST_PASSWORD' env variable.")
    exit(1)

#mt = mt.Minetest( "localhost", "playername", "password", port= 29999 )

try:
    with miney.Luanti("localhost", os.environ['MINETEST_USER'], os.environ['MINETEST_PASSWORD'] ) as mt:

        if len(sys.argv) > 1:
            time= int( sys.argv[1] )
            mt.time_of_day= time/24.0
        else:
            print( "Specify time of day as hour between 0 and 23")

except Exception as e:
        print(f"An unexpected error occurred: {e}")

