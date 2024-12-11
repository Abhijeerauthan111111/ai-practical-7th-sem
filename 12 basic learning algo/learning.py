import numpy as np
from sklearn import datasets, tree
import pandas as pd   #pip install numpy scikit-learn pandas or pip install --user numpy scikit-learn pandas

# Decision Tree Implementation
class DecisionTree:
    def __init__(self):
        self.tree = tree.DecisionTreeClassifier()
    
    def train(self, X, y):
        self.tree.fit(X, y)
    
    def predict(self, X):
        return self.tree.predict(X)

# Frame-based Knowledge Representation
class Frame:
    def __init__(self, name):
        self.name = name
        self.slots = {}
    
    def add_slot(self, slot_name, value):
        self.slots[slot_name] = value
    
    def get_slot(self, slot_name):
        return self.slots.get(slot_name)

def main():
    # Example using Decision Tree with Iris dataset
    print("Decision Tree Example:")
    iris = datasets.load_iris()
    dt = DecisionTree()
    dt.train(iris.data, iris.target)
    
    # Test prediction
    sample = iris.data[0].reshape(1, -1)
    prediction = dt.predict(sample)
    print(f"Predicted class: {prediction}")

    # Example using Frames
    print("\nFrame-based Knowledge Example:")
    # Create a frame for a car
    car_frame = Frame("Car")
    car_frame.add_slot("color", "red")
    car_frame.add_slot("make", "Toyota")
    car_frame.add_slot("year", 2022)
    
    # Access frame information
    print(f"Car color: {car_frame.get_slot('color')}")
    print(f"Car make: {car_frame.get_slot('make')}")
    print(f"Car year: {car_frame.get_slot('year')}")

if __name__ == "__main__":
    main()