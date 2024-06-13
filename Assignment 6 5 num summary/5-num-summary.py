# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# def calculate_five_number_summary(data):
#     summary = {
#         'Min': data.min(),
#         'Q1': data.quantile(0.25),
#         'Median': data.median(),
#         'Q3': data.quantile(0.75),
#         'Max': data.max()
#     }
#     return summary

# # Read data from CSV file
# file_path = 'input.csv'  # Replace with the path to your CSV file
# df = pd.read_csv(file_path)

# # Assuming your dataset has a single column named 'data'
# data_column_name = 'data'  # Replace with the actual column name in your dataset
# data = df[data_column_name]

# # Calculate the five-number summary
# summary = calculate_five_number_summary(data)
# print("Five-Number Summary:")
# for key, value in summary.items():
#     print(f"{key}: {value}")

# # Plot box plot using seaborn
# plt.figure(figsize=(8, 6))
# sns.boxplot(x=data)
# plt.title('Box Plot')
# plt.show()

import matplotlib.pyplot as plt

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        # Skip header
        next(file)
        for line in file:
            values = line.strip().split(',')
            data.extend(map(float, values))
    return data

def calculate_five_number_summary(data):
    data_sorted = sorted(data)
    n = len(data)
    
    minimum = data_sorted[0]
    maximum = data_sorted[-1]
    
    if n % 2 == 0:
        q1_index = n // 4
        q3_index = n // 4 * 3
        q1 = (data_sorted[q1_index - 1] + data_sorted[q1_index]) / 2
        q3 = (data_sorted[q3_index - 1] + data_sorted[q3_index]) / 2
    else:
        q1_index = (n + 1) // 4
        q3_index = (n + 1) // 4 * 3
        q1 = data_sorted[q1_index - 1]
        q3 = data_sorted[q3_index - 1]
    
    median_index = n // 2
    if n % 2 == 0:
        median = (data_sorted[median_index - 1] + data_sorted[median_index]) / 2
    else:
        median = data_sorted[median_index]
    
    return minimum, q1, median, q3, maximum

def main():
    filename = "C:\\Users\\Abhi\\OneDrive\\Desktop\\DM Codes\\Assignment 6 5 num summary\\input.csv"
    data = read_csv(filename)
    min_val, q1_val, median_val, q3_val, max_val = calculate_five_number_summary(data)
    
    print("Five-Number Summary:")
    print("Minimum:", min_val)
    print("Q1:", q1_val)
    print("Median:", median_val)
    print("Q3:", q3_val)
    print("Maximum:", max_val)
    
    plt.figure(figsize=(8,6))
    plt.boxplot(data, vert=False)
    plt.title("Box Plot of Five-Number Summary")
    plt.xlabel("Values")
    plt.yticks([1], ['Data'])
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

