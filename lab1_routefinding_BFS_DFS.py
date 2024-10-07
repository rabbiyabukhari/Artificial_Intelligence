from collections import deque

class Graph: 
    def __init__(self, citieslst, connectionslst):
        self.cities = citieslst  
        self.connections = connectionslst
        self.visited = set()  

    def dfs(self, curr, target, path):
        path.append(curr)  
        if curr == target:  
            return path
        self.visited.add(curr)  
        for neighbor in self.connections[curr]:
            if neighbor not in self.visited:
                result = self.dfs(neighbor, target, path.copy())  
                if result:  
                    return result
        return None 
    
    def bfs(self, start, target):
        queue = deque([(start, [start])])  
        visited = set()  
        while queue:
            curr, path = queue.popleft()  
            
            if curr == target: 
                return path
            
            visited.add(curr) 
            for neighbor in self.connections[curr]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
        return None 
    
    def find_path(self, strt, end, method="dfs"):
        if method == "dfs":
            return self.dfs(strt, end, [])
        elif method == "bfs":
            return self.bfs(strt, end)
        else:
            raise ValueError("Invalid method. Choose 'dfs' or 'bfs'.")

def main():
    filename = input('Enter the filename with network data: ')
    start = input('Enter the starting city: ')
    end = input('Enter the destination city: ') 
    with open(filename, 'r') as file:
        lines = file.readlines()   
    cities = []
    connections = []
    for i in range(1, len(lines)):  
        line = lines[i]
        parts = line.split()
        city_name = parts[1][:-1]  
        cities.append(city_name)
        neighbors = [int(parts[j]) for j in range(3, len(parts))]  
        connections.append(neighbors)

    graph = Graph(cities, connections)
    
    if start not in cities:
        print(f"{start} is not a valid city, please try again.")
    elif end not in cities:
        print(f"{end} is not a valid city, please try again.")
    else:
        strt_index = cities.index(start)
        end_index = cities.index(end)
        search_method = input('Choose search method (dfs or bfs): ').strip().lower()
        result = graph.find_path(strt_index, end_index, method=search_method)
        if result:
            path = ' -> '.join(cities[i] for i in result)
            print(f"Path found: {path}")
        else:
            print(f"No path exists from {start} to {end}.")
    return
            
main()
