import numpy as np 

import miney
from .conv import ntom

class MineyToolbox:
    """__init__([server, playername, password, [port]])

    :param str server: IP or DNS name of an minetest server with installed apisocket mod
    :param str playername: A name to identify yourself to the server.
    :param str password: Your password
    :param int port: The apisocket port, defaults to 29999
    """
    def __init__(self, server: str = "127.0.0.1", playername: str = None, password: str = "", port: int = 29999):
        """
        Connect to the minetest server.

        :param server: IP or DNS name of an minetest server with installed apisocket mod
        :param port: The apisocket port, defaults to 29999
        """

        if not miney.is_miney_available():
            raise miney.MinetestRunError("Miney not available, please start Minetest with miney enabled")

        self.mt= miney.Minetest(server, playername, password, port)
        self.playername= playername
        self.player= self.mt.player

    ## return position of player as numpy array
    def pos( self, playername: str = None ) -> np.array:

        if playername:
            p= self.player[playername].position
        else:
            p= self.player[self.playername].position

        #ret= np.array([ int(p['x']), int(p['y']), int(p['z']) ])
        ret= np.array([ p['x'], p['y'], p['z'] ])

        return ret

    """ create a line from 'start' to 'end' the given 'material',
    relative to the given position 'pos'
    adopted from https://github.com/pinae/BresenhamLidar """
    def line( self, pos, start, end, material ):

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

        error_per_step = (start_to_target_vector / np.abs(start_to_target_vector[steepest_dimension])) * step_size

        error = np.modf(start / step_size)[0]
        start_voxel = np.around(start / step_size, decimals=0)
        line_direction = int(start_to_target_vector[steepest_dimension] > 0) * 2 - 1

        positions.append( ntom( pos + start_voxel[0]*vx + start_voxel[1]*vy + start_voxel[2]*vz ) )

        current_voxel = np.copy(start_voxel)
        for i in range(length_in_steepest_dimension):
            np.add(error, error_per_step / step_size, out=error)
            step_dims = np.abs(error) >= 0.5
            step_dir = ((error > 0) * 2.0 - 1.0)
            np.subtract(error, step_dir, out=error, where=step_dims)
            np.add(current_voxel, step_dir, out=current_voxel, where=step_dims)
            positions.append( ntom( pos + current_voxel[0]*vx + current_voxel[1]*vy + current_voxel[2]*vz ) )

        self.mt.node.set( nodes= positions, name= material )


    """ place a list of blocks with the given material, 
    expects a list of 3-dim numpy vectors """
    def set( mt, pos, listofpositions, material ):

        positions = []

        for p in listofpositions:

            positions.append( ntom(pos+p) )

        self.mt.node.set( nodes= positions, name= material )
