# Practical 1(a): 
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






# Practical 1(b):
##from collections import deque
##
##def bfs_paths(graph, start, goal):
##    queue = deque([[start]])  # Each element is a path
##    paths = []
##
##    while queue:
##        path = queue.popleft()
##        node = path[-1]
##
##        if node == goal:
##            paths.append(path)
##
##        for neighbor in graph.get(node, []):
##            if neighbor not in path:  # Avoid cycles
##                queue.append(path + [neighbor])
##
##    return paths
##
##
### Example graph
##graph = {
##    'A': ['B', 'C'],
##    'B': ['D', 'E'],
##    'C': ['F', 'A'],
##    'D': [],
##    'E': ['F'],
##    'F': []
##}
##
### Find all paths from C to F
##print(bfs_paths(graph, 'C', 'F'))


