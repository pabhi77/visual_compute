# import numpy as np 
# import pandas as pd

# def calculate_entropy(data, target_class):
#     class_count = data[target_class].value_counts()
#     entropy = 0
#     for count in class_count:
#         probability = count / len(data)
#         entropy -= probability * np.log2(probability)
#     return entropy

# def calculate_info_gain(data, attribute, target_class):
#     total_entropy = calculate_entropy(data, target_class)
#     attribute_values = data[attribute].unique()

#     attribute_entropy = 0
#     for value in attribute_values:
#         subset = data[data[attribute] == value]
#         subset_entropy = calculate_entropy(subset, target_class)
#         weight = len(subset) / len(data)
#         attribute_entropy += weight * subset_entropy

#     info_gain = total_entropy - attribute_entropy
#     return info_gain

# # Input file
# input_file = "C:\\Users\\Abhi\\OneDrive\\Desktop\\DM\\Data_Mining\\DM Codes\\Assignment 4 Info Gain\\input_infodata.csv"
# data = pd.read_csv(input_file)

# # Target column
# target_class = 'PlayTennis'

# # Attributes
# attributes = data.columns.drop(target_class)

# # Calculate and print information gain for each attribute
# for attribute in attributes:
#     info_gain = calculate_info_gain(data, attribute, target_class)
#     print(f"Information Gain for {attribute}: {info_gain}")
import numpy as np 
import pandas as pd

def calculate_entropy(data, target_class):
    class_count = data[target_class].value_counts()
    entropy = 0
    for count in class_count:
        probability = count / len(data)
        entropy -= probability * np.log2(probability)
    return entropy

def calculate_info_gain(data, attribute, target_class):
    total_entropy = calculate_entropy(data, target_class)
    attribute_values = data[attribute].unique()

    attribute_entropy = 0
    for value in attribute_values:
        subset = data[data[attribute] == value]
        subset_entropy = calculate_entropy(subset, target_class)
        weight = len(subset) / len(data)
        attribute_entropy += weight * subset_entropy

    info_gain = total_entropy - attribute_entropy
    return info_gain

# Input file
input_file = "C:\\Users\\Abhi\\OneDrive\\Desktop\\DM\\Data_Mining\\DM Codes\\Assignment 4 Info Gain\\input_infodata.csv"
data = pd.read_csv(input_file)

# Target column
target_class = 'PlayTennis'

# Calculate total entropy
total_entropy = calculate_entropy(data, target_class)
print(f"Total Entropy of {target_class}: {total_entropy}")

# Attributes
attributes = data.columns.drop(target_class)
print("Attributes available for calculation:")
for attribute in attributes:
    print(attribute)

# Select attribute for information gain calculation
selected_attribute = input("Enter the attribute to calculate information gain for: ")

if selected_attribute in attributes:
    info_gain = calculate_info_gain(data, selected_attribute, target_class)
    print(f"Information Gain for {selected_attribute}: {info_gain}")
else:
    print(f"Attribute '{selected_attribute}' is not in the dataset.")

