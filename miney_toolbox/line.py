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

    # don't need this here, remove again later
    array = np.zeros((10, 10, 10), dtype=np.float32)

    start_to_target_vector = end - start
    error_dimensions = list(range(len(array.shape)))
    #print("array.shape ", array.shape)
    #print("error_dimension ", error_dimensions)
    steepest_dimension = error_dimensions.pop(np.argmax(np.abs(start_to_target_vector)))
    #print("start_to_target_vector", start_to_target_vector, "  error_dimensions", error_dimensions)
    error_per_step = (start_to_target_vector / np.abs(start_to_target_vector[steepest_dimension])) * step_size
    #print("Error per step:", error_per_step)
    
    error = np.modf(start / step_size)[0]
    start_voxel = np.around(start / step_size, decimals=0)
    line_direction = int(start_to_target_vector[steepest_dimension] > 0) * 2 - 1

    #voxels = [start_voxel]
    positions.append( conv.ntom( pos + start_voxel[0]*vx + start_voxel[1]*vy + start_voxel[2]*vz ) )

    #print("Error at start:", error)
    current_voxel = np.copy(start_voxel)
    #print(current_voxel)
    while True:
        np.add(error, error_per_step / step_size, out=error)
        #print("i:", current_voxel[steepest_dimension], "Error:", error)
        step_dims = np.abs(error) >= 0.5
        step_dir = ((error > 0) * 2.0 - 1.0)
        #print("step_dims & step_dir", step_dims, step_dir)
        np.subtract(error, step_dir, out=error, where=step_dims)
        np.add(current_voxel, step_dir, out=current_voxel, where=step_dims)
        #print(current_voxel, "Error:", error)
        if np.any(current_voxel < 0) or np.any(current_voxel > np.array(array.shape, dtype=np.float32)): 
            break
        #voxels.append(np.copy(current_voxel))
        positions.append( conv.ntom( pos + current_voxel[0]*vx + current_voxel[1]*vy + current_voxel[2]*vz ) )

    mt.node.set( nodes= positions, name= material )
 
