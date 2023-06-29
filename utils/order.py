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

def generate_neighbor(order, i, k):
    neighbor = []
    for j in range(i):
        #j Varia de 0 a i-1
        neighbor.append(order[j])
    for j in range(i, k+1):
        #j varia de i a k
        neighbor.append(order[k-j+i])
    for j in range(k+1, len(order)):
        #j varia de k+1 a n-1
        neighbor.append(order[j])
    return neighbor


def generate_neighborhood(order: List[int]) -> List[List[int]]:
    neighborhood = []
    for k in range (2, len(order) - 1):
        #k varia de 2 a n-2
        neighbor = generate_neighbor(order, 1, k)
        neighborhood.append(neighbor)
    for i in range(2, len(order) - 1):
        #i varia de 2 a n-2
        neighbor = generate_neighbor(order, i, k)
        neighborhood.append(neighbor)
    return neighborhood


def select_best_neighbor(cities: List[int], distances: np.ndarray, neighborhood: List[List[int]]) -> List[int]:
    best_order = neighborhood[0]
    best_distance = calculate_total_distance(cities, best_order, distances)

    for i in range(1, len(neighborhood)):
        new_order = neighborhood[i]
        new_distance = calculate_total_distance(cities, new_order, distances)
        if new_distance < best_distance:
            best_order = new_order
            best_distance = new_distance
    return best_order
