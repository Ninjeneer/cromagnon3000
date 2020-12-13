import pygame as py

class StatusBar:
    def __init__(self):
        self.bar_width = 150
        self.bar_height = 10
        self.border_size = 5

    def conditional_color(self, conditional):
        self.conditional = conditional

    def render(self, value: int) -> py.Surface:
        container: py.Surface = py.Surface((self.bar_width + 2 * self.border_size, self.bar_height + 2 * self.border_size))
        inner_width = value * self.bar_width / 100 if value > 0 else 0
        py.draw.rect(container, py.Color(100, 100, 100), py.Rect(0, 0, self.bar_width + 2 * self.border_size, self.bar_height + 2 * self.border_size))
        py.draw.rect(container, self.conditional(value), py.Rect(self.border_size, self.border_size, inner_width, self.bar_height))
        return container

class Hud:

    def __init__(self, window: py.Surface):
        self.window = window

        self.life_bar = StatusBar()
        self.life_bar.conditional_color(lambda x: py.Color(255, 0, 0) if x < 25 else (py.Color(255, 128, 0) if x < 75 else py.Color(0, 255, 0)))

        self.hunger_bar = StatusBar()
        self.hunger_bar.conditional_color(lambda x: py.Color(0, 255, 0) if x < 25 else (py.Color(98, 15, 236) if x < 75 else py.Color(56, 143, 197)))

    def display_life_bar(self, life: int):
        self.window.blit(self.life_bar.render(life), (10, 20))
        self.window.blit(self.hunger_bar.render(life), (10, 50))