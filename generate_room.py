"""
This module defines a few classes, to be used 
primarily by the Resources class when its initialized.

Room: takes a file path that is a blueprint for
a room and creates it out of actual tile objects to be
drawn to the game screen. It's generic enough that we
could theoretically generate rooms at random and pass
them into this function.

Tile: a generic superclass for the various different
tile classes. Not much use right now but I created it
this way just in case general tile features would be 
needed at a later date.

Wall, Floor, Hole: three classes for the three different
tiles that I've created. In the future, each tile type
would be given its own subclass and functionality.
"""

import pygame
import constants as C

class Room(object):
    """
    Class that creates and maintains a room state.
    """
    def __init__(self, room_file):

        self.rm_structure = list() # Will be a list of lists

        #possibly entrances and exists from a room object
        self.left_available = True
        self.top_available = True
        self.right_available = True
        self.bottom_available = True

        # Open the room file and parse the contents
        row = list()

        x_coord = 0 
        y_coord = 0

        with open(room_file) as room_text:
            in_comment = False
            for line in room_text:
                if line[:2] == '$$':
                    if in_comment is False:
                        in_comment = True
                        continue
                    elif in_comment is True:
                        in_comment = False
                        continue
                else:
                    if in_comment is True:
                        continue
                    else:
                        for char in line:
                            print("Room.__init__(): creating tile with coords {},{}".format(x_coord, y_coord))
                            if char == 'x':
                                row.append(Wall(x=x_coord, y=y_coord))
                            elif char == '.':
                                row.append(Floor(x=x_coord, y=y_coord))
                            elif char == '0':
                                row.append(Hole(x=x_coord, y=y_coord))
                            x_coord += C.TILE_WIDTH
                    self.rm_structure.append(row)
                    row = []
                    x_coord = 0
                y_coord += C.TILE_HEIGHT

        # Draw the room tiles to a background surface stored by the room object
        self.floor = pygame.Surface((C.GAME_DISPLAY.get_size()))
        self.walls = pygame.Surface((C.GAME_DISPLAY.get_size()))

        for row in self.rm_structure:
            for column in row:
                if type(column) is Wall:
                    column.draw(self.walls)
                else:
                    column.draw(self.floor)

        # Mask out the parts of the wall surface that aren't walls
        self.walls.convert_alpha()
        self.walls.set_colorkey((0, 0, 0))


    def __str__(self):
        for i in self.rm_structure:
            for j in i:
                print(j, end="")
            print("")

class Tile(object):
    """
    Parent class for the different kinds of tiles that may be in the game
    """

    def __init__(self, x=0, y=0):
        self.coords = (x, y)


class Wall(Tile):
    """
    Basic wall objects. Has these properties:
    - Collides with everything
    - Does no damage
    - Kills projectiles
    """

    image = pygame.Surface((C.TILE_WIDTH, C.TILE_HEIGHT))
    image = pygame.image.load(C.T_WALL)

    def __init__(self, x=0, y=0):
        super(Wall, self).__init__(x, y)

    def __str__(self):
        """
        For debug purposes
        """
        return 'x'

    def draw(self, background):
        background.blit(Wall.image, self.coords)


class Floor(Tile):
    """
    Basic floor objects. Has these properties:
    - No collision, does not interact with sprites
    - Drawn under everything
    - Does no damage
    """

    image = pygame.Surface((C.TILE_WIDTH, C.TILE_HEIGHT))
    image = pygame.image.load(C.T_FLOOR)

    def __init__(self, x=0, y=0):
        super(Floor, self).__init__(x, y)

    def __str__(self):
        """
        For debug purposes
        """
        return '.'

    def draw(self, background):
        background.blit(Floor.image, self.coords)


class Hole(Tile):
    """
    Basic hole in the floor objects. Has these properties:
    - No collision but does interact with sprites
    - Drawn under everything
    - Does damage
    """

    image = pygame.Surface((C.TILE_WIDTH, C.TILE_HEIGHT))
    image = pygame.image.load(C.T_HOLE)

    def __init__(self, x=0, y=0):
        super(Hole, self).__init__(x, y)

    def __str__(self):
        """
        For debug purposes
        """
        return '0'

    def draw(self, background):
        background.blit(Hole.image, self.coords)
