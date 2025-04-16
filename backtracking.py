import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from route import Route


def compute_weight(coord1, coord2):
    coord1 = np.array(coord1)
    coord2 = np.array(coord2)
    l2_norm = np.linalg.norm(coord1 - coord2)
    weight = int(np.round(l2_norm))
    return weight

def generate_initial_graph(n_cities : int, positions : np.array) -> nx.Graph:

	"""

	From an initial list of cities and coordinates, generate the complete graph.

	"""

	initial_graph = nx.complete_graph(n_cities)
	initial_graph = nx.relabel_nodes(initial_graph, lambda x : str(x))
	for c in range(n_cities):
		for i in range(c + 1, n_cities):
			initial_graph[str(c)][str(i)]['weight'] = int(np.linalg.norm(positions[c] - positions[i]))
		initial_graph.nodes[str(c)]['pos'] = positions[c]
	return initial_graph


def draw_graph(initial_graph : nx.Graph, use_pos=True) -> None:

	"""

	Draw a graph from a NetworkX.

	"""

	plt.figure(figsize=(6, 6))
	if use_pos:
		positions = nx.get_node_attributes(initial_graph, 'pos')
		nx.draw_networkx_nodes(initial_graph, positions)
		nx.draw_networkx_labels(initial_graph, positions, font_color='white')
		nx.draw_networkx_edges(initial_graph, positions)
		edge_labels = nx.get_edge_attributes(initial_graph, "weight")
		nx.draw_networkx_edge_labels(initial_graph, positions, edge_labels, font_size=6, label_pos=0.3)
	else:
		nx.draw_networkx(initial_graph, font_color='white')
	plt.axis('equal')
	plt.show(block=False)
	return


def is_feasible(route : list[nx.Graph], radius : int) -> bool:

	"""

	Checks feasibility of an added candidate.

	"""

	raise NotImplementedError
	# return True


def backtracking(
		route : list[nx.Graph],
		initial_graph : nx.Graph,
		cover_LB : dict,
		cover_UB : dict,
		radius : int,
		use_pos=True) -> list[nx.Graph]:

	"""

	Backtracking algorithm to get a solution for the VRPBC problem.

	"""

	raise NotImplementedError
	# return route


def nearest_neighbor_candidate(
		initial_graph : nx.Graph,
		routes : list[Route],
		candidates : list[str],
		cover_LB : dict,
		cover_UB : dict,
		k : int) -> str:

	"""

	Generate node candidate to be added to route in backtracking algorithm.

	"""

	vehicle = 'k0'
	curr_obj = routes[0].obj
	for k_i in range(1, k):
		if routes[k_i].obj < curr_obj:
			vehicle = routes[k_i].vehicle_id
			curr_obj = routes[k_i].obj

	last_city = routes[int(vehicle[1:])].trajectory[-1]

	max_dist = 2**31 - 1
	contender = '0'
	for c in candidates:
		c_dist = compute_weight(initial_graph.nodes[last_city]['pos'], initial_graph.nodes[c]['pos'])
		if c_dist < max_dist:
			contender = c

	return contender


def generate_solution(initial_graph : nx.Graph,
					  cover_LB : dict,
					  cover_UB : dict,
					  k : int) -> list[Route]:
	
	"""

	Generate a solution through first found solution in a backtracking search

	"""

	# Generate a solution through first found backtracking search
	n = initial_graph.number_of_nodes()
	
	# create vehicle directed graph route
	routes = []
	for i in range(k):
		vehicle_name = "k" + str(i)
		routes.append(Route(vehicle_name, initial_graph.nodes['0']['pos']))

	# create event graph
	events = nx.DiGraph()
	events.add_node('0')

	feasibility = True

	candidates = list(initial_graph.nodes())
	while(feasibility):
		candidate = nearest_neighbor_candidate(initial_graph, routes, candidates, cover_LB, cover_UB, k)
		if candidate == '0':
			break
		else:
			# check feasibility
			if is_feasible(route, candidate):
				for i in range(k):
					route[i].add_stop(candidate, G.nodes[candidate]['pos'])
				events.add_node(candidate)
				events.add_edge('0', candidate)
				for i in range(k):
					route[i].finish_route()
			else:
				feasibility = False


	raise NotImplementedError
	return 0


def read_instance(instance_file : str) -> tuple[int, int, int, np.ndarray]:

	"""
	
	Read a instance from a BackCovered file instance.

	"""

	with open(instance_file, mode='r') as f:
		k, n, r = f.readline().split('\t')
		n = int(n) + 1
		k = int(k)
		r = int(r)
		positions = np.zeros(shape=(n, 2))
		for l in range(n):
			line = f.readline()
			positions[l] = list(map(int, line.split('\t')))
	return n, k, r, positions


def read_pre_processing(cover_file : str) -> tuple[dict, dict]:

	"""
	
	Get the times needed to hold coverage in a vehicle traversing an arc.
	
	"""


	cover_LB = {}
	cover_UB = {}
	with open(cover_file, mode='r') as f:
		for line in f:
			values = line.strip().split()

			p = int(values[0])
			a = int(values[1])
			b = int(values[2])
			l = float(values[3])
			u = float(values[4])

			if l < u:
				indices = (p, a, b)

				cover_LB[indices] = l
				cover_UB[indices] = u
	return cover_LB, cover_UB


def main():
	# positions = np.array([[0,0], [-4, 2], [8,9],[0,2],[2,-4]])
	## initialize instance and plot initial graph
	n, k, r, positions = read_instance(instance)
	initial_graph = generate_initial_graph(n, positions)
	draw_graph(initial_graph, True)
	cover_LB, cover_UB = read_pre_processing(cover_file)
	generate_solution(initial_graph, cover_LB, cover_UB, k)
	input("pressione para sair...")


if __name__=='__main__':
	# instance = sys.argv[1]
	cover_file = "cover.dat"
	instance = "instancia_D2_2v_11n_2d.BC"
	main()
