class Building:
    graph = None
    floors = None

    def __init__(self, graph, floors):
        self.graph = graph
        self.floors = floors


class Graph:
    points = []
    connections = []

    def __init__(self, points, connections):
        self.points = points
        self.connections = connections
        # download data from db is planned


class Point:
    id = -1
    name = None
    floor_index = -1
    x = -1
    y = -1

    def __init__(self, id, name, floor_index, x, y):
        self.id = id
        self.name = name
        self.floor_index = floor_index
        self.x = x
        self.y = y


class PointConnection:
    point1 = None
    point2 = None
    connection_weight = -1
    floor_index = -1
    trans_floor_marker = False

    def __init__(self, point1, point2, connection_weight, floor_index):
        self.point1 = point1
        self.point2 = point2
        self.connection_weight = connection_weight
        self.floor_index = floor_index


class Floor:
    floor_index = -1
    picture_path = None

    def __init__(self, floor_index, picture_path):
        self.floor_index = floor_index
        self.picture_path = picture_path



class Path:
    points = []
    connections = []
    floors = []

    def __init__(self, points, connections, floors):
        self.points = points
        self.connections = connections
        self.floors = floors


class Router:
    building = None

    def __init__(self, building):
        self.building = building

    def find_best_path(self, start, finish):
        # TODO
        # use dijkstra algorithm
        best_path = Path()
        return best_path  # return instance of class Path