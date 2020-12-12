import pygame as py
from game.map.map import Map

class MapController:

    def __init__(self):
        pass

    def init(self, file_path):
        self.map = Map()
        self.map.load_from_file(file_path)

    def draw(self, window: py.Surface):
        py.draw.rect(window, py.Color(255, 0, 0), py.Rect(0, 0, 100, 100))
