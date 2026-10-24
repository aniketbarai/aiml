graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

h = {
    'A': 6, 'B': 4, 'C': 3,
    'D': 5, 'E': 2, 'F': 1, 'G': 0
}

def gbfs(start, goal):
    visited = []
    queue = [start]

    while queue:
        node = min(queue, key=lambda x: h[x])
        queue.remove(node)

        if node in visited:
            continue
        print(node, end=" ")
        visited.append(node)

        if node == goal:
            print("\nGoal Found!")
            return
        queue.extend(graph[node])

    print("\nGoal Not Found!")

print("GBFS Traversal:")
gbfs('A', 'G')
