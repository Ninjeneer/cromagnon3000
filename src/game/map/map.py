import json
import pygame as py
from math import floor, ceil
from utils import clear_config

NB_TILES_X = 8
NB_TILES_Y = 12


class Map:

    def __init__(self):
        self.tiles = []

    def load_from_file(self, file_path):
        with open(file_path, "r") as file:
            self.map_config = json.loads(file.read())

        self.tileset_img = py.image.load(self.map_config["tileset"]).convert_alpha()
        self.sprite_width = self.tileset_img.get_rect().width / NB_TILES_X
        self.sprite_height = self.tileset_img.get_rect().height / NB_TILES_Y

    def get_tile(self, bloc, zoom=1):
        tile = py.Rect(
            floor(bloc % NB_TILES_X) * self.sprite_width,
            floor(bloc / NB_TILES_X) * self.sprite_height,
            self.sprite_width,
            self.sprite_height
        )
        return tile
