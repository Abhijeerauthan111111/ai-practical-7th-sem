import random
import math

def objective_function(x):
    """
    Simple objective function to optimize
    In this case: f(x) = -(x-2)^2 + 4
    This function has a maximum at x = 2
    """
    return -(x - 2)**2 + 4

def hill_climbing(max_iterations=1000, step_size=0.1):
    # Start with a random solution
    current_x = random.uniform(-10, 10)
    current_value = objective_function(current_x)
    
    for i in range(max_iterations):
        # Generate slightly modified neighbor solutions
        left_neighbor = current_x - step_size
        right_neighbor = current_x + step_size
        
        # Evaluate neighbors
        left_value = objective_function(left_neighbor)
        right_value = objective_function(right_neighbor)
        
        # Find the best neighbor
        if left_value > current_value and left_value > right_value:
            current_x = left_neighbor
            current_value = left_value
        elif right_value > current_value:
            current_x = right_neighbor
            current_value = right_value
        else:
            # If no better neighbor is found, we've reached a local maximum
            break
            
        print(f"Iteration {i}: x = {current_x:.4f}, f(x) = {current_value:.4f}")
    
    return current_x, current_value

def main():
    print("Hill Climbing Algorithm for Function Optimization")
    print("Objective: Maximize f(x) = -(x-2)^2 + 4")
    print("\nStarting optimization...")
    
    best_x, best_value = hill_climbing()
    
    print("\nOptimization Results:")
    print(f"Best x found: {best_x:.4f}")
    print(f"Best value found: {best_value:.4f}")
    print(f"True optimal x: 2.0000")
    print(f"True optimal value: 4.0000")

if __name__ == "__main__":
    main()