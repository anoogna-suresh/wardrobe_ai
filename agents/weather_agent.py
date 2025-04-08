class WeatherAgent:
    def __init__(self, condition="sunny", temperature=22):
        # For now, you can manually change this or hook to weather API later
        self.condition = condition.lower()
        self.temperature = temperature

    def get_weather_context(self):
        if self.temperature < 10:
            temp_label = "cold"
        elif 10 <= self.temperature < 20:
            temp_label = "cool"
        elif 20 <= self.temperature < 30:
            temp_label = "warm"
        else:
            temp_label = "hot"

        return {
            "condition": self.condition,
            "temperature": self.temperature,
            "temp_label": temp_label
        }
