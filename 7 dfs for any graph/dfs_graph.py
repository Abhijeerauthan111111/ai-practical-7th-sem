def dfs(graph, start, visited=None):
    # Initialize visited set if None
    if visited is None:
        visited = set()
    
    # Mark current node as visited and print it
    visited.add(start)
    print(start, end=' ')
    
    # Recur for all adjacent vertices
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage
if __name__ == "__main__":
    # Define the graph using a dictionary (adjacency list)
    # Each key is a vertex and its value is a list of adjacent vertices
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("Depth-First Search starting from vertex 'A':")
    dfs(graph, 'A')

    # Example with a different graph using numbers
    graph_numbers = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1, 5],
        5: [2, 4]
    }

    print("\n\nDFS starting from vertex 0:")
    dfs(graph_numbers, 0)