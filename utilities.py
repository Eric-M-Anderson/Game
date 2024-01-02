
class Utilities:
    @staticmethod
    def center_square(x, y, size):
        return x - (size / 2), y - (size / 2)

    @staticmethod
    def center_square_tile_square(world, tile_location_x, tile_location_y, object_size):
        return ((tile_location_x - 1) * world.get_tile_size()) + (world.get_tile_size() - object_size) / 2,\
               ((tile_location_y - 1) * world.get_tile_size()) + (world.get_tile_size() - object_size) / 2

    @staticmethod
    def center_square_tile_circle(world, tile_location_x, tile_location_y):
        return ((tile_location_x - 1) * world.get_tile_size()) + world.get_tile_size() / 2,\
               ((tile_location_y - 1) * world.get_tile_size()) + world.get_tile_size() / 2
