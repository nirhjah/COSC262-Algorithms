def next_vertex(in_tree, distance):
    """Takes two arrays, in_tree and distance, and returns the vertex
    that should be added to the tree next"""
    listo = []
    for i in range(len(in_tree)):
        item = in_tree[i]
        if item == False:
            listo.append((distance[i], i))
    answer = min(listo)
    return answer[1]