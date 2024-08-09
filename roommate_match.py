import pandas as pd
import numpy as np
from scipy.spatial import distance  

students = pd.read_csv('/Users/ayushmanroy/Desktop/Roommate_Matching/test_data_RA.csv')

print(students.head())

selected_columns = [2,4,6]
studentList = [(row[0], tuple(row[i] for i in selected_columns)) for row in students.values]

print(studentList)

# Function to find closest neighbors and drop matched elements
def find_closest_neighbors(data):
    closest_pairs = []
    
    while len(data) > 1:
        # Extract vectors from the data
        vectors = np.array([item[1] for item in data])
        
        # Calculate distances between all pairs
        distances = distance.cdist(vectors, vectors, 'euclidean')
        
        # Set diagonal (self-distances) to infinity to ignore them
        np.fill_diagonal(distances, np.inf)
        
        # Find the pair with the minimum distance
        min_index = np.unravel_index(np.argmin(distances), distances.shape)
        
        # Get the corresponding first elements and append to the result
        closest_pairs.append((data[min_index[0]][0], data[min_index[1]][0]))
        
        # Remove the matched elements from the list
        data = [data[i] for i in range(len(data)) if i not in min_index]
    
    return closest_pairs

# Find and print closest neighbors
closest_neighbors = find_closest_neighbors(studentList)
print(closest_neighbors)