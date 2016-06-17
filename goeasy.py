#!/usr/bin/env python3
import sys
import collections
import math

def readInput():
    # number of zones and stations
    Z, S = [int(x) for x in str.split(sys.stdin.readline())]
    # empty array of size S + 1
    stationZones = [None] * S
    # for each zone
    for z in range(Z):
        # save each station's zone
        for station in [int(x) - 1 for x in str.split(sys.stdin.readline())[1:]]:
            stationZones[station] = z

    # number of train and buses routes
    T, B = [int(x) for x in str.split(sys.stdin.readline())]

    trainRoutes = []
    for t in range(T):
        trainRoutes.append([int(x) - 1 for x in str.split(sys.stdin.readline())[1:]])

    busRoutes = []
    for b in range(B):
        busRoutes.append([int(x) - 1 for x in str.split(sys.stdin.readline())[1:]])

    X, Y = [int(x) - 1 for x in str.split(sys.stdin.readline())]

    return Z, S, T, B, X, Y, stationZones, trainRoutes, busRoutes


def find_all_paths(connections, start, end):
    paths = []

    def all_paths(current, end, path=[]):
        path.append(current)
        if current == end:
            paths.append(path)
            return

        adjacent_nodes = [x for x in connections[current] if x not in path]
        if len(adjacent_nodes) == 0:
            return
        for an in adjacent_nodes:
            all_paths(an, end, path[:])

    all_paths(start, end)
    return paths


def cheapestPath(Z, S, T, B, X, Y, stationZones, trainRoutes, busRoutes):
    print("Z = {}".format(Z))
    print("S = {}".format(S))
    print("T = {}".format(T))
    print("B = {}".format(B))
    print("X = {}".format(X))
    print("Y = {}".format(Y))
    print("Train routes:")
    print(trainRoutes)
    print("Bus routes:")
    print(busRoutes)
    connections = []
    for s in range(S):
        connections.append([])
    # for each train route
    for tr in trainRoutes:
        for i in range(len(tr)-1):
            # add pairs of stations both ways to connections
            newConnection = tr[i:i+2]
            connections[newConnection[0]].append(newConnection[1])
            connections[newConnection[1]].append(newConnection[0])

    for br in busRoutes:
        for i in range(len(br)-1):
            # add pairs of stations both ways to connections
            newConnection = br[i:i+2]
            connections[newConnection[0]].append(newConnection[1])
            connections[newConnection[1]].append(newConnection[0])
    print("Connections:")
    print(connections)
    print("Paths:")
    print(find_all_paths(connections, X, Y))


def minCostOfPath(path, stationZones, trainRoutes, busRoutes):
    possibleStarts = [(x, 0) for x in trainRoutes if x[0] == path[0]] + \
                     [(x, 1) for x in busRoutes if x[0] == path[0]]
    for start in possibleStarts:
        cost = 2


inputData = readInput()
cheapestPath(*inputData)
# start = 0
# end = 4
# connections = [
#     [1, 3, 4],
#     [0, 2, 4],
#     [1, 4],
#     [0],
#     [0, 1, 2]
# ]
# print(find_all_paths(connections, start, end))
