from collections import defaultdict, deque  
class Graph:
    def __init__(self):   
        self.graph = defaultdict(list)
    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)   
    def bfs(self, start_vertex):     
        visited = set()
        queue = deque()
        queue.append(start_vertex)
        visited.add(start_vertex)      
        while queue: 
            current_vertex = queue.popleft()
            print(current_vertex, end=" ")         
            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Example usage
if __name__ == "__main__":
    # Create a graph
    g = Graph()
    # Add edges
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print("Breadth First Traversal (starting from vertex 0):")
    g.bfs(0)