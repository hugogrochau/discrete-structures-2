#!/usr/bin/env python3
import sys
import collections
import math
from enum import Enum


class Transport(Enum):
    bus = 1
    train = 2

    def to_string(self):
        return "Ônibus" if self.value is 1 else "Trem"


class Graph:
    def __init__(self, zones, stations):
        self.zones = zones
        self.stations = stations
        self.nodes = [None] * stations


class Node:
    def __init__(self, station, zone):
        self.station = station
        self.zone = zone
        self.edges = set()


class Edge:
    def __init__(self, to, cost, transport, line):
        self.to = to
        self.cost = cost
        self.transport = transport
        self.line = line


def zone_change_cost(graph, route, start, end):
    if (start > end):
        tmp = start
        start = end
        end = tmp

    current_zone = graph.nodes[route[start]].zone
    total_cost = 0
    for i in range(start, end + 1):
        if graph.nodes[route[i]].zone != current_zone:
            current_zone = graph.nodes[route[i]].zone
            total_cost += 4

    return total_cost


def read_input():
    # number of zones and stations
    first_line = sys.stdin.readline()
    while first_line.strip() is "":
        first_line = sys.stdin.readline()
    Z, S = [int(x) for x in str.split(first_line)]
    if Z == 0 and S == 0:
        return False

    graph = Graph(Z, S)

    # for each zone
    for z in range(Z):
        # create a node for each station with its zone
        for s in [int(x) - 1 for x in str.split(sys.stdin.readline())[1:]]:
            graph.nodes[s] = Node(s, z)

    # number of train and buses routes
    T, B = [int(x) for x in str.split(sys.stdin.readline())]

    # train routes
    for t in range(T):
        route = [int(x) - 1 for x in str.split(sys.stdin.readline())[1:]]
        # add an edge for each pair of stations
        for i in range(len(route)):
            for j in range(len(route)):
                if i != j:
                    node_from = graph.nodes[route[i]]
                    node_to = graph.nodes[route[j]]
                    cost = zone_change_cost(graph, route, i, j)
                    node_from.edges.add(Edge(node_to, cost, Transport.train, t))
                    node_to.edges.add(Edge(node_from, cost, Transport.train, t))

    # bus routes
    for b in range(B):
        route = [int(x) - 1 for x in str.split(sys.stdin.readline())[1:]]
        # add an edge for each pair of stations
        for i in range(len(route)):
            for j in range(len(route)):
                if i != j:
                    node_from = graph.nodes[route[i]]
                    node_to = graph.nodes[route[j]]
                    node_from.edges.add(Edge(node_to, 1, Transport.bus, b))
                    node_to.edges.add(Edge(node_from, 1, Transport.bus, b))

    # start and end locations
    X, Y = [int(x) - 1 for x in str.split(sys.stdin.readline())]
    graph.start = X
    graph.end = Y
    return graph


def dijkstra(graph, source):
    costs = dict()
    previous = dict()
    edges = dict()

    for node in graph.nodes:
        costs[node] = float("inf")
        previous[node] = None
        edges[node] = None

    costs[source] = 0
    nodes = set(graph.nodes)

    while len(nodes) > 0:
        min_node = None
        for node in nodes:
            if node in costs:
                if min_node is None:
                    min_node = node
                elif costs[node] < costs[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)

        if costs[min_node] == float('inf'):
            break

        for edge in min_node.edges:
            alt = costs[min_node] + edge.cost
            if alt < costs[edge.to]:
                costs[edge.to] = alt
                previous[edge.to] = min_node
                edges[edge.to] = edge
    return previous, edges


def cheapest_path(graph, a, b):
    previous, edges = dijkstra(graph, a)
    steps = []
    node = b
    while previous[node]:
        steps.append((node, edges[node]))
        node = previous[node]
    return reversed(steps)

graph = read_input()
while (graph):
    cost = 2
    steps = cheapest_path(graph, graph.nodes[graph.start], graph.nodes[graph.end])
    print("Passageiro iniciou sua viagem pela estação {} da zona {}".format(graph.start + 1, graph.nodes[graph.start].zone + 1))
    for step in steps:
        print("Passageiro chegou na estação {} da zona {} pela linha de {} #{}".format(step[0].station + 1, step[0].zone + 1, step[1].transport.to_string(), step[1].line + 1))
        cost += step[1].cost
    print("Custo total: {} UTs".format(cost))
    graph = read_input()
