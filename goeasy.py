#!/usr/bin/env python3
import sys
import collections
import math


class Map:
    def __init__(self, zones, stations):
        self.zones = zones
        self.stations = stations
        self.nodes = [None] * stations


class Node:
    def __init__(self, station, zone):
        self.station = station
        self.zone = zone
        self.edges = []


class Edge:
    def __init__(self, to, bus, line):
        self.to = to
        self.bus = bus
        self.line = line


def read_input():
    # number of zones and stations
    Z, S = [int(x) for x in str.split(sys.stdin.readline())]
    if Z == 0 and S == 0:
        return False

    travelMap = Map(Z, S)

    # for each zone
    for z in range(Z):
        # create a node for each station with its zone
        for s in [int(x) - 1 for x in str.split(sys.stdin.readline())[1:]]:
            travelMap.nodes[s] = Node(s, z)

    # number of train and buses routes
    T, B = [int(x) for x in str.split(sys.stdin.readline())]

    # train routes
    for t in range(T):
        route = [int(x) - 1 for x in str.split(sys.stdin.readline())[1:]]
        for i in range(len(route) - 1):
            # create edges for each step of route in both ways
            travelMap.nodes[route[i]].edges.append(Edge(route[i+1], False, t))
            travelMap.nodes[route[-i-1]].edges.append(Edge(route[-i-2], False, t))

    # bus routes
    for b in range(B):
        route = [int(x) - 1 for x in str.split(sys.stdin.readline())[1:]]
        for i in range(len(route) - 1):
            # create edges for each step of route in both ways
            travelMap.nodes[route[i]].edges.append(Edge(route[i+1], True, b))
            travelMap.nodes[route[-i-1]].edges.append(Edge(route[-i-2], True, b))

    # start and end locations
    X, Y = [int(x) - 1 for x in str.split(sys.stdin.readline())]
    travelMap.start = X
    travelMap.end = Y
    return travelMap


def cheapest_path(travelMap):
    def find_path(current, end, cost, path=[], travel_log=[], bus=False, line=-1):
        nonlocal lowest_cost
        nonlocal lowest_cost_path
        nonlocal lowest_cost_travel_log

        if cost > lowest_cost:
            return

        path.append(current.station)
        travel_log.append((current.station + 1, "Ônibus" if bus else "Trem", line + 1, cost, current.zone + 1))

        if current.station == end:
            if cost < lowest_cost:
                lowest_cost = cost
                lowest_cost_path = path
                lowest_cost_travel_log = travel_log
            return

        edges = [x for x in current.edges if x.to not in path]
        if len(edges) == 0:
            return
        for edge in edges:
            toNode = travelMap.nodes[edge.to]
            cost_to_add = 0
            # transfer from bus to bus of different line
            if bus and edge.bus and (line != edge.line):
                find_path(toNode, end, cost + 1, path[:], travel_log[:], True, edge.line)
            # transfer from train to bus
            elif not bus and edge.bus:
                find_path(toNode, end, cost + 1, path[:], travel_log[:], True, edge.line)
            # zone while choosing train change
            elif not edge.bus and current.zone != toNode.zone:
                find_path(toNode, end, cost + 4, path[:], travel_log[:], False, edge.line)
            else:
                find_path(toNode, end, cost, path[:], travel_log[:], edge.bus, edge.line)

    lowest_cost = math.inf
    lowest_cost_path = []
    lowest_cost_travel_log = []

    find_path(travelMap.nodes[travelMap.start], travelMap.end, 2)

    return lowest_cost_travel_log


travelMap = read_input()
while (travelMap):
    log = cheapest_path(travelMap)
    print("Passageiro iniciou sua viagem pela estação {} da zona {}".format(log[0][0], log[0][4]))
    for entry in log[1:]:
        print("Passageiro chegou na estação {} da zona {} pela linha de {} #{}".format(entry[0], entry[4], entry[1], entry[2]))
    print("Custo total: {} UTs".format(log[-1][3]))
    travelMap = read_input()
