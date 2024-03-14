import unittest
from route_finder import RouteFinder

class TestRouteFinder(unittest.TestCase):
    def test_find_route(self):
        route_finder = RouteFinder('tubedata.csv')
        for method in ['DFS', 'BFS', 'UCS', 'Heuristic BFS']:
            route, cost, nodes_expanded = route_finder.find_route('Harrow & Wealdstone', 'Waterloo', method)
            self.assertIsNotNone(route)
            self.assertIsNotNone(cost)
            self.assertIsNotNone(nodes_expanded)
