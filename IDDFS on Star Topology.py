
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, node):
        self.neighbors.append(node)

def depth_limited_dfs(node, goal, depth_limit, depth):
    if depth > depth_limit:
        return None
    if node.name == goal:
        return node
    for neighbor in node.neighbors:
        result = depth_limited_dfs(neighbor, goal, depth_limit, depth + 1)
        if result is not None:
            return result
    return None

def iddfs(start, goal, max_depth):
    for depth_limit in range(max_depth + 1):
        result = depth_limited_dfs(start, goal, depth_limit, 0)
        if result is not None:
            return result

    return None


# Example usage
# Create nodes for the star topology
center = Node("Center")
leaf_nodes = []

# Add 7 leaf nodes to the center node
num_leaf_nodes = 7
for i in range(1, num_leaf_nodes + 1):
    leaf = Node("Leaf" + str(i))
    center.add_neighbor(leaf)
    leaf_nodes.append(leaf)

# Define the goal node
goal_node = "Leaf3"

# Perform IDDFS search
result_node = iddfs(center, goal_node, 3)

# Check the result
if result_node is not None:
    print("Goal node found:", result_node.name)
else:
    print("Goal node not found")
