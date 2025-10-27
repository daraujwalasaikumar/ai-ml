from heapq import heappop, heappush

# Define the graph as an adjacency list with edge costs
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'D': 4, 'E': 7},
    'C': {'A': 5, 'E': 3},
    'D': {'B': 4, 'F': 4},
    'E': {'B': 7, 'C': 3, 'F': 2},
    'F': {'D': 4, 'E': 2}
}

# Define heuristic values (straight-line distance estimates to goal 'F')
heuristic = {
    'A': 8,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 0
}

def astar(graph, start, goal):
    # Priority queue: (f = g + h, current_node, path, g)
    open_set = []
    heappush(open_set, (heuristic[start], start, [start], 0))
    visited = set()

    while open_set:
        f, current, path, g = heappop(open_set)

        if current == goal:
            return path, g

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph[current].items():
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + heuristic[neighbor]
                heappush(open_set, (f_new, neighbor, path + [neighbor], g_new))

    return None, float('inf')


# Run A* algorithm
path, cost = astar(graph, 'A', 'F')

print("Shortest path found :", path)
print("Total cost :", cost)
