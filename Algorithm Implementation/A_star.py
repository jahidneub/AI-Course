from heapq import heappush, heappop

def a_star(graph, start, goal, heuristic):
    open_set = [(heuristic[start], 0, start)]
    parent = {start: None}
    g_cost = {start: 0}
    visited = set()

    while open_set:
        _, cost, node = heappop(open_set)
        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]

        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                parent[neighbor] = node
                f = new_cost + heuristic[neighbor]
                heappush(open_set, (f, new_cost, neighbor))

    return None

# ---- Input ----
n = int(input("Number of nodes (n): "))
m = int(input("Number of edges (m): "))

graph = {}
print("Enter edges as: u v w (node names + weight)")
for _ in range(m):
    u, v, w = input().split()
    w = int(w)
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, w))
    graph[v].append((u, w))

heuristic = {}
print("Enter heuristic values (node h):")
for node in graph:
    heuristic[node] = int(input(f"h({node}): "))

start = input("Start node: ")
goal = input("Goal node: ")

path = a_star(graph, start, goal, heuristic)
print("A* Path:", path)
