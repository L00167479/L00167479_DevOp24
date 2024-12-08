import unittest
from landmarks import Landmark

class TestLandmark(unittest.TestCase):
    def test_update_state_based_on_time(self):
        landmark = Landmark("Eiffel Tower")
        landmark.update_state_based_on_time()
        self.assertIn(
            landmark.current_state,
            ["Morning Glow", "Afternoon Brilliance", "Evening Sunset", "Night Lights"]
        )

    def test_update_state_based_on_weather(self):
        landmark = Landmark("Eiffel Tower")
        landmark.update_state_based_on_weather("Sunny")
        self.assertEqual(landmark.current_state, "Bright and Cheerful")
        landmark.update_state_based_on_weather("Rainy")
        self.assertEqual(landmark.current_state, "Gloomy and Reflective")
        landmark.update_state_based_on_weather("Snowy")
        self.assertEqual(landmark.current_state, "Covered in Snow")
        landmark.update_state_based_on_weather("Cloudy")
        self.assertEqual(landmark.current_state, "Default Appearance")

if __name__ == "__main__":
    unittest.main()
