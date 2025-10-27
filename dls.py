# Define the graph as an adjacency list
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [7, 8],
    5: [],
    6: [],
    7: [],
    8: []
}

visited = []

def DLS(node, goal, depth, limit):
    if depth > limit:
        return False

    print(node, end=" ")
    visited.append(node)

    if node == goal:
        print("\nfound element")
        return True

    for neighbour in graph[node]:
        if neighbour not in visited:
            if DLS(neighbour, goal, depth + 1, limit):
                return True
    return False


# ---- Main Program ----
limit = 3
start_node = 1
goal_node = 8

print(f"D L S Traversal (limit={limit}):", end=" ")
DLS(start_node, goal_node, 0, limit)
