from pprint import pprint

# Each vertex is a dictionary composed of:
# Vertex index, dictionary of neighbors and their edge costs
# For backward-value iteration, reverse edge directions
graph = {
       'a':{'a':2, 'c':1},
       'b':{'a':2},
       'c':{'b':1, 'd':1},
       'd':{'b':4, 'c':1},
       'e':{'d':1}
       }

# graph = {
#        'a':{'a':2, 'b':2},
#        'b':{'c':1, 'd':4},
#        'c':{'a':1, 'd':1},
#        'd':{'c':1, 'e':1},
#        'e':{}
# }

distances = {}  # Dictionary of final distance for each node
parent = {}  # Dictionary of parent of each node

# Input:  graph and goal
# Output: edge costs
def backwardValueIteration(graph, start):
    # Initially, the starting vertex distance is 0, and every other vertex is infinity
    # Each vertex' parent is "none"
    for v in graph:
        parent[v] = "none"
        if v == start:
            distances[v] = 0
        else:
            distances[v] = float("inf")

    difference = True  # Is there a difference between this iteration's distances and the previous one
    while difference:  # Repeat until all values stabilize
        difference = False
        # For every node v
        for v in graph:
            # For every neighbor u of v
            for u in graph[v]:
                if distances[u] > distances[v] + graph[v][u]:  # If u's distance > v's distance + weight of the edge (v, u)
                    distances[u] = distances[v] + graph[v][u]  # Update u's distance to v's distance + weight (v, u)
                    parent[u] = v  # Set it's parent to v
                    difference = True  # Values are still changing
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

backwardValueIteration(graph, 'd')
getDistances()
getPath('a')

# Output
# Vertex    Distance
# {'a': 4,
#  'b': 2,
#  'c': 1,
#  'd': 0,
#  'e': inf}
# Path from: a to start:
# ['a', 'b', 'c', 'd']
