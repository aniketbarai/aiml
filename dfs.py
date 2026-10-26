def dfs(node,visited,graph):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        
        for neighbors in graph.get(node,[]):
            dfs(neighbors,visited,graph)
            
#Create an empty graph
graph={}

#Enter the number of nodes
nodes = int(input("Enter number of nodes: "))

for i in range(nodes):
    node = input(f"Enter node {i + 1}: ")
    neighbors = input(f"Enter neighbors of node {node} (space-separated): ")
    graph[node] = neighbors
    
#Create an empty set to store unique numbers
visited = set()
    
#Enter start node
start = input("Enter starting node: ")

#Print graph
print("Graph:")
print(graph)

#DFS Traversal
print("DFS Traversal:")
dfs(start,visited,graph)