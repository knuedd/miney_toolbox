#!/bin/bash


export MINETEST_USER="knue"
export MINETEST_PASSWORD=""

# vector addition example

# background
./circle.py knue 60 -1 default:snow

# example
./line.py knue 0 0 0 20 15 10 wool:orange
./line.py knue 0 0 0 5 10 5 wool:yellow
./line.py knue 0 0 0 15 5 5 wool:violet
./line.py knue 15 5 5 20 15 10 wool:yellow

# coordinate axes
./line.py knue 0 0 0 30 0 0 wool:red
./line.py knue 0 0 0 0 30 0 wool:green
./line.py knue 0 0 0 0 0 30 wool:blue
