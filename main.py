from agents.wardrobe_agent import WardrobeAgent

if __name__ == "__main__":
    wardrobe = WardrobeAgent()
    print("Your wardrobe contains:")
    for item in wardrobe.get_items():
        print(f"- {item['name']} ({item['type']})")
