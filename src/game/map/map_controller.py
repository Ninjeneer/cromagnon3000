from game.map.map import Map

class MapController:

    def __init__(self):
        pass

    def init(self, file_path):
        self.map = Map()
        self.map.load_from_file(file_path)