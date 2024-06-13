# import pandas as pd
# import numpy as np

# def min_max_normalization(value, old_min, new_min, old_range, new_range):
#     normalized_value = ((value - old_min)/old_range) * new_range + new_min
#     return normalized_value

# def standard_deviation(values):
#     mean = np.mean(values)
#     standard_deviation = 0
#     for value in values:
#         standard_deviation += (value - mean) ** 2
#     std_dev = np.sqrt(standard_deviation / len(values))

#     return std_dev

# input_file = "C:\\Users\\Abhi\\OneDrive\\Desktop\\DM Codes\\Assignment 2 min max z score\\input_data.csv"
# data = pd.read_csv(input_file)

# values = data.values.flatten()
# print(values)
# new_max = int(input("Enter the new minimum: "))
# new_min = int(input("Enter the new maximum: "))

# old_range = values.max(axis = 0) - values.min(axis = 0)
# new_range = new_max - new_min

# normalized_values = []
# for value in values:
#     normalized_value = min_max_normalization(value, values.min(), new_min, old_range, new_range)
#     normalized_values.append(normalized_value)

# standard_normalized_values = []
# standard_deviation_data = standard_deviation(values)
# for value in values:
#     normalized_value = (value - np.mean(values)) / standard_deviation_data
#     standard_normalized_values.append(normalized_value)

# print(normalized_values)
# print(standard_normalized_values)

import csv

def min_max_normalization(value, old_min, old_max, new_min, new_max):
    old_range = old_max - old_min
    new_range = new_max - new_min
    normalized_value = ((value - old_min) / old_range) * new_range + new_min
    return normalized_value

def calculate_mean(values):
    total = sum(values)
    count = len(values)
    return total / count

def calculate_standard_deviation(values, mean):
    variance = sum((value - mean) ** 2 for value in values) / len(values)
    return variance ** 0.5

# Load the input data
input_file = "C:\\Users\\Abhi\\OneDrive\\Desktop\\DM Codes\\Assignment 2 min max z score\\input_data.csv"

values = []
with open(input_file, mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row if there is one
    for row in csv_reader:
        for item in row:
            try:
                values.append(float(item))
            except ValueError:
                print(f"Skipping non-numeric value: {item}")

print("Original Values:", values)

# Get new min and max values from the user
new_min = float(input("Enter the new minimum: "))
new_max = float(input("Enter the new maximum: "))

# Calculate old min and max
old_min = min(values)
old_max = max(values)

# Apply min-max normalization
normalized_values = [min_max_normalization(value, old_min, old_max, new_min, new_max) for value in values]

# Calculate mean and standard deviation for Z-score normalization
mean = calculate_mean(values)
std_dev = calculate_standard_deviation(values, mean)

# Apply Z-score normalization
standard_normalized_values = [(value - mean) / std_dev for value in values]

print("Min-Max Normalized Values:", normalized_values)
print("Standard Normalized (Z-score) Values:", standard_normalized_values)

