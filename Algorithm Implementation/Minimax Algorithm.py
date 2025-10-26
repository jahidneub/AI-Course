def minimax(node, depth, maximizing_player, values, children):
    if depth == 0 or node not in children:
        return values[node]

    if maximizing_player:
        best = float("-inf")
        for child in children[node]:
            val = minimax(child, depth - 1, False, values, children)
            best = max(best, val)
        return best
    else:
        best = float("inf")
        for child in children[node]:
            val = minimax(child, depth - 1, True, values, children)
            best = min(best, val)
        return best

# ---- Input ----
n = int(input("Number of nodes: "))
children = {}
values = {}

print("Enter children (parent child1 child2 ...), or -1 if leaf:")
for _ in range(n):
    data = input().split()
    parent = data[0]
    if data[1] == "-1":  # leaf
        values[parent] = int(input(f"Value of leaf {parent}: "))
    else:
        children[parent] = data[1:]

root = input("Root node: ")
depth = int(input("Depth of tree: "))

score = minimax(root, depth, True, values, children)
print("Minimax Value:", score)
