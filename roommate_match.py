import pandas as pd
import numpy as np
from scipy.spatial import distance  

# code preferences using numbers and attach prefernce weights
# clean data as per format on the test_data_RA.csv
# append another collumn for roommate messages within the csv
# change location for accessing said data below
students = pd.read_csv('/Users/ayushmanroy/Desktop/Roommate_Matching/test_data_RA.csv')

# checking if data imported
print(students.head())

# select columns with preferences
selected_columns = [2,4,6]

# student as a vector list for matching
studentList = [(row[0], row[7], tuple(row[i] for i in selected_columns)) for row in students.values]

# check the cleaned list
print(studentList)

# closest neighbors and drop matched elements
def find_closest_neighbors(data):
    closest_pairs = []
    
    while len(data) > 1:
        # extract vectors from the data
        vectors = np.array([item[2] for item in data])
        
        # calculate distances between all pairs
        distances = distance.cdist(vectors, vectors, 'euclidean')
        
        # set diagonal (self-distances) to infinity to ignore them
        np.fill_diagonal(distances, np.inf)
        
        # find the pair with the minimum distance
        min_index = np.unravel_index(np.argmin(distances), distances.shape)
        
        # corresponding names and messages and append to the result
        closest_pairs.append((((data[min_index[0]][0], data[min_index[0]][1]), data[min_index[1]][0], data[min_index[1]][1])))
        # remove the matched elements 
        data = [data[i] for i in range(len(data)) if i not in min_index]
    
    return closest_pairs

closest_neighbors = find_closest_neighbors(studentList)

# export as excel maybe
print(closest_neighbors)