def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]

    if start == goal:
        yield path

    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])


# Example graph (adjacency as sets for easier difference operation)
graph = {
    'A': {'B', 'C'},
    'B': {'D', 'E'},
    'C': {'F', 'A'},
    'D': set(),
    'E': {'F'},
    'F': set()
}

# Find all paths from C to F 
print(list(dfs_paths(graph, 'C', 'F')))
