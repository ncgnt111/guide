import unittest
from route import *

class RouterTestCase(unittest.TestCase):

    def setUp(self):
        self.building = Building(graph, floors) # graph, floors are predetermined
        self.router = Router(self.building)
        self.start = Point(id1, name1, floor_index1, x1, y1)# id1, name1, floor_index1, x1, y1 are predetermined
        self.finish = Point(id2, name2, floor_index2, x2, y2)# id2, name2, floor_index2, x2, y2 are predetermined
        self.path = Path(points, connections, floors)# points, connections, floors are predetermined

    def test_find_best_path(self):
        self.assertEqual(self.router.find_best_path(self.start, self.finish), self.path, 'path is not correct')


if __name__ == '__main__':
        unittest.main()