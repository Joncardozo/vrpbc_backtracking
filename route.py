import numpy as np
import networkx as nx


def compute_weight(coord1, coord2):
    coord1 = np.array(coord1)
    coord2 = np.array(coord2)
    l2_norm = np.linalg.norm(coord1 - coord2)
    weight = int(np.round(l2_norm))
    return weight


class Route:

    def __init__(self, vehicle_id, coord):
        self.vehicle_id = vehicle_id
        self.graph = nx.DiGraph()
        self.graph.add_node('0')
        self.graph.nodes['0']['pos'] = coord
        self.obj = 0
        self.trajectory = ['0']

    def add_stop(self, stop_id : str, coord : tuple[int, int]):
        last_city = list(nx.topological_sort(self.graph))[-1]
        coord1 = np.array(self.graph.nodes[last_city]['pos'])
        weight = compute_weight(coord1, coord)
        self.graph.add_edge(last_city, stop_id, weight=weight)
        self.graph.nodes[stop_id]['pos'] = coord
        self.obj = self.graph.size('weight')
        self.__update_route()

    def remove_stop(self, stop_id : str):
        if stop_id in self.graph.nodes:
            if stop_id == '0':
                raise ValueError("Cannot remove the initial node.")
            pred_i = self.graph.predecessors(stop_id)
            succ_i = self.graph.successors(stop_id)
            if not list(self.graph.successors(stop_id)):
                self.graph.remove_node(stop_id)
                self.obj = self.graph.size('weight')
                self.__update_route()
                return
            pred = next(iter(pred_i))
            succ = next(iter(succ_i))
            self.graph.remove_node(stop_id)
            weight = compute_weight(self.graph.nodes[pred]['pos'], self.graph.nodes[succ]['pos'])
            self.graph.add_edge(pred, succ, weight=weight)
            self.obj = self.graph.size('weight')
            self.__update_route()
        else:
            raise ValueError(f"Node {stop_id} not found in the graph.")

    def __update_route(self):
        self.trajectory = list(nx.topological_sort(self.graph))
