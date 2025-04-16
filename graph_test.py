import unittest
from route import Route

class TestRoute(unittest.TestCase):

    def setUp(self):
        # Initialize a Route object for use in tests
        self.route = Route('k0', (2, 3))

    def test_graph_initialization(self):
        self.assertEqual(self.route.graph.number_of_nodes(), 1, "Graph should initialize with 1 node")

    def test_add_stop(self):
        self.route.add_stop('5', (10, 3))
        self.assertEqual(self.route.graph.number_of_nodes(), 2, "Graph should have 2 nodes after adding a stop")
        self.assertEqual(self.route.obj, 8, "Weight should be 8 after adding the stop")

    def test_trajectory_after_add_stop(self):
        self.route.add_stop('5', (10, 3))
        self.route.add_stop('3', (9, -4))
        self.assertEqual(self.route.trajectory, ['0', '5', '3'], "Trajectory should be ['0', '5', '3']")

    def test_remove_stop(self):
        self.route.add_stop('5', (10, 3))
        self.route.add_stop('4', (-1, 6))
        self.route.remove_stop('4')
        self.assertEqual(self.route.graph.number_of_nodes(), 2, "Graph should have 2 nodes after removing a stop")
        self.assertEqual(self.route.obj, 8, "Weight should be 8 after removing the stop")
        self.assertEqual(self.route.trajectory, ['0', '5'], "Trajectory should be ['0', '5'] after removing the stop")

    def test_finish_route(self):
        self.route.add_stop('5', (10, 3))
        self.route.finish_route()
        self.assertEqual(self.route.graph.number_of_nodes(), 3, "Graph should have 3 nodes after finishing the route")
        self.assertEqual(self.route.trajectory, ['0', '5', '0f'], "Trajectory should be ['0', '5', '0f'] after finishing the route")


if __name__ == '__main__':
    unittest.main()