import pygame as py
from game.map.map_controller import MapController


class Game:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.map_controller: MapController = MapController()

        py.init()
        py.display.set_caption("Cromagnon 3000")

    def start(self):
        self.map_controller.init("assets/maps/map00.json", self.width, self.height)
        self.map_controller.move_view_to_cell(0, 0)

        run = True

        while run:
            self.map_controller.clear()
            event = py.event.poll()
            if event.type == py.constants.QUIT:
                run = False

            key_pressed = py.key.get_pressed()
            self.map_controller.handle_key(key_pressed)

            self.map_controller.draw()
            py.display.flip()
            pass
