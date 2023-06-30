from typing import List
from utils.order import generate_random_order, calculate_total_distance, select_best_neighbor, generate_neighborhood
from utils.reader import read_cities_from_file
import random
import math
from models.city import City
import sys
import numpy as np

def simulated_annealing(cities: List[City], TMax:float, k: float, Kt: int, TMin:float) -> tuple[List[int], float]:
    #Inicializa T
    T = TMax

    #Selecionar um ponto corrente vc de forma aleatória e definir seu valor de avaliação
    vc = generate_random_order(len(cities))
    aval_vc = calculate_total_distance(cities, vc, distances)
    while T > TMin:
        t = 0
        while t <  Kt:
            #Seleciona um novo ponto vn em N(vc)
            neighborhood = generate_neighborhood(vc)
            vn = select_best_neighbor(cities, distances, neighborhood)
            best_aval = calculate_total_distance(cities, vn, distances)

            if best_aval < aval_vc:
                vc = vn.copy()
                aval_vc = best_aval
            else:
                euler = math.e
                difv = aval_vc - best_aval
                exponent = difv/T
                if random.random() < euler**exponent:
                    vc = vn.copy()
                    aval_vc = best_aval
            t += 1
        T = k*T

    return vc, aval_vc

if __name__ == "__main__"    :
    #Verificar argumentos de execução do programa
    if len(sys.argv) < 6:
        print("Erro: Número de argumentos incorreto.")
        print("Exemplo de uso: python main.py arquivo_de_entrada Tmax k KT Tmin")
        sys.exit(1)

    #Inicialização
    input_file = sys.argv[1]
    TMax = float(sys.argv[2])
    k = float(sys.argv[3])
    Kt = int(sys.argv[4])
    TMin = float(sys.argv[5])

    cities = read_cities_from_file(input_file)
    num_cities = len(cities)
    
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i, j] = cities[i].calculate_distance(cities[j])

    #Execução do algoritmo Simulated Annealing    
    best_order, best_distance = simulated_annealing(cities, TMax, k, Kt, TMin)

    print("Melhor ordem de visitação das cidades:", [city for city in best_order])
    print("Distância total percorrida:", best_distance)
