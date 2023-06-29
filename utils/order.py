import random
import time
from typing import List
import numpy as np
from models.city import City


def calculate_total_distance(
    cities: List[City], order: List[int], distances: np.ndarray
) -> float:
    total_distance = 0
    num_cities = len(cities)

    for i in range(num_cities):
        current_city = order[i]
        next_city = order[(i + 1) % num_cities]
        total_distance += distances[current_city, next_city]

    return total_distance


def generate_random_order(num_cities: int) -> List[int]:
    order = list(range(num_cities))
    current_time = time.time()
    random.seed(current_time)
    random.shuffle(order)
    return order
