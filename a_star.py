# Graph with costs
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 2)],
    'C': [('F', 2), ('G', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

# Heuristic values
h = {
    'A': 6, 'B': 5, 'C': 4,
    'D': 4, 'E': 2, 'F': 2, 'G': 0
}

def astar(start, goal):
    visited = []
    queue = [(h[start], 0, start)]

    while queue:
        queue.sort()
        f, cost, node = queue.pop(0)

        if node in visited:
            continue

        print(node, end=" ")
        visited.append(node)

        if node == goal:
            print("\nGoal Found! Cost =", cost)
            return

        for neighbour, edge_cost in graph[node]:
            if neighbour not in visited:
                new_cost = cost + edge_cost
                f = new_cost + h[neighbour]
                queue.append((f, new_cost, neighbour))

    print("\nGoal Not Found!")

astar('A', 'G')
