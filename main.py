from collections import deque


def longest_path(graph: list) -> int:
    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)

# Helper function to perform topological sort
def topological_sort(graph: list) -> list[int]:
    indegree = {i: 0 for i in range(len(graph))}
    for node in graph:
        for neighbor, _ in node:
            indegree[neighbor] += 1

    que = deque([node for node in indegree if indegree[node] == 0])
    topo_order = []

    while que:
        node = que.popleft()
        topo_order.append(node)
        for neighbor, _ in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                que.append(neighbor)

    return topo_order

# Function to calculate longest path using topological sort
def calculate_longest_path(graph: list, topo_order: list[int]) -> int:
    dist = {node: 0 for node in range(len(graph))}
    
    for node in topo_order:
        for neighbor, weight in graph[node]:
            if dist[neighbor] < dist[node] + weight:
                dist[neighbor] = dist[node] + weight

    return max(dist.values())