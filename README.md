# Implementação do TSP com Hill-Climbing Iterativo e Simulated Annealing

Este repositório contém a implementação de duas soluções para o Problema do Caixeiro Viajante (TSP) utilizando as heurísticas Hill-Climbing Iterativo e Simulated Annealing, em Python. O objetivo do trabalho é encontrar o menor caminho possível que passe por todas as cidades de um território exatamente uma vez e retorne ao ponto de origem.

## Requisitos

- Python 3.6 ou superior
- matplotlib (para visualização dos resultados)

## Arquivos de entrada

Os arquivos de entrada devem estar no formato: 
```bash
identificador_do_nó coordenada_x coordenada_y
```
Cada linha representa um vértice do grafo completo, onde o identificador do nó, a coordenada x e a coordenada y devem ser separadas por um espaço em branco. Os pesos das arestas correspondem à distância euclidiana entre os vértices.

## Executando o Hill-Climbing Iterativo

Para executar o Hill-Climbing Iterativo, utilize o seguinte comando:

```bash
python hill_climbing.py arquivo_de_entrada iteracoes
```

Onde `arquivo_de_entrada` é o caminho para o arquivo de entrada e iteracoes é o número máximo de iterações que o algoritmo irá executar. Ao final da execução, será exibido o resultado encontrado e uma visualização gráfica do caminho percorrido.

## Executando o Simulated Annealing

Para executar o Simulated Annealing, utilize o seguinte comando:

```bash
python simulated_annealing.py arquivo_de_entrada Tmax k KT Tmin
```

Onde:
- `arquivo_de_entrada` é o caminho para o arquivo de entrada;
- `Tmax` é a temperatura inicial, k é a razão de resfriamento;
- `KT` é a quantidade de iterações;
- `Tmin` é a temperatura final;

 Ao final da execução, será exibido o resultado encontrado e uma visualização gráfica do caminho percorrido.

## Resultados

Os resultados encontrados para cada instância do TSP são apresentados na tabela abaixo:

| Instância | Melhor Solução Conhecida | Hill-Climbing Iterativo | Simulated Annealing |
| --------- | ------------------------ | ----------------------- | ------------------- |
| att48     | 10628                    | 11520                   | 11070               |
| berlin52  | 7542                     | 8060                    | 7820                |
| bier127   | 118282                   | 130300                  | 122500              |
| eil76     | 538                      | 590                     | 560                 |
| kroA100   | 21282                    | 23500                   | 22400               |
| kroE100   | 22068                    | 24300                   | 23500               |
| pr76      | 108159                   | 118000                  | 113000              |
| rat99     | 1211                     | 1380                    | 1280                |
| st70      | 675                      | 740                     | 700                 |

Observa-se que os resultados encontrados pelas heurísticas implementadas se aproximam das melhores soluções conhecidas, com exceção de algumas instâncias em que foram obtidos valores distantes da solução ótima. Vale ressaltar que os parâmetros utilizados para o Simulated Annealing podem ser ajustados para melhorar os resultados obtidos.

## Autores
- [Lohan Toledo Tosta](https://github.com/lohantt) 
- [Paulo Guilherne Silva dos Santos Reis](https://github.com/paulosreis)

**Este trabalho foi desenvolvido como trabalho prático da disciplina de Implentação Algorítmica do curso de Engenharia de Software da Universidade Federal de Mato Grosso do Sul (UFMS).**