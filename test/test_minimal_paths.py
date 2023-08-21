import unittest
from simulation.model import CommunicationNetwork
from simulation.model import EntityNotFound
from simulation.minimal_paths import single_source_dijkstra_vertices, single_source_dijkstra_hyperedges, DistanceType

class MinimalPath(unittest.TestCase):
    cn_data = {
        'h1': ['v1', 'v2'],
        'h2': ['v2', 'v3'],
        'h3': ['v3', 'v4']
    }
    cn_timings = {
        'h1': 1,
        'h2': 2,
        'h3': 3
    }
    def setUp(self):
        self.c_n = CommunicationNetwork(self.cn_data, self.cn_timings, name="TestNetwork")
    # shortest
    #ID 8
    def test_shortest_for_vertex(self):
        expected = {'v2': 1, 'v3': 2, 'v4': 3}
        result = single_source_dijkstra_vertices(self.c_n, 'v1', DistanceType.SHORTEST, min_timing=0)
        self.assertEqual(result, expected)
    #ID 9
    def test_shortest_for_hyperedge(self):
        expected = {'v2': 1, 'v3': 2, 'v4': 3}
        result = single_source_dijkstra_hyperedges(self.c_n, 'v1', DistanceType.SHORTEST, min_timing=0)
        self.assertEqual(result, expected)
    # fastest
    #ID 10
    def test_fastest_for_vertex(self):
        expected = {'v2': 0, 'v3': 1, 'v4': 2}
        result = single_source_dijkstra_vertices(self.c_n, 'v1', DistanceType.FASTEST, min_timing=0)
        self.assertEqual(result, expected)
    #ID 11
    def test_fastest_for_hyperedge(self):
        expected = {'v2': 0, 'v3': 1, 'v4': 2}
        result = single_source_dijkstra_hyperedges(self.c_n, 'v1', DistanceType.FASTEST, min_timing=0)
        self.assertEqual(result, expected)
    ### Additional Equivalence Tests
    #ID 12
    def test_equivalence_of_different_start_nodes(self):
        start_nodes = ['v2', 'v3']
        distances = [DistanceType.SHORTEST, DistanceType.FASTEST, DistanceType.FOREMOST]     
        for distance in distances:
            for start_node in start_nodes:
                with self.subTest(distance=distance, start_node=start_node):
                    result_start_node = single_source_dijkstra_vertices(self.c_n, start_node, distance, min_timing=0)
                    result_initial_node = single_source_dijkstra_vertices(self.c_n, 'v1', distance, min_timing=0)
                    self.assertNotEqual(result_start_node, result_initial_node, f'Path calculation methods for {distance} should not be equivalent for start node {start_node}')
    ## Additional Error Handling Tests ###
    #ID 13
    def test_empty_graph(self):
        empty_cn = CommunicationNetwork({}, {}, name="EmptyNetwork")
        with self.assertRaises(EntityNotFound):
            single_source_dijkstra_vertices(empty_cn, 'v1', DistanceType.SHORTEST, min_timing=0)
