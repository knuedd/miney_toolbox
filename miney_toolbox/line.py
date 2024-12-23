import math
import numpy as np 
import time

from miney_toolbox import conv

""" create a line from 'start' to 'end' the given 'material',
relative to the given position 'pos'
adopted from https://github.com/pinae/BresenhamLidar """
def line( mt, pos, start, end, material ):

    positions = []

    ## coordinate system
    vx= np.array([1,0,0])
    vy= np.array([0,1,0])
    vz= np.array([0,0,1])

    step_size=1.0
    start_to_target_vector = end - start

    error_dimensions = [0, 1, 2]
    steepest_dimension = error_dimensions.pop(np.argmax(np.abs(start_to_target_vector)))
    length_in_steepest_dimension= np.abs( end[steepest_dimension] - start[steepest_dimension] )

    #print("start_to_target_vector", start_to_target_vector, "  error_dimensions", error_dimensions)
    error_per_step = (start_to_target_vector / np.abs(start_to_target_vector[steepest_dimension])) * step_size
    #print("Error per step:", error_per_step)

    error = np.modf(start / step_size)[0]
    start_voxel = np.around(start / step_size, decimals=0)
    line_direction = int(start_to_target_vector[steepest_dimension] > 0) * 2 - 1

    positions.append( conv.ntom( pos + start_voxel[0]*vx + start_voxel[1]*vy + start_voxel[2]*vz ) )

    #print("Error at start:", error)
    current_voxel = np.copy(start_voxel)
    #print(current_voxel)
    for i in range(length_in_steepest_dimension):
        np.add(error, error_per_step / step_size, out=error)
        #print("i:", current_voxel[steepest_dimension], "Error:", error)
        step_dims = np.abs(error) >= 0.5
        step_dir = ((error > 0) * 2.0 - 1.0)
        #print("step_dims & step_dir", step_dims, step_dir)
        np.subtract(error, step_dir, out=error, where=step_dims)
        np.add(current_voxel, step_dir, out=current_voxel, where=step_dims)
        #print(current_voxel, "Error:", error)
        positions.append( conv.ntom( pos + current_voxel[0]*vx + current_voxel[1]*vy + current_voxel[2]*vz ) )

    mt.node.set( nodes= positions, name= material )


""" place a list of blocks with the given material, 
expects a list of 3-dim numpy vectors """
def set( mt, pos, listofpositions, material ):

    positions = []

    for p in listofpositions:

        positions.append( conv.ntom(pos+p) )

    mt.node.set( nodes= positions, name= material )
