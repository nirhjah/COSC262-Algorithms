from math import inf
from next_vertex import next_vertex
from adjacency_list import adjacency_list


def dijkstra(adj_list, s):
    """Dijkstra's algorithm to give shortest path tree"""
    n = len(adj_list)
    in_tree = [False]*n
    distance = [float('inf')]*len(adj_list)    
    parent = [None]*n
    distance[s] = 0
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if in_tree[v] == False and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
    return parent, distance
                        
                        
graph_string = """\
D 3 W
1 0 3
2 0 1
1 2 1
"""

print(dijkstra(adjacency_list(graph_string), 1))
print(dijkstra(adjacency_list(graph_string), 2))