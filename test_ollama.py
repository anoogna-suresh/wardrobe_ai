from chat import ask_ollama

weather = "rainy, feels cool"
mood = "cozy, low-energy"
wardrobe = ["grey hoodie", "black joggers", "white sneakers", "beige trench coat", "red scarf"]

print("Asking your AI wardrobe assistant...\n")
response = ask_ollama(weather, mood, wardrobe)
print(response)
