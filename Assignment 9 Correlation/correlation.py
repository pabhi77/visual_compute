# def mean(values):
#     return sum(values) / len(values)

# def covariance(x, y, mean_x, mean_y):
#     covar = 0.0
#     for i in range(len(x)):
#         covar += (x[i] - mean_x) * (y[i] - mean_y)
#     return covar / (len(x) - 1)

# def correlation_coefficient(x, y):
#     mean_x, mean_y = mean(x), mean(y)
#     covar = covariance(x, y, mean_x, mean_y)

#     std_dev_x = sum((xi - mean_x) ** 2 for xi in x) ** 0.5
#     std_dev_y = sum((yi - mean_y) ** 2 for yi in y) ** 0.5

#     correlation = covar / (std_dev_x * std_dev_y)
#     return correlation

# # Example usage:
# if __name__ == "__main__":
#     # Replace these with your actual data for attributes x and y
#     attribute_x = [1, 2, 3, 4, 5]
#     attribute_y = [2, 3, 4, 5, 6]

#     correlation = correlation_coefficient(attribute_x, attribute_y)
#     print(f"Correlation coefficient: {correlation:.4f}")
import csv
import math

def read_data_from_csv(file_path):
    x_values = []
    y_values = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header
        for row in reader:
            x_values.append(float(row[0]))
            y_values.append(float(row[1]))
    return x_values, y_values

def calculate_correlation_coefficient(x_values, y_values):
    n = len(x_values)
    mean_x = sum(x_values) / n
    mean_y = sum(y_values) / n

    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_values, y_values))
    denominator = math.sqrt(sum((x - mean_x) ** 2 for x in x_values) * sum((y - mean_y) ** 2 for y in y_values))

    correlation_coefficient = numerator / denominator
    return correlation_coefficient

if __name__ == "__main__":
    file_path = r"C:\Users\Abhi\OneDrive\Desktop\DM Codes\Assignment 9 Correlation\dataset.csv"
    x_values, y_values = read_data_from_csv(file_path)
    correlation_coefficient = calculate_correlation_coefficient(x_values, y_values)
    print("Correlation Coefficient (r):", correlation_coefficient)

# Temperature,Humidity
# 22.5,35.0
# 25.0,15.0
# 28.3,4.0
# 30.1,15.0
# 26.5,75.0
# 23.7,20.0
# 29.8,10.0
# 27.4,90.0
# 24.6,100.0
# 31.2,10.0