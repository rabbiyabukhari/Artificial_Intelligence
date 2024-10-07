from collections import deque

def dfs(graph,node,stack,visited,path):
    path.append(node)
    if stack!=[]:
        s = stack.pop()
        print(s, end = ' ')
        for n in graph[s]:
            if n not in visited:
                visited.add(n)
                stack.append(n)
                return dfs(graph,n,stack,visited,path)  
def dfsrec(graph,node):
    visited = set()
    stack = []
    visited.add(node)
    stack.append(node) 
    return dfs(graph,node,stack,visited,[])  

def bfs(graph, node):
    visited = set()
    queue = deque()
    visited.add(node)
    queue.append(node)
    while queue:
        s = queue.popleft()
        print(s, end = ' ')
        for n in graph[s]:
            if n not in visited:
                visited.add(n)
                queue.append(n)         
                  
#graph is a dictionary containing vertices as key
#and their corresponding adjlist as value  
graph={1:[2,7],2:[3,4,5],3:[],4:[],5:[6],6:[],7:[8],8:[9],9:[]}  
node=1
dfsrec(graph,node)
print()
bfs(graph,9)
  

    
