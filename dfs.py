def dfs(graph,start,visited=None):
    if visited is None:
        visited=set()
    visited.add(start)
    print(start,end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)

if __name__=="__main__":
    

    graph={}
    num=int(input("Enter no of nodes :"))

    for i in range(num):
        u,v=input("Enter edge u,v:").split()

        if u not in graph:
            graph[u]=[]     #creates a empty list for u

        if v not in graph:
            graph[v]=[]    #creates a empty list for v

        graph[u].append(v)
        graph[v].append(u)

    start=input("Enter start node :")

    print("DFS Traversal :",end=" ")
    dfs(graph,start)        
    
  