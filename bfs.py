from collections import deque


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}

def bfs_traversal(graph, start, goal):
    visited = []
    queue = deque([start])

    print("B F S Traversal")

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            if node == goal:
                print("\nGoal node", goal, "found !")
                return
            queue.extend(graph[node])


bfs_traversal(graph, 'A', 'E')
