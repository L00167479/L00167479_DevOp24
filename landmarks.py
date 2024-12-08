"class Landmark:" 
import datetime
import random

class Landmark:
    def __init__(self, name):
        self.name = name
        self.current_state = "Default"

    def update_state_based_on_time(self):
        """Update the landmark's appearance based on the time of day."""
        current_hour = datetime.datetime.now().hour
        if 6 <= current_hour < 12:
            self.current_state = "Morning Glow"
        elif 12 <= current_hour < 18:
            self.current_state = "Afternoon Brilliance"
        elif 18 <= current_hour < 21:
            self.current_state = "Evening Sunset"
        else:
            self.current_state = "Night Lights"

    def update_state_based_on_weather(self, weather):
        """Update the landmark's appearance based on the weather."""
        if weather == "Sunny":
            self.current_state = "Bright and Cheerful"
        elif weather == "Rainy":
            self.current_state = "Gloomy and Reflective"
        elif weather == "Snowy":
            self.current_state = "Covered in Snow"
        else:
            self.current_state = "Default Appearance"

    def display(self):
        """Display the current state of the landmark."""
        print(f"{self.name} is now in the state: {self.current_state}")


# Simulating the feature
def simulate_landmark_changes():
    # Create a landmark
    eiffel_tower = Landmark("Eiffel Tower")

    # Simulate time-based change
    eiffel_tower.update_state_based_on_time()
    eiffel_tower.display()

    # Simulate weather-based change
    simulated_weather = random.choice(["Sunny", "Rainy", "Snowy", "Cloudy"])
    print(f"Simulated Weather: {simulated_weather}")
    eiffel_tower.update_state_based_on_weather(simulated_weather)
    eiffel_tower.display()


if __name__ == "__main__":
    simulate_landmark_changes()
