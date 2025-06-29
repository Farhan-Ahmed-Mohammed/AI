import heapq

def greedy_bfs(graph,start,goal,heuristic):
    visited=set()
    queue=[] # its a list as we define it as [] we name it queue
    
    heapq.heappush(queue,(heuristic[start],start)) # heapq puts elements in ascednig order heuristic start is heuristiv calue of start
    
    while queue:
        h,current=heapq.heappop(queue)
        
        if current in visited:
            continue
        
        print("Visiting :",current)
        visited.add(current)
        
        if current==goal:
            print("Goal found",current)
            return
        
        for neighbour in graph[current]:
            if neighbour not in visited:
                heapq.heappush(queue,(heuristic[neighbour],neighbour))
                
    print("Goal not reachable")
        
        
graph={}
heuristic={}

n=int(input("Enter the no of nodes :"))

for i in range(n):
    u,v=input("Enter the nodes u,v:").split()
    
    if u not in graph:
        graph[u]=[]
        
    if v not in graph:
        graph[v]=[]
        
    graph[u].append(v)
    graph[v].append(u)
    
for node in graph:
    h=int(input(f"Enter the heuristic for {node}:"))
    heuristic[node]=h
    
start=input("Enter the starting node :")
goal=input("Enter the gaol node :")
print("Greedy BFS")
greedy_bfs(graph,start,goal,heuristic)
        
