import unittest
from simulation.model import CommunicationNetwork
from simulation.model import EntityNotFound
class TimeVaryingHypergraphTest(unittest.TestCase):
    cn = CommunicationNetwork({'h1': ['v1', 'v2'], 'h2': ['v2', 'v3'], 'h3': ['v3', 'v4']}, {'h1': 1, 'h2': 2, 'h3': 3})
    #ID 1
    def test_vertices(self):
        self.assertEqual(len(TimeVaryingHypergraphTest.cn.vertices()), 4)
        self.assertEqual(TimeVaryingHypergraphTest.cn.vertices('h1'), {'v1', 'v2'})
    #ID 2
    def test_hyperedges(self):
        self.assertEqual(len(TimeVaryingHypergraphTest.cn.hyperedges()), 3)
        self.assertEqual(TimeVaryingHypergraphTest.cn.hyperedges('v1'), {'h1'})
    #ID 3
    def test_timings(self):
        self.assertEqual(TimeVaryingHypergraphTest.cn.timings('h1'), 1)
        self.assertEqual(TimeVaryingHypergraphTest.cn.timings('h2'), 2)
    #ID 4
    def test_invalid_vertex(self):
        with self.assertRaises(EntityNotFound):
            TimeVaryingHypergraphTest.cn.hyperedges('v5')
    #ID 5
    def test_invalid_hyperedge(self):
        with self.assertRaises(EntityNotFound):
            TimeVaryingHypergraphTest.cn.vertices('h4')
    #ID 6
    def test_channels(self):
        self.assertEqual(TimeVaryingHypergraphTest.cn.channels('v1'), {'h1'})
        self.assertEqual(TimeVaryingHypergraphTest.cn.channels('v2'), {'h1', 'h2'})
    #ID 7
    def test_participants(self):
        self.assertEqual(TimeVaryingHypergraphTest.cn.participants('h1'), {'v1', 'v2'})
        self.assertEqual(TimeVaryingHypergraphTest.cn.participants('h2'), {'v2', 'v3'})
class CNModelTest(unittest.TestCase):
    cn = CommunicationNetwork({'h1': ['v1', 'v2'], 'h2': ['v2', 'v3'], 'h3': ['v3', 'v4']}, {'h1': 1, 'h2': 2, 'h3': 3})
    #ID 14
    def test_vertices(self):
        self.assertEqual(len(CNModelTest.cn.vertices()), 4)
        self.assertEqual(CNModelTest.cn.vertices('h1'), {'v1', 'v2'})
    #ID 15
    def test_hyperedges(self):
        self.assertEqual(len(CNModelTest.cn.hyperedges()), 3)
        self.assertEqual(CNModelTest.cn.hyperedges('v1'), {'h1'})
class ModelDataTest(unittest.TestCase):
    #ID 16
    def test_model_with_data(self):
        communciation_network = CommunicationNetwork.from_json('./data/networks/microsoft.json.bz2')
        self.assertEqual(len(communciation_network.participants()), 37103)
        self.assertEqual(len(communciation_network.channels()), 309740)
        self.assertEqual(len(communciation_network.vertices()), 37103)
        self.assertEqual(len(communciation_network.hyperedges()), 309740)
