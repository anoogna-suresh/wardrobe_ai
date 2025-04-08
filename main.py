from agents.wardrobe_agent import WardrobeAgent
from agents.weather_agent import WeatherAgent
from agents.style_agent import StyleAgent

if __name__ == "__main__":
    wardrobe = WardrobeAgent()
    weather = WeatherAgent(condition="rainy", temperature=15)
    style = StyleAgent(mood="lazy", occasion="casual")  # You can play with these

    context = weather.get_weather_context()
    print(f"Today's weather: {context['condition']}, feels {context['temp_label']}")
    print(f"Your mood is '{style.mood}', and you're dressing for a '{style.occasion}' occasion.\n")

    print("Recommended clothes from your wardrobe:")
    for item in wardrobe.get_items():
        temp_match = item.get("temp_label") == context["temp_label"] or item.get("season") == "all"
        style_match = style.match_style(item)
        if temp_match and style_match:
            print(f"- {item['name']} ({item['type']})")
