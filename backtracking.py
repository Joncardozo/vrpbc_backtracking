import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from route import Route


def generate_initial_graph(n_cities : int, positions : np.array) -> nx.Graph:

	"""

	From an initial list of cities and coordinates, generate the complete graph.

	"""

	initial_graph = nx.complete_graph(n_cities)
	for c in range(n_cities):
		for i in range(c + 1, n_cities):
			initial_graph[c][i]['weight'] = int(np.linalg.norm(positions[c] - positions[i]))
	return initial_graph


def draw_graph(initial_graph : nx.Graph, positions : np.array, use_pos=True) -> None:

	"""

	Draw a graph from a NetworkX.

	"""

	plt.figure(figsize=(6, 6))
	if use_pos:
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
		positions : np.array,
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
		route : list[nx.Graph],
		positions : list,
		cover_LB : dict,
		cover_UB : dict,
		radius : int) -> int:

	"""

	Generate node candidate to be added to route in backtracking algorithm.

	"""

	raise NotImplementedError
	# return node


def generate_solution(G : nx.Graph, positions : list,
					  cover_LB : dict,
					  cover_UB : dict,
					  k : int) -> list[nx.Graph]:
	
	"""

	Generate a solution thru first found solution in a backtracking search

	"""

	# Generate a solution through first found backtracking search
	n = G.number_of_nodes()

	# solution variables
	obj = 0

	# create tree structure
	tree = nx.DiGraph()
	tree.add_node(0, label="Root")
	
	# create vehicle directed graph route
	route = []
	for i in range(k):
		route.append(nx.DiGraph())
		route[i].add_node(0)

	# create event graph
	events = nx.DiGraph()
	events.add_node(0)

	# backtraking
	# phase 1: assign first event to k0 using nearest neighbor heuristic
	# loop:
	# 	phase 2: assign routes to vehicles covering last event, using nearest neighbor heuristics,
	# 			 checking feasibility at first arrival between pairs of vehicles
	#	phase 3: find next node from last event trigger, 
	#			 checking feasibility at first arrival between pairs of vehicles
	# 	phase 3: compute next event; last event <- next event; phase 2
	for i in range(n):
		# phase 1
		if i == 0:
			candidates = list(range(1, n))
			d = 1e9
			e = 0
			for c in candidates:
				d_tmp = G[0][c]["weight"]
				if d_tmp < d:
					d = d_tmp
					e = c
			events.add_edge(0, e, weight=d)
			# tree.add_edge(0, e, weight=d)
			route[0].add_edge(0, e, weigth=d)
		# loop
		# else:
		# 	# phase 2
		# 	# compute last event and time of last event
		# 	last_event = list(nx.topological_sort(events))[-1]
		# 	last_event_time = events.size(weight="weight")
		# 	feasible = 1
		# 	# compute vehicle times
		# 	time_v = [[]] * k
		# 	for i in range(k):
		# 		time_v[i] = route[i].size(weight="weight")
		# 	# iterate over vehicles to get candidates for arc covering
		# 	for v in range(k):
		# 		last_node = list(nx.topological_sort(route[v]))[-1]
		# 		candidates = [key for key in cover_LB.keys() if key[0] == last_event and 
		# 		  key[1] == last_node]
		# 		d = 1e9
		# 		feasible_tmp = 0
		# 		contender = None
		# 		# iterate over candidates
		# 		for c in candidates:
		# 			d_tmp = G[c[1]][c[2]]["weight"]
		# 			if d_tmp < d:
		# 				d = d_tmp
		# 				feasible_tmp =  1
		# 				contender = c
		# 		# check feasibility
		# 		feasible = feasible and feasible_tmp
		# 		if feasible_tmp:
		# 			candidates.remove(contender)
		# 			route[v].add_edge()

		# continue

	# raise NotImplementedError
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
	print(positions)
	draw_graph(initial_graph, positions, True)
	cover_LB, cover_UB = read_pre_processing(cover_file)
	generate_solution(initial_graph, positions, cover_LB, cover_UB, k)
	input("pressione para sair...")


if __name__=='__main__':
	# instance = sys.argv[1]
	cover_file = "cover.dat"
	instance = "instancia_D2_2v_11n_2d.BC"
	main()
