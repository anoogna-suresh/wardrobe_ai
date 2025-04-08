import json

class WardrobeAgent:
    def __init__(self, file_path="data/wardrobe.json"):
        self.file_path = file_path
        self.wardrobe = self.load_wardrobe()

    def load_wardrobe(self):
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def get_items(self):
        return self.wardrobe
