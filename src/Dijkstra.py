from copy import copy
from pprint import pprint

# Each vertex is a dictionary composed of:
# Vertex index, dictionary of neighbors and their edge costs
graph = {
       'a':{'a':2, 'b':2},
       'b':{'c':1, 'd':4},
       'c':{'a':1, 'd':1},
       'd':{'c':1, 'e':1},
       'e':{}
       }

# graph = {
#        '1':{'2':7, '3':9, '6':14},
#        '2':{'1':7, '3':10, '4':15},
#        '3':{'1':9, '2':10, '4':11, '6':2},
#        '4':{'2':15, '3':11, '5':6},
#        '5':{'4':6, '6':9},
#        '6':{'1':14, '3':2, '5':9}
#        }

distances = {}  # Dictionary of final distance for each node
parent = {}  # Dictionary of parent of each node

def dijkstra(graph, start):
    # Initially, the starting vertex distance is 0, and every other vertex is infinity
    # Each vertex' parent is "none"
    for v in graph:
        parent[v] = "none"
        if v == start:
            distances[v] = 0
        else:
            distances[v] = float("inf")

    nonFinal = copy(distances)

    # While there are nonFinal vertices
    while nonFinal:
        v = min(nonFinal, key=nonFinal.get)  # Let v be the vertex in nonFinal with the smallest distance
        nonFinal.pop(v)  # Remove v from nonFinal

        # For every neighbor u of v
        for u in graph[v]:
            if distances[u] > distances[v] + graph[v][u]:  # If u's distance > v's distance + weight of the edge (v, u)
                distances[u] = distances[v] + graph[v][u]  # Update u's distance to v's distance + weight (v, u)
                nonFinal[u] = distances[u]
                parent[u] = v  # Set it's parent to v
    return distances

def getDistances():  # Print the vertices and their final costs
    print "Vertex\tDistance"
    pprint (distances, width=1)

def getPath(final):  # Print path from start to given vertex
    print "Path from:", final, "to start:"
    current = final
    path = []
    while parent[current] != "none":
        path.append(current)
        current = parent[current]
    path.append(current)
    print path

dijkstra(graph, 'a')
getDistances()
getPath('d')

# Output
# Vertex    Distance
# {'a': 0,
#  'b': 2,
#  'c': 3,
#  'd': 4,
#  'e': 5}
# Path from: d to start:
# ['d', 'c', 'b', 'a']

# Vertex    Distance
# {'1': 0,
#  '2': 7,
#  '3': 9,
#  '4': 20,
#  '5': 20,
#  '6': 11}
# Path from: 5 to start:
# ['5', '6', '3', '1']
