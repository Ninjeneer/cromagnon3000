import pygame as py
from game.map.map import Map

class MapController:

    _shift_speed = 1.5

    def __init__(self):
        pass

    def init(self, file_path: str, window: py.Surface, width: int, height: int):

        self.width = width
        self.height = height
        self.window = window
        self.map = Map()
        self.map.load_from_file(file_path)

        self.shift_x = 0
        self.shift_y = 0

    def move_view_to_cell(self, cell_x: int, cell_y: int):
        self.shift_x = cell_x * self.map.sprite_width + self.width / 2
        self.shift_y = cell_y * self.map.sprite_height + self.height / 2

    def move(self, vector: tuple):
        self.shift_x += vector[0]
        self.shift_y += vector[1]

    def draw(self):
        map_structure: [int] = self.map.map_config["map"]
        for y in range(len(map_structure)):
            for x in range(len(map_structure[0])):
                tile = self.map.get_tile(map_structure[y][x])
                
                screen_x = x * self.map.sprite_width
                screen_y = y * self.map.sprite_height
                isometric_x = (x - y) * self.map.sprite_width / 2
                isometric_y = (x + y) * self.map.sprite_height / 2

                self.window.blit(self.map.tileset_img, (isometric_x + self.shift_x, isometric_y + self.shift_y), tile)

    def clear(self):
        self.window.fill(py.Color(0, 0, 0))

    def handle_key(self, key_pressed: []):
        if key_pressed[py.constants.K_z] or key_pressed[py.constants.K_UP]:
            self.move((0, MapController._shift_speed))

        if key_pressed[py.constants.K_s] or key_pressed[py.constants.K_DOWN]:
            self.move((0, -MapController._shift_speed))

        if key_pressed[py.constants.K_q] or key_pressed[py.constants.K_LEFT]:
            self.move((MapController._shift_speed, 0))

        if key_pressed[py.constants.K_d] or key_pressed[py.constants.K_RIGHT]:
            self.move((-MapController._shift_speed, 0))
