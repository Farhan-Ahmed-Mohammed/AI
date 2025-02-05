from collections import deque

def bfs(graph,start):
    visited=set()
    queue=deque([start])

    while queue:
        node=queue.popleft()

        if node not in visited:
            print(node," ")
            visited.add(node)

        for neighbour in graph[node]:
             if neighbour not in visited:
                queue.append(neighbour) 

if __name__=="__main__":
    

    graph={}
    num=int(input("Enter no of nodes :"))

    for i in range(num):
        u,v=input("Enter endge u,v:").split()

        if u not in graph:
            graph[u]=[]

        if v not in graph:
            graph[v]=[]

        graph[u].append(v)
        graph[v].append(u)

    start=input("Enter start node :")

    print("BFS Traversal :")
    bfs(graph,start)        
    




          
    