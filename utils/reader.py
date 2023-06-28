from typing import List
from models.city import City


def read_cities_from_file(filename: str) -> List[City]:
    cities = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                city_data = line.split()
                identifier = int(city_data[0])
                x = float(city_data[1])
                y = float(city_data[2])
                city = City(identifier, x, y)
                cities.append(city)

    return cities
