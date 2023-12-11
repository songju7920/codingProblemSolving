from collections import deque

def bfs(graph, start, distence):
    distence[1] = 1
    
    deq = deque()
    deq.append(start)
    
    while deq:
        next = deq.popleft()
        for node in graph[next]:
            if distence[node] == 0:
                distence[node] = distence[next] + 1;
                deq.append(node);
            
    return distence.count(max(distence))
            

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    distence = [0] * (n + 1)
        
    for data in edge:
        graph[data[0]].append(data[1])
        graph[data[1]].append(data[0])
    
    return bfs(graph, 1, distence)