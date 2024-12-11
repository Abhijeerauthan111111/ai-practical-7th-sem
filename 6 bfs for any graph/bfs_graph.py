from collections import defaultdict, deque

class Graph:
    def __init__(self):
        # Using defaultdict to store the graph as an adjacency list
        self.graph = defaultdict(list)
    
    def add_edge(self, vertex1, vertex2):
        # Add edges to the graph (undirected)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)
    
    def bfs(self, start_vertex):
        # Set to keep track of visited vertices
        visited = set()
        # Queue for BFS traversal
        queue = deque()
        
        # Add the start vertex to queue and mark it as visited
        queue.append(start_vertex)
        visited.add(start_vertex)
        
        while queue:
            # Remove vertex from queue and print it
            current_vertex = queue.popleft()
            print(current_vertex, end=" ")
            
            # Get all adjacent vertices
            # If an adjacent vertex has not been visited, add it to queue
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

    # Create a larger, more complex graph
    g = Graph()

    # Creating a graph that resembles a social network
    g.add_edge(0, 1)  # Person 0 is friends with Person 1
    g.add_edge(0, 2)  # Person 0 is friends with Person 2
    g.add_edge(1, 3)  # Person 1 is friends with Person 3
    g.add_edge(2, 3)  # Person 2 is friends with Person 3
    g.add_edge(3, 4)  # Person 3 is friends with Person 4
    g.add_edge(4, 5)  # Person 4 is friends with Person 5
    g.add_edge(5, 6)  # Person 5 is friends with Person 6
    g.add_edge(6, 7)  # Person 6 is friends with Person 7
    g.add_edge(7, 8)  # Person 7 is friends with Person 8
    g.add_edge(8, 9)  # Person 8 is friends with Person 9
    g.add_edge(9, 0)  # Person 9 is friends with Person 0
    g.add_edge(1, 4)  # Additional connections
    g.add_edge(2, 5)
    g.add_edge(3, 6)

    print("\n\nBreadth First Traversal of larger graph (starting from vertex 0):")
    g.bfs(0)