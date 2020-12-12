import pygame as py
from game.map.map_controller import MapController


class Game:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.map_controller: MapController = MapController()
        self.map_controller.init("assets/maps/map00.json")

        py.display.set_caption("Cromagnon 3000")

    def start(self):
        self.window: py.Surface = py.display.set_mode((self.width, self.height), py.DOUBLEBUF)
        while True:
            self.map_controller.draw(self.window)
            py.display.flip()
            pass
