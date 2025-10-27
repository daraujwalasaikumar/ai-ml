# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}

visited = []

def dfs(graph, node, goal):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        if node == goal:
            print("\nGoal node", goal, "found!")
            return True  # Stop when goal is found
        for neighbour in graph[node]:
            if dfs(graph, neighbour, goal):
                return True
    return False

print("D F S Traversal")
dfs(graph, 'A', 'E')
