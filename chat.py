from agents.wardrobe_agent import WardrobeAgent
from agents.weather_agent import WeatherAgent
from agents.style_agent import StyleAgent

import requests
from typing import List

def run_chat():
    print("👕 Welcome to your AI Wardrobe Assistant!")
    
    wardrobe = WardrobeAgent()
    
    while True:
        user_input = input("\n🧍 You: ").lower()

        if "bye" in user_input or "exit" in user_input:
            print("👋 Goodbye! Stay stylish.")
            break

        if "wear" in user_input:
            mood = input("What's your mood today? (e.g. chill, active): ")
            occasion = input("What's the occasion? (e.g. casual, formal): ")

            # (Later: use LLM to get this from natural input)

            weather = WeatherAgent(condition="rainy", temperature=15)  # You can randomize or use a mock
            context = weather.get_weather_context()
            style = StyleAgent(mood=mood, occasion=occasion)

            print(f"\n📍 Weather: {context['condition']}, feels {context['temp_label']}")
            print(f"🧠 Style: Mood = {mood}, Occasion = {occasion}")
            print("👕 Recommended outfit:")

            for item in wardrobe.get_items():
                temp_match = item.get("temp_label") == context["temp_label"] or item.get("season") == "all"
                style_match = style.match_style(item)
                if temp_match and style_match:
                    print(f"- {item['name']} ({item['type']})")
        
        else:
            print("🤖 I can help you pick an outfit. Just type something like 'What should I wear today?'")

def ask_ollama(weather: str, mood: str, wardrobe: List[str]) -> str:
    url = "http://localhost:11434/api/generate"
    system_prompt = (
        "You are an AI wardrobe assistant. Based on the user's current weather, mood, and wardrobe, "
        "suggest a stylish and comfortable outfit. Be specific, and explain your reasoning."
    )
    user_prompt = (
        f"The weather is {weather}, and the user feels {mood}. "
        f"Their wardrobe contains: {', '.join(wardrobe)}. "
        f"What should they wear today?"
    )

    data = {
        "model": "mistral",
        "prompt": f"{system_prompt}\n\n{user_prompt}",
        "stream": False
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "").strip()
    except requests.exceptions.RequestException as e:
        return f"Error talking to Ollama: {e}"

if __name__ == "__main__":
    run_chat()
