from collections import deque

def bidirectional_search(graph, start, goal):
    # Queues for forward and backward searches
    forward_queue = deque([[start]])
    backward_queue = deque([[goal]])

    # Visited sets
    forward_visited = {start}
    backward_visited = {goal}

    # To reconstruct path
    forward_parents = {start: None}
    backward_parents = {goal: None}

    # Start searching
    while forward_queue and backward_queue:
        # Expand from the start side
        path = forward_queue.popleft()
        current = path[-1]

        # Check intersection with backward search
        if current in backward_visited:
            # Reconstruct path
            meet = current
            path_to_meet = []
            while meet is not None:
                path_to_meet.append(meet)
                meet = forward_parents[meet]
            path_to_meet.reverse()

            meet = current
            meet_to_goal = []
            while meet is not None:
                meet_to_goal.append(meet)
                meet = backward_parents[meet]
            meet_to_goal = meet_to_goal[1:]  # avoid repeating intersection

            return path_to_meet + meet_to_goal

        # Expand neighbors from start side
        for neighbor in graph[current]:
            if neighbor not in forward_visited:
                forward_visited.add(neighbor)
                forward_parents[neighbor] = current
                new_path = list(path)
                new_path.append(neighbor)
                forward_queue.append(new_path)

        # Expand from the goal side
        path = backward_queue.popleft()
        current = path[-1]

        if current in forward_visited:
            # Reconstruct path
            meet = current
            path_to_meet = []
            while meet is not None:
                path_to_meet.append(meet)
                meet = forward_parents[meet]
            path_to_meet.reverse()

            meet = current
            meet_to_goal = []
            while meet is not None:
                meet_to_goal.append(meet)
                meet = backward_parents[meet]
            meet_to_goal = meet_to_goal[1:]

            return path_to_meet + meet_to_goal

        # Expand neighbors from goal side
        for neighbor in graph[current]:
            if neighbor not in backward_visited:
                backward_visited.add(neighbor)
                backward_parents[neighbor] = current
                new_path = list(path)
                new_path.append(neighbor)
                backward_queue.append(new_path)

    return None


# --- Example Graph ---
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'H'],
    'F': ['C', 'I'],
    'G': ['D'],
    'H': ['E'],
    'I': ['F']
}

# --- Run Search ---
start = 'A'
goal = 'H'
path = bidirectional_search(graph, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path found.")
