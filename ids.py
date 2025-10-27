# Define the graph as an adjacency list
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}

visited_count = 0  # count total nodes visited


def DLS(node, goal, depth, limit):
    """
    Perform Depth-Limited Search (recursive)
    """
    global visited_count
    visited_count += 1

    if depth > limit:
        return False

    print(node, end=" ")

    if node == goal:
        return True

    if depth < limit:
        for neighbour in graph[node]:
            if DLS(neighbour, goal, depth + 1, limit):
                return True

    return False


def IDS(start, goal, max_depth):
    """
    Perform Iterative Deepening Search up to max_depth
    """
    global visited_count
    print(f"I D S Traversal upto depth {max_depth}")

    for limit in range(max_depth + 1):
        print(f"Depth {limit}:", end=" ")
        if DLS(start, goal, 0, limit):
            print(f"\nFound element at depth {limit}")
            print(f"Total nodes visited in IDS={visited_count}")
            return
        print()  # new line between depths


# ---- Main Program ----
start_node = 1
goal_node = 6
max_depth = 2

IDS(start_node, goal_node, max_depth)
