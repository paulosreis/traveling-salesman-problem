import os
import sys
import numpy as np
from typing import List
from utils.output_writer import save_output_to_file
from utils.reader import read_cities_from_file
from utils.order import calculate_total_distance, generate_random_order
from models.city import City


def hill_climbing(cities: List[City], max_iterations: int) -> tuple[List[int], float]:
    num_cities = len(cities)
    best_order = generate_random_order(num_cities)
    best_distance = calculate_total_distance(cities, best_order, distances)

    t = 0
    while t < max_iterations:
        current_order = generate_random_order(num_cities)
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

                    if aval < best_aval and len(set(new_order)) == num_cities:
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

    # Criar a pasta "output" se não existir
    output_folder = "output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Gerar o nome do arquivo de saída
    input_filename = os.path.basename(input_file)
    output_filename = "hillclimbing_out_" + input_filename

    save_output_to_file(output_folder, output_filename, max_iterations, best_order, best_distance)