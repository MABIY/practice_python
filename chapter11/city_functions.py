"""A collection of function for working with cities."""

def city_country(city,country,population=None):
    """Return a string like 'Santiago, chile'."""
    output_string =  f"{city.title()}, {country.title()}"
    if population:
         output_string += f" - population {population}"
    return output_string

city_country("1","2")