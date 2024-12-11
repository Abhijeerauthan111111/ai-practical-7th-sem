from queue import PriorityQueue
def heuristic(a, b):
    """Manhattan distance heuristic"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(node, grid):
    """Get valid neighboring cells"""
    neighbors = []
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Right, Down, Left, Up
        new_x, new_y = node[0] + dx, node[1] + dy
        if (0 <= new_x < len(grid) and 
            0 <= new_y < len(grid[0]) and 
            grid[new_x][new_y] != '#'):  # '#' represents obstacles
            neighbors.append((new_x, new_y))
    return neighbors

def a_star(grid, start, goal):
    """A* pathfinding algorithm"""
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()[1]

        if current == goal:
            break

        for next_node in get_neighbors(current, grid):
            new_cost = cost_so_far[current] + 1  # Assuming cost of 1 for each step
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(goal, next_node)
                frontier.put((priority, next_node))
                came_from[next_node] = current

    # Reconstruct path
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from.get(current)
    path.reverse()
    
    return path if path[0] == start else []

# Example usage
if __name__ == "__main__":
    # Create a sample grid (0 = empty, # = obstacle)
    grid = [
        ["0", "0", "0", "0", "#"],
        ["#", "0", "0", "#", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "#", "#", "#", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    
    start = (0, 0)
    goal = (4, 4)
    
    path = a_star(grid, start, goal)
    
    if path:
        print("Path found:", path)
        # Visualize the path
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in path:
                    print("*", end=" ")
                else:
                    print(grid[i][j], end=" ")
            print()
    else:
        print("No path found!") 