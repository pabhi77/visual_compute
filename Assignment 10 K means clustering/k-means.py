# import csv
# import random
# from math import sqrt

# def read_csv(filename):
#     data = []
#     with open(filename, 'r') as file:
#         csv_reader = csv.reader(file)
#         for row in csv_reader:
#             if len(row) >= 2:
#                 data.append([float(row[0]), float(row[1])])
#             else:
#                 print(f"Ignoring row {row}, as it doesn't have enough values.")

#     return data

# def initialize_centroids(data, k):
#     return random.sample(data, k)

# def euclidean_distance(point1, point2):
#     return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# def assign_to_clusters(data, centroids):
#     clusters = [[] for _ in range(len(centroids))]

#     for point in data:
#         distances = [euclidean_distance(point, centroid) for centroid in centroids]
#         min_distance_index = distances.index(min(distances))
#         clusters[min_distance_index].append(point)

#     return clusters

# def update_centroids(clusters):
#     centroids = []

#     for cluster in clusters:
#         if cluster:
#             mean_x = sum(point[0] for point in cluster) / len(cluster)
#             mean_y = sum(point[1] for point in cluster) / len(cluster)
#             centroids.append([mean_x, mean_y])
#         else:
#             # If a cluster is empty, keep the centroid unchanged
#             centroids.append([0, 0])

#     return centroids

# def k_means(data, k, max_iterations=100):
#     centroids = initialize_centroids(data, k)

#     for _ in range(max_iterations):
#         clusters = assign_to_clusters(data, centroids)
#         new_centroids = update_centroids(clusters)

#         # Check for convergence
#         if new_centroids == centroids:
#             break

#         centroids = new_centroids

#     return clusters, centroids

# if __name__ == "__main__":
#     filename = 'inputcls.csv'  # Replace with the actual file name
#     k = 3  # Number of clusters

#     data = read_csv(filename)
#     clusters, centroids = k_means(data, k)

#     # Print the results
#     for i, cluster in enumerate(clusters):
#         print(f"Cluster {i + 1}: {cluster}")

#     print("Final Centroids:")
#     for i, centroid in enumerate(centroids):
#         print(f"Centroid {i + 1}: {centroid}")





#https://aryabhattacollege.ac.in/samplepaper/637227449508725497DataMining(Chapter8).pdf


 
import pandas as pd

# Load data from CSV
file_path = "C:\\Users\\Abhi\\OneDrive\\Desktop\\DM Codes\\Assignment 10 K means clustering\\inputcls.csv"
data = pd.read_csv(file_path)

# Assuming columns 'X' and 'Y' represent the coordinates of the points
points = data[['x', 'y']]

# Compute the initial center of the cluster
initial_cluster_center = points.mean()

# Print the initial cluster center
print("Initial Cluster Center:")
print(initial_cluster_center)

# Compute distances from each point to the initial cluster center manually
initial_distances = ((points - initial_cluster_center) ** 2).sum(axis=1) ** 0.5
print("\nDistances from Initial Cluster Center:")
print(initial_distances)

# Find the nearest point as the updated cluster center
nearest_point_index = initial_distances.idxmin()
updated_cluster_center = points.loc[nearest_point_index]

# Print the updated cluster center
print("\nUpdated Cluster Center:")
print(updated_cluster_center)

# Compute distances from the updated cluster center manually
updated_distances = ((points - updated_cluster_center) ** 2).sum(axis=1) ** 0.5
print("\nDistances from Updated Cluster Center:")
print(updated_distances)
