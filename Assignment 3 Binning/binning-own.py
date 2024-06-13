# import numpy as np
# import pandas as pd 

# input_file = 'C:\\Users\\Abhi\\OneDrive\\Desktop\\DM Codes\\Assignment 3 Binning\\input_data.csv'
# data = pd.read_csv(input_file)

# array = data.values.flatten()
# num_bins = int(input("Enter the number of bins"))

# bin_width = int(((max(array) - min(array)) / num_bins))

# for x in array:
#     bin_index = max(0, min(int((x - min(array)) / bin_width), num_bins-1))
#     print(f"{x} : bin {bin_index}")

# print ("\n")

# np.sort(array)
# bin_width_freq = len(array) / num_bins
# bin_index_freq = 0
# count = 1
# for i in range(len(array) - 1):
#     print(f"{x} : Bin: {int(i/bin_width_freq)}")

import csv

def equal_width_binning(array, num_bins):
    min_val = min(array)
    max_val = max(array)
    bin_width = (max_val - min_val) / num_bins

    bins = []
    for x in array:
        bin_index = max(0, min(int((x - min_val) / bin_width), num_bins - 1))
        bins.append(bin_index)
        print(f"{x} : bin {bin_index}")
    return bins

def equal_frequency_binning(array, num_bins):
    sorted_array = sorted(array)
    bin_size = len(array) // num_bins

    bins = []
    for i, x in enumerate(sorted_array):
        bin_index = i // bin_size
        if bin_index >= num_bins:  # Edge case for last bin
            bin_index = num_bins - 1
        bins.append((x, bin_index))
        print(f"{x} : bin {bin_index}")
    return bins

# Load the input data
input_file = 'C:\\Users\\Abhi\\OneDrive\\Desktop\\DM Codes\\Assignment 3 Binning\\input_data.csv'
array = []

with open(input_file, mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row if there is one
    for row in csv_reader:
        for item in row:
            try:
                array.append(float(item))
            except ValueError:
                print(f"Skipping non-numeric value: {item}")

print("Original Array:", array)

# Get the number of bins from the user
num_bins = int(input("Enter the number of bins: "))

# Perform equal-width binning
print("\nEqual-width Binning:")
equal_width_bins = equal_width_binning(array, num_bins)

print("\nEqual-frequency Binning:")
# Perform equal-frequency binning
equal_frequency_bins = equal_frequency_binning(array, num_bins)






