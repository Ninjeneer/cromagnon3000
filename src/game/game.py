import pygame as py
from game.map.map_controller import MapController
from game.ui.hud import Hud


class Game:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.map_controller: MapController = MapController()

        py.init()
        py.display.set_caption("Cromagnon 3000")

    def start(self):
        self.window: py.Surface = py.display.set_mode((self.width, self.height), py.DOUBLEBUF)
        self.map_controller.init("assets/maps/map00.json", self.window, self.width, self.height)
        self.map_controller.move_view_to_cell(0, 0)

        self.hud = Hud(self.window)

        run = True
        while run:
            self.map_controller.clear()
            event = py.event.poll()
            if event.type == py.constants.QUIT:
                run = False

            key_pressed = py.key.get_pressed()
            self.map_controller.handle_key(key_pressed)

            self.map_controller.draw()
            self.hud.display_life_bar(100)

            py.display.flip()
            py.time.wait(10)
            pass
