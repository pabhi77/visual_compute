# import pandas as pd
# from scipy.cluster.hierarchy import linkage, dendrogram
# import matplotlib.pyplot as plt

# input_file = 'input_data.csv'
# data = pd.read_csv(input_file, index_col = 0)

# linkage_matrix = linkage(data, method = 'single')
# print(linkage_matrix)

# plt.figure(figsize = (10,6))

# dendrogram(linkage_matrix, labels = data.index)
# plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def hierarchical_clustering(input_file):
    # Read data from CSV
    data = pd.read_csv(input_file, index_col=0)

    # Initialize dendrogram labels
    labels = list(data.index)

    # Initialize distance matrix
    distance_matrix = np.zeros((len(labels), len(labels)))

    # Fill distance matrix with values from CSV
    for i, row_label in enumerate(labels):
        for j, col_label in enumerate(labels):
            if i != j:
                distance_value = data.at[row_label, col_label]
                if not pd.isnull(distance_value):
                    distance_matrix[i, j] = distance_value

    num_clusters = len(labels)
    clusters = []

    # Perform agglomerative hierarchical clustering
    while num_clusters > 1:
        # Find the closest pair of clusters
        min_dist = np.inf
        min_indices = None
        for i in range(len(labels)):
            for j in range(i + 1, len(labels)):
                if distance_matrix[i, j] < min_dist:
                    min_dist = distance_matrix[i, j]
                    min_indices = (i, j)

        # Merge the closest pair of clusters
        i, j = min_indices
        new_label = f"{labels[i]} & {labels[j]}"
        new_distances = np.minimum(distance_matrix[i], distance_matrix[j])
        distance_matrix = np.delete(distance_matrix, [i, j], axis=0)
        distance_matrix = np.delete(distance_matrix, [i, j], axis=1)

        # Ensure new_distances has the same shape as distance_matrix
        if len(new_distances) < len(labels):
            new_distances = np.append(new_distances, np.zeros((len(labels) - len(new_distances))))

        distance_matrix = np.vstack((distance_matrix, new_distances))
        new_distances = np.append(new_distances, np.zeros((1, len(labels))))
        distance_matrix = np.column_stack((distance_matrix, new_distances))
        labels = [new_label if l in (labels[i], labels[j]) else l for l in labels]

        # Store cluster for dendrogram
        clusters.append((labels[i], labels[j]))

        num_clusters -= 1

    return clusters

def plot_dendrogram(clusters):
    plt.figure(figsize=(10, 6))
    for idx, (cluster1, cluster2) in enumerate(clusters):
        plt.plot([idx, idx], [0, 1], color='black')
        plt.plot([idx, idx+1], [1, 1], color='black')
        plt.plot([idx+1, idx+1], [1, 0], color='black')
        plt.text((idx + idx + 1) * 0.5, 1.05, f'{cluster1} & {cluster2}', ha='center', va='bottom', rotation=90)
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('Cluster Index')
    plt.ylabel('Distance')
    plt.show()

if __name__ == "__main__":
    input_file = "C:\\Users\\Abhi\\OneDrive\\Desktop\\DM Codes\\Assignment 11 Hierarchical Clustering\\11input.csv"
    clusters = hierarchical_clustering(input_file)
    plot_dendrogram(clusters)






#"C:\\Users\\Abhi\\OneDrive\\Desktop\\DM Codes\\Assignment 11 Hierarchical Clustering\\11input.csv"