# show the shortest path from graph
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


graph = [
    [0, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0]
]

start_node = 0
end_node = 3
# call the bfs function
shortest_path = bfs(graph, start_node, end_node)
if shortest_path:
    print(f"The shortest path from {start_node} to {end_node} is: {shortest_path}")
else:
    print(f"No shortest path from {start_node} to {end_node}")