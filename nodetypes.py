#!/usr/bin/env python3

import sys
import math
import numpy as np 
import time
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

        for node_type in mt.nodes.names:
            print(node_type)
        print(f"We have {len(mt.nodes.names)} node types")

except Exception as e:
        print(f"An unexpected error occurred: {e}")
