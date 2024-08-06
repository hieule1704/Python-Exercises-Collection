def formated_city_country(city, country, population=''):
    if population:
        full_name = f"{city}, {country} - Population {population}"
    else:
        full_name = f"{city}, {country}"
    return full_name.title()

