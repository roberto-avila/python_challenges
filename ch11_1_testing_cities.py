#-----Define a function on a separate file that prints out the a city's name, its country, and optionally, its population.
#Write a test below that will perform unit tests on different inputs.

from cities_function import formatted_city_name
import unittest

class TestCityNameCase(unittest.TestCase):
    """Test case for cities_function.py"""

    def test_city_country(self):
        """Do locations like Santiago, Chile work?"""
        result = formatted_city_name('santiago', 'chile')
        self.assertEqual(result, 'Santiago is located in Chile.')

    def test_city_country_population(self):
        """
        Do locations like San Salvador,
        El Salvador, population: 1_770_000 work?
        """
        result = formatted_city_name('san salvador', 'el salvador', 1_770_000)
        self.assertEqual(result, 'San Salvador is located in El Salvador. Population: 1770000')


if __name__ == '__main__':
    unittest.main()