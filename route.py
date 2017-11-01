class Building:
    graph = None


class Graph:
    points = []
    connections = []


class Point:
    id = -1
    name = None
    floor_index = -1
    x = -1
    y = -1


class PointConnection:
    point1 = None
    point2 = None
    floor_index = -1
    trans_floor_marker = False


class Floor:
    floor_index = -1
    picture_path = None


class Path:
    points = []
    connections = []
    floors = []
    weight = -1
