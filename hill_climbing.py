import sys
import time
import numpy as np
from typing import List
from utils.reader import read_cities_from_file
from utils.order import calculate_total_distance, generate_random_order
from models.city import City


def hill_climbing(cities: List[City], max_iterations: int) -> tuple[List[int], float]:
    num_cities = len(cities)
    current_order = generate_random_order(num_cities)
    best_order = current_order.copy()
    best_distance = calculate_total_distance(cities, best_order, distances)

    t = 0
    while t < max_iterations:
        local = False
        vc = current_order.copy()
        aval_vc = calculate_total_distance(cities, vc, distances)

        while not local:
            vn = None
            best_aval = float("inf")

            for i in range(num_cities):
                for j in range(i + 1, num_cities):
                    new_order = vc.copy()
                    new_order[i], new_order[j] = new_order[j], new_order[i]
                    aval = calculate_total_distance(cities, new_order, distances)

                    if aval < best_aval:
                        best_aval = aval
                        vn = new_order

            if best_aval < aval_vc:
                vc = vn
                aval_vc = best_aval
            else:
                local = True

        t += 1
        remaining_iterations = max_iterations - t

        print("Iteração:", t)
        print("Faltam", remaining_iterations, "iterações para terminar.")

        if aval_vc < best_distance:
            best_distance = aval_vc
            best_order = vc

    return best_order, best_distance


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Erro: Número de iterações não especificado.")
        print("Exemplo de uso: python main.py arquivo_de_entrada numero_iteracoes")
        sys.exit(1)

    input_file = sys.argv[1]
    max_iterations = int(sys.argv[2])

    cities = read_cities_from_file(input_file)
    num_cities = len(cities)

    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i, j] = cities[i].calculate_distance(cities[j])

    best_order, best_distance = hill_climbing(cities, max_iterations)

    print("Melhor ordem de visitação das cidades:", [city for city in best_order])
    print("Distância total percorrida:", best_distance)
