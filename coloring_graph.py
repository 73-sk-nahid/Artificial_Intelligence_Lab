# Define the graph as a dictionary of nodes and their neighbors
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

# Define a dictionary to store the colors of each node
colors = {}

# Define a list of available colors
available_colors = ['red', 'green', 'blue', 'yellow']

# Loop through each node in the graph
for node in graph:
    # Initialize the set of used colors for this node
    used_colors = set()

    # Loop through the neighbors of this node and add their colors to the set of used colors
    for neighbor in graph[node]:
        if neighbor in colors:
            used_colors.add(colors[neighbor])

    # Find the first available color that is not used by any of the neighbors
    for color in available_colors:
        if color not in used_colors:
            colors[node] = color
            break

# Print the color of each node
for node in colors:
    print(node + ': ' + colors[node])