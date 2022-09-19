def formatted_city_name(city, country, population=0):
    """Returns a neatly formatted description of a city's location"""
    if population:
        return f"{city.title()} is located in {country.title()}. Population: {population}"
    else:
        return f"{city.title()} is located in {country.title()}."

print(formatted_city_name('san salvador', 'el salvador', 1_770_000))