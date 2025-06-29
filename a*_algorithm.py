import heapq

def astar(graph,heuristic,start,goal):
    queue=[]
    visited=set()
    heapq.heappush(queue,(heuristic[start],0,start)) # goal cost from first node to itself is 0
    g_cost={start:0}
    
    while queue:
        f,g,current=heapq.heappop(queue)
        
        if current in visited:
            continue
        
        print(f"Visiting :{current}")
        
        if current==goal:
            print(f"gaol found :{current}")
            print(f"cost total :{g_cost[goal]}")
            return 
        
        for neighbour,cost in graph[current]:
            new_g=g_cost[current]+cost
            if neighbour not in visited and (neighbour not in g_cost or new_g<g_cost[neighbour] ):
                g_cost[neighbour]=new_g
                new_f=new_g+heuristic[neighbour]
                heapq.heappush(queue,(new_f,new_g,neighbour))
                
    print("Goal not reachable")        
        
graph={}
heuristic={}

n=int(input("Enter the no of nodes :"))

for i in range(n):
    u,v,cost=input("Enter the nodes u,v and cost:").split()
    cost=int(cost)
    
    if u not in graph:
        graph[u]=[]
        
    if v not in graph:
        graph[v]=[]
        
    graph[u].append((v,cost)) #here we have to put in tuple () bcoz as append takes only one object to add both grp them as one object inside tuple and then append
    graph[v].append((u,cost))
    
for node in graph:
    h=int(input(f"Enter the heuristic of {node}:"))
    heuristic[node]=h
    
start=input("Enter the start node :")
goal=input("Enter the goal node :")

print("A* algorithm")
astar(graph,heuristic,start,goal)
