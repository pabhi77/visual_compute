# # import csv
# # from collections import defaultdict

# # # Function to calculate probabilities for each class and attribute value
# # def train(dataset):
# #     class_counts = defaultdict(int)
# #     attribute_counts = defaultdict(lambda: defaultdict(int))
# #     total_samples = 0

# #     for row in dataset:
# #         class_val = row[-1]  # last column is the class label
# #         class_counts[class_val] += 1
# #         total_samples += 1

# #         for i in range(len(row) - 1):
# #             attribute_counts[i][row[i].strip("'").strip(), class_val] += 1  
# #     return class_counts, attribute_counts, total_samples

# # # Function to predict class for a given instance
# # def predict(class_counts, attribute_counts, total_samples, instance):
# #     class_probs = defaultdict(float)

# #     for class_val, class_count in class_counts.items():
# #         prob = 1.0
# #         for i in range(len(instance)):
# #             count = attribute_counts[i][instance[i].strip("'").strip(), class_val]
# #             prob *= (count + 1) / (class_count + len(attribute_counts[i]))

# #         class_probs[class_val] = prob * class_count / total_samples

# #     prob_yes = class_probs['Yes'] / (class_probs['Yes'] + class_probs['No'])
# #     prob_no = class_probs['No'] / (class_probs['Yes'] + class_probs['No'])

# #     if(prob_yes > prob_no):
# #         pred_class = 'Yes'
# #     else:
# #         pred_class = 'No'

# #     return pred_class, prob_yes, prob_no

# # def read_csv(filename):
# #     dataset = []
# #     with open(filename, 'r') as file:
# #         csv_reader = csv.reader(file)
# #         for row in csv_reader:
# #             dataset.append(row)
# #     return dataset

# # if __name__ == "__main__":
# #     filename = 'inputbayes.csv'
# #     dataset = read_csv(filename)

# #     class_counts, attribute_counts, total_samples = train(dataset)

# #     # Take test_instance as input from the user
# #     test_instance = input("Enter the test Sample attributes (comma-separated values): ").split(',')
# #     # eg - Sunny,Cool,Normal,Strong
# #     test_instance = [value.strip().strip("'") for value in test_instance]

# #     predicted_class, prob_yes, prob_no = predict(class_counts, attribute_counts, total_samples, test_instance)
# #     print(f"Predicted class: {predicted_class}")
# #     print(f"Probability (Yes): {prob_yes:.4f}")
# #     print(f"Probability (No): {prob_no:.4f}")

# # import csv
# # from collections import defaultdict

# # # Function to calculate probabilities for each class and attribute value during training
# # def train(dataset):
# #     class_counts = defaultdict(int)
# #     attribute_counts = defaultdict(lambda: defaultdict(int))
# #     total_samples = 0

# #     for row in dataset:
# #         class_val = row[-1]  # last column is the class label
# #         class_counts[class_val] += 1
# #         total_samples += 1

# #         for i in range(len(row) - 1):
# #             attribute_counts[i][(row[i].strip("'").strip(), class_val)] += 1  

# #     return class_counts, attribute_counts, total_samples

# # # Function to predict class for a given instance
# # def predict(class_counts, attribute_counts, total_samples, instance):
# #     class_probs = defaultdict(float)

# #     for class_val, class_count in class_counts.items():
# #         prob = 1.0
# #         for i in range(len(instance)):
# #             count = attribute_counts[i][instance[i].strip("'").strip(), class_val]
# #             prob *= (count + 1) / (class_count + len(attribute_counts[i]))

# #         class_probs[class_val] = prob * class_count / total_samples

# #     prob_yes = class_probs['Yes'] / (class_probs['Yes'] + class_probs['No'])
# #     prob_no = class_probs['No'] / (class_probs['Yes'] + class_probs['No'])

# #     if(prob_yes > prob_no):
# #         pred_class = 'Yes'
# #     else:
# #         pred_class = 'No'

# #     return pred_class, prob_yes, prob_no


# # # Function to read CSV file and return dataset
# # def read_csv(filename):
# #     dataset = []
# #     with open(filename, 'r') as file:
# #         csv_reader = csv.reader(file)
# #         for row in csv_reader:
# #             dataset.append(row)
# #     return dataset

# # if __name__ == "__main__":
# #     # Path to the input CSV file
# #     filename = 'C:\\Users\\Abhi\\OneDrive\\Desktop\\DM Codes\\Assignment 13 Baye\'s classifier\\inputbayes.csv'
    
# #     # Read dataset from CSV file
# #     dataset = read_csv(filename)

# #     # Train the Naive Bayes model
# #     class_counts, attribute_counts, total_samples = train(dataset)

# #     # Take test_instance as input from the user
# #     test_instance = input("Enter the test Sample attributes (comma-separated values): ").split(',')
# #     test_instance = [value.strip() for value in test_instance]

# #     # Predict the class and probabilities
# #     predicted_class, prob_yes, prob_no = predict(class_counts, attribute_counts, total_samples, test_instance)
    
# #     # Output the results
# #     print(f"Predicted class: {predicted_class}")
# #     print(f"Probability (Yes): {prob_yes:.4f}")
# #     print(f"Probability (No): {prob_no:.4f}")

import csv
from collections import defaultdict
import numpy as np

# Function to read CSV file and process data
def read_csv(filename):
    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)
        titles = next(csv_reader)  # Read the column headings
        data = [row for row in csv_reader]
    return titles, data

# Function to calculate probabilities for Bayesian classification
def calculate_probabilities(titles, data):
    parent = defaultdict(float)
    child = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
    count = 0

    for row in data:
        parent[row[-1]] += 1
        for i in range(1, len(row) - 1):
            child[titles[i]][row[i]][row[-1]] += 1
        count += 1

    result_classes = list(parent.keys())
    output = np.ones(len(result_classes))

    for title in titles[1:-1]:
        while True:
            condition = input(f"Enter {title} condition: ").strip()
            if condition in child[title]:
                break
            print("No match. Please enter a valid condition.")
        
        for i, result_class in enumerate(result_classes):
            val = child[title][condition][result_class] / parent[result_class]
            output[i] *= val

    for i, result_class in enumerate(result_classes):
        output[i] *= parent[result_class] / count

    total_sum = sum(output)
    return result_classes, output, total_sum

# Function to display results
def display_results(result_classes, output, total_sum):
    print(f"Sum of probabilities: {total_sum}")
    print("Output probabilities:")
    for i, result_class in enumerate(result_classes):
        print(f"{result_class}: {output[i]}")
        print(f"Percentage: {(output[i] / total_sum) * 100:.2f}%")

def main():
    filepath = "C:\\Users\\Abhi\\OneDrive\\Desktop\\DM Codes\\Assignment 13 Baye\'s classifier\\inputbayes.csv"
    titles, data = read_csv(filepath)
    result_classes, output, total_sum = calculate_probabilities(titles, data)
    display_results(result_classes, output, total_sum)

if __name__ == "__main__":
    main()




