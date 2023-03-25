# write a python code of taking the grid from user for building the matrix
# show the matrix
# take start and end node from the user
# show the shortest path
from queue import Queue

def bfs(graph, start, end):
    visited = [False] * len(graph)
    paths = {start: [start]}

    q = Queue()
    q.put(start)
    visited[start] = True

    while not q.empty():
        node = q.get()

        if node == end:
            return paths[node]
        for neighbour in range(len(graph[node])):
            if graph[node][neighbour] != 0 and not visited[neighbour]:
                visited[neighbour] = True
                paths[neighbour] = paths[node] + [neighbour]
                q.put(neighbour)
    return None


n = int(input("Enter the grid size: "))
"""graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0]
]"""
"""graph = [
    [0, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0]
]"""
graph = []
print("Enter the entries row wise:")
# taking matrix input from user
for i in range(n):
    a = []
    for j in range(n):
        a.append(int(input()))
    graph.append(a)
# showing the matrix
for i in range(n):
    for j in range(n):
        print(graph[i][j], end=" ")
    print()
start_node = int(input("Enter start node: "))
end_node = int(input("Enter end node: "))
# call the bfs function
shortest_path = bfs(graph, start_node, end_node)
if shortest_path:
    print(f"The shortest path from {start_node} to {end_node} is: {shortest_path}")
else:
    print(f"No shortest path from {start_node} to {end_node}")