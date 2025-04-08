class StyleAgent:
    def __init__(self, mood="chill", occasion="casual"):
        self.mood = mood.lower()
        self.occasion = occasion.lower()

    def match_style(self, clothing_item):
        # For now, match occasion with clothing "style"
        return clothing_item.get("style", "").lower() == self.occasion
