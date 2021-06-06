def adjacency_list(graph_str):
    """Takes a graph string and returns the adjacency list"""

    lines = graph_str.splitlines()
    header = lines[0].split()

    if len(header) > 2:
        graph_type, vertices, weight = header[0], header[1], header[2]
    else:
        graph_type, vertices = header[0], header[1]
        weight = None

    edges = lines[1:]
    adj_list = [[] for _ in range(int(vertices))]

    if len(edges) > 0:
        for edge in edges:
            if weight == 'W':
                v1, v2, w = edge.split()
                v1, v2, w = int(v1), int(v2), int(w)
            else:
                v1, v2 = edge.split()
                v1, v2 = int(v1), int(v2)
                w = None
                
            if graph_type == 'U':
                adj_list[v1] += [(v2, w)]
                adj_list[v2] += [(v1, w)]
            else:
                adj_list[v1] += [(v2, w)]
    return adj_list

def dfs_tree(adj_list, start):
    """dfs"""
    parent = [None]*len(adj_list)
    state = ['U']*len(adj_list)
   
    state[start] = 'D'
    dfs_loop(adj_list, start, state, parent)
    return parent
    
    
    
def dfs_loop(adj_list, u, state, parent):
    """dfs loop"""
    for exact_v in adj_list[u]:
        v = exact_v[0]
        if state[v] == 'U':
            state[v] = 'D'
            parent[v] = u
            dfs_loop(adj_list, v, state, parent)
    state[u] = 'P'
    
    

# graph from the textbook example
graph_string = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

print(dfs_tree(adjacency_list(graph_string), 1))
    
    
    
    



    