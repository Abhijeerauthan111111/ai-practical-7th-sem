import numpy as np

# Activation function: Sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Input dataset
inputs = np.array([[0, 0],
                   [0, 1],
                   [1, 0],
                   [1, 1]])

# Output dataset
outputs = np.array([[0], [1], [1], [0]])

# Seed the random number generator
np.random.seed(1)

# Initialize weights randomly with mean 0
weights_0 = 2 * np.random.random((2, 4)) - 1
weights_1 = 2 * np.random.random((4, 1)) - 1

# Training the neural network
for epoch in range(10000):
    # Forward propagation
    layer_0 = inputs
    layer_1 = sigmoid(np.dot(layer_0, weights_0))
    layer_2 = sigmoid(np.dot(layer_1, weights_1))
    
    # Calculate the error
    layer_2_error = outputs - layer_2
    
    if (epoch % 1000) == 0:
        print(f"Error at epoch {epoch}: {np.mean(np.abs(layer_2_error))}")
    
    # Backpropagation
    layer_2_delta = layer_2_error * sigmoid_derivative(layer_2)
    layer_1_error = layer_2_delta.dot(weights_1.T)
    layer_1_delta = layer_1_error * sigmoid_derivative(layer_1)
    
    # Update weights
    weights_1 += layer_1.T.dot(layer_2_delta)
    weights_0 += layer_0.T.dot(layer_1_delta)

# Output the final results
print("Output after training:")
print(layer_2)