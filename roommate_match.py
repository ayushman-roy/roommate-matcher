import pandas as pd
import numpy as np
from scipy.spatial import distance  
import csv


# code preferences using numbers and attach prefernce weights
# clean data as per format on the test_data_RA.csv
# append another collumn for roommate messages within the csv
# change location for accessing said data below
students = pd.read_csv('/Users/ayushmanroy/Code/Roommate_Matching/DATA.csv')

# checking if data imported
print(students.head())

# encode the textual preferences as numeric values
# ensure that encoding takes into account how preferences are aligned and synergic 
# allot weights for each preference and then take the weighted preferences as final values

# select columns with weighted preferences
selected_columns = [1,2,3,4,5,6,7]

# student as a vector list for matching where student identifier must the first column
studentList = [(row[0], tuple(row[i] for i in selected_columns)) for row in students.values]

# check the cleaned list
print(studentList)

# closest neighbors and drop matched elements
def find_closest_neighbors(data):
    closest_pairs = []
    
    while len(data) > 1:
        # extract vectors from the data
        vectors = np.array([item[1] for item in data])
        
        # calculate distances between all pairs
        distances = distance.cdist(vectors, vectors, 'euclidean')
        
        # set diagonal (self-distances) to infinity to ignore them
        np.fill_diagonal(distances, np.inf)
        
        # find the pair with the minimum distance
        min_index = np.unravel_index(np.argmin(distances), distances.shape)
        
        # corresponding names and messages and append to the result
        closest_pairs.append((((data[min_index[0]][0]), data[min_index[1]][0])))
        # remove the matched elements 
        data = [data[i] for i in range(len(data)) if i not in min_index]
    
    return closest_pairs

closest_neighbors = find_closest_neighbors(studentList)

print(closest_neighbors)

# exporting the allocated roommates as .csv

filename = "/Users/ayushmanroy/Code/Roommate_Matching/Allocation.csv"

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Roommate 1', 'Roommate 2'])
    
    # Writing the data
    writer.writerows(closest_neighbors)

print(f"Data has been written to {filename}")
