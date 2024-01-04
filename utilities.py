
class Utilities:
    @staticmethod
    def center_square(x, y, size):
        return x - (size / 2), y - (size / 2)

    @staticmethod
    def center_square_tile_square(world, tile_location_x, tile_location_y, object_size, to_grid=False):
        if to_grid is False:
            return ((tile_location_x - 1) * world.get_tile_size()) + (world.get_tile_size() - object_size) / 2,\
                   ((tile_location_y - 1) * world.get_tile_size()) + (world.get_tile_size() - object_size) / 2
        elif to_grid is True:
            return tile_location_x / world.get_tile_size(), tile_location_y / world.get_tile_size()

    @staticmethod
    def center_square_tile_circle(world, tile_location_x, tile_location_y, to_grid=False):
        if to_grid is False:
            return ((tile_location_x - 1) * world.get_tile_size()) + world.get_tile_size() / 2, \
                   ((tile_location_y - 1) * world.get_tile_size()) + world.get_tile_size() / 2
        elif to_grid is True:
            return tile_location_x / world.get_tile_size(), tile_location_y / world.get_tile_size()
