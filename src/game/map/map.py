class Map:

    def __init__(self):
        self.tiles = []
    
    def load_from_file(self, file_path):
        with open(file_path, "r") as file:
            pass