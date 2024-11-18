from collections import deque

def solution(n, vertex):
    graph = {i: [] for i in range(1, n + 1)}
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    
    distances = [-1] * (n + 1) 
    distances[1] = 0  
    queue = deque([1])  
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == -1: 
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    
    max_distance = max(distances)
    return distances.count(max_distance)