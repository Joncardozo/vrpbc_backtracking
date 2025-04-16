# VRPBC backtracking

## Algoritmo

O algoritmo implementado é uma versão do algoritmo de backtracking para resolver o problema dos múltiplos caixeiros viajantes (mTSP) com restrições de cobertura. O algoritmo tenta encontrar a melhor rota para um veículo, minimizando a distância total percorrida e respeitando as restrições de cobertura através da busca exaustiva em profundidade, retornando a primeira solução factível encontrada.
- Arquivo: `backtracking.py`

### Estrutura do código
O código é dividido em duas partes principais:
1. **Funções**: Implementam as operações necessárias para resolver o problema.
2. **Execução**: Realiza a leitura dos dados de entrada, executa o algoritmo e imprime os resultados.

### Funções de entrada e saída
- `read_pre_processing(cover_file : str) -> tuple[dict, dict]`: Lê o arquivo que contém o pré-processamento da cobertura e retorna dois dicionários: um os tempos mínimos de localização no arco e outro com os tempos máximos.
- `read_instance(instance_file : str) -> tuple[int, int, int, np.ndarray]`: Lê o arquivo da instância e retorna o número de nós, o número de veículos, o raio de cobertura, e uma lista com as coordenadas dos nós.
- `draw_graph(initial_graph : nx.Graph, positions : np.array, use_pos=True) -> None`: Desenha o grafo completo da instância.
### Funções de processamento
- `generate_initial_graph(n_cities : int, positions : np.array) -> nx.Graph` : Gera o grafo completo da instância.
- `is_feasible(route : list[nx.Graph], radius : int) -> bool` : Verifica se a solução é factível em relação à cobertura de apoio.
- `backtracking(
		route : list[nx.Graph],
		initial_graph : nx.Graph,
		positions : np.array,
		cover_LB : dict,
		cover_UB : dict,
		radius : int,
		use_pos=True) -> list[nx.Graph]` : Rotina que realiza a busca exaustiva em profundidade para encontrar a primeira solução, minimizando a distância total percorrida e respeitando as restrições de cobertura.
- `nearest_neighbor_candidate(
		route : list[nx.Graph],
		positions : list,
		cover_LB : dict,
		cover_UB : dict,
		radius : int) -> int` : Retorna o nó mais próximo do último nó da rota.
- `generate_solution(G : nx.Graph, positions : list,
					  cover_LB : dict,
					  cover_UB : dict,
					  k : int) -> list[nx.Graph]` : Gera uma solução inicial para o problema, utilizando backtraking.

## Classes

### Route

Classe para representar uma rota de um veículo.

- Arquivo: `route.py`

#### Atributos

- `trajectory`: Lista com os pontos da trajetória.
- `obj`: Custo total da rota.

#### Métodos

- `__init__(self, vehicle_id, coord)`: Inicializa a rota com o id do veículo e coordenada da garagem.
- `add_stop(self, stop_id : str, coord : tuple[int, int])`: adiciona um nó ao final da trajetória.
- `remove_stop(self, stop_id : str)`: remove um nó da trajetória.

