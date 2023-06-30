# Implementação do TSP com Hill-Climbing Iterativo e Simulated Annealing

Este repositório contém a implementação de duas soluções para o Problema do Caixeiro Viajante (TSP) utilizando as heurísticas Hill-Climbing Iterativo e Simulated Annealing, em Python. O objetivo do trabalho é encontrar o menor caminho possível que passe por todas as cidades de um território exatamente uma vez e retorne ao ponto de origem.

## Requisitos

- Python 3.10 ou superior
- Numpy (`pip install numpy`)

## Arquivos de entrada

Os arquivos de entrada devem estar no formato: 
```bash
identificador_do_nó coordenada_x coordenada_y
```
Cada linha representa um vértice do grafo completo, onde o identificador do nó, a coordenada x e a coordenada y devem ser separadas por um espaço em branco. Os pesos das arestas correspondem à distância euclidiana entre os vértices.

## Executando o Hill-Climbing Iterativo

Para executar o Hill-Climbing Iterativo, utilize o seguinte comando:

```bash
python hill_climbing.py <arquivo_de_entrada> <iteracoes>
```

Onde `<arquivo_de_entrada>` é o caminho para o arquivo de entrada e `<iteracoes>` é o número máximo de iterações que o algoritmo irá executar. Ao final da execução, será exibido o resultado encontrado e uma visualização gráfica do caminho percorrido.

## Executando o Simulated Annealing

Para executar o Simulated Annealing, utilize o seguinte comando:

```bash
python simulated_annealing.py arquivo_de_entrada <Tmax> <k> <KT> <Tmin>
```

Onde:
- `arquivo_de_entrada` é o caminho para o arquivo de entrada;
- `<Tmax>` é a temperatura inicial, k é a razão de resfriamento;
- `<k>` é a razão de resfriamento;
- `<KT>` é a quantidade de iterações;
- `<Tmin>` é a temperatura final.

 Ao final da execução, será exibido o resultado encontrado e uma visualização do caminho percorrido.

## Resultados

Os resultados encontrados para cada instância do TSP são apresentados na tabela abaixo:

| Instância | Melhor Solução Conhecida | Hill-Climbing Iterativo | Simulated Annealing |
| --------- | ------------------------ | ----------------------- | ------------------- |
| att48     | 10628                    | 47081                   | 54907               |
| berlin52  | 7542                     | 11578                   | 18107               |
| bier127   | 118282                   | 274471                  | 358060              |
| eil76     | 538                      | 926                     | 1479                |
| kroA100   | 21282                    | 52216                   | 157260              |
| kroE100   | 22068                    | 52180                   | 98363               |
| pr76      | 108159                   | 184384                  | 291200              |
| rat99     | 1211                     | 2665                    | 3317                |
| st70      | 675                      | 1147                    | 2300                |

Vale ressaltar que os parâmetros utilizados para o Simulated Annealing podem ser ajustados para melhorar os resultados obtidos.

[Relatorio](https://github.com/paulosreis/traveling-salesman-problem/files/11911535/Relatorio.pdf)

## Autores
- [Lohan Toledo Tosta](https://github.com/lohantt) 
- [Paulo Guilherne Silva dos Santos Reis](https://github.com/paulosreis)

**Este trabalho foi desenvolvido como trabalho prático da disciplina de Implentação Algorítmica do curso de Engenharia de Software da Universidade Federal de Mato Grosso do Sul (UFMS).**
