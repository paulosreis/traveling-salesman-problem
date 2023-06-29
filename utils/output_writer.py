import os


def save_output_to_file(output_folder, output_filename, max_iterations, best_order, best_distance):
    # Verificar se o arquivo já existe e se a distância é menor
    existing_file_path = os.path.join(output_folder, output_filename)
    if os.path.exists(existing_file_path):
        with open(existing_file_path, "r") as existing_file:
            existing_lines = existing_file.readlines()
            existing_distance = float(existing_lines[2].split(":")[1].strip())

        if best_distance >= existing_distance:
            print("A distância encontrada é maior ou igual à distância existente. "
                  "O arquivo não será criado ou atualizado.")
            return

    # Salvar os valores de saída no arquivo de texto
    output_file_path = os.path.join(output_folder, output_filename)
    with open(output_file_path, "w") as file:
        file.write("Número de iterações: {}\n".format(max_iterations))
        file.write("Melhor ordem de visitação das cidades: {}\n".format(best_order))
        file.write("Distância total percorrida: {}\n".format(best_distance))
        file.write("\nValores salvos com sucesso em {}.".format(output_file_path))
