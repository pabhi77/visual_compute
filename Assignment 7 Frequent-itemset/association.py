# def read_transactions_from_csv(file_path):
#     transactions = []
#     with open(file_path, 'r') as csvfile:
#         for line in csvfile:
#             transaction = line.strip().split(',')
#             transactions.append(set(transaction))
#     return transactions

# def generate_frequent_itemsets(transactions, min_support):
#     item_counts = {}
#     for transaction in transactions:
#         for item in transaction:
#             if item in item_counts:
#                 item_counts[item] += 1
#             else:
#                 item_counts[item] = 1

#     frequent_itemsets = []
#     for item, count in item_counts.items():
#         if count >= min_support:
#             frequent_itemsets.append([item])

#     length = 2
#     while True:
#         candidates = []
#         for i in range(len(frequent_itemsets) - 1):
#             for j in range(i + 1, len(frequent_itemsets)):
#                 candidate = list(set(frequent_itemsets[i]) | set(frequent_itemsets[j]))
#                 if len(candidate) == length:
#                     candidates.append(candidate)

#         if not candidates:
#             break

#         frequent_candidates = []
#         for candidate in candidates:
#             support = sum(1 for transaction in transactions if set(candidate).issubset(transaction))
#             if support >= min_support:
#                 frequent_itemsets.append(candidate)
#                 frequent_candidates.append(candidate)

#         if not frequent_candidates:
#             break

#         length += 1

#     return frequent_itemsets

# def generate_association_rules(frequent_itemsets, transactions, min_confidence):
#     association_rules = []
    
#     for itemset in frequent_itemsets:
#         if len(itemset) > 1:
#             for i in range(1, len(itemset)):
#                 antecedent = itemset[:i]
#                 consequent = itemset[i:]
                
#                 support_itemset = sum(1 for transaction in transactions if set(itemset).issubset(transaction))
#                 support_antecedent = sum(1 for transaction in transactions if set(antecedent).issubset(transaction))
                
#                 confidence = support_itemset / support_antecedent
                
#                 if confidence >= min_confidence:
#                     association_rules.append((antecedent, consequent, support_itemset, support_antecedent, confidence))
    
#     return association_rules

# if __name__ == "__main__":
#     file_path = input("Enter the path to the CSV file: ")

#     # Read transactions from CSV file
#     transactions = read_transactions_from_csv(file_path)

#     # Get minimum support and confidence from the user
#     min_support = int(input("Enter the minimum support (e.g., 2): "))
#     min_confidence = float(input("Enter the minimum confidence (e.g., 0.5): "))

#     # Generate frequent itemsets
#     frequent_itemsets = generate_frequent_itemsets(transactions, min_support)

#     # Generate association rules
#     association_rules = generate_association_rules(frequent_itemsets, transactions, min_confidence)

#     # Display the result
#     print("\nFrequent Itemsets:")
#     for itemset in frequent_itemsets:
#         print(itemset)

#     print("\nAssociation Rules:")
#     for rule in association_rules:
#         antecedent, consequent, support_itemset, support_antecedent, confidence = rule
#         print(f"{antecedent} => {consequent} | Support: {support_itemset}, Confidence: {confidence}")


def read_transactions_from_csv(file_path):
    transactions = []
    with open(file_path, 'r') as csvfile:
        for line in csvfile:
            transaction = line.strip().split(',')
            transactions.append(set(transaction))
    return transactions

def generate_frequent_itemsets(transactions, min_support):
    item_counts = {}
    for transaction in transactions:
        for item in transaction:
            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1

    frequent_itemsets = []
    for item, count in item_counts.items():
        if count >= min_support:
            frequent_itemsets.append([item])

    length = 2
    while True:
        candidates = []
        for i in range(len(frequent_itemsets) - 1):
            for j in range(i + 1, len(frequent_itemsets)):
                candidate = list(set(frequent_itemsets[i]) | set(frequent_itemsets[j]))
                if len(candidate) == length:
                    candidates.append(candidate)

        if not candidates:
            break

        frequent_candidates = []
        for candidate in candidates:
            support = sum(1 for transaction in transactions if set(candidate).issubset(transaction))
            if support >= min_support:
                frequent_itemsets.append(candidate)
                frequent_candidates.append(candidate)

        if not frequent_candidates:
            break

        length += 1

    return frequent_itemsets

def generate_association_rules(frequent_itemsets, transactions, min_confidence):
    association_rules = []
    
    for itemset in frequent_itemsets:
        if len(itemset) > 1:
            for i in range(1, len(itemset)):
                antecedent = itemset[:i]
                consequent = itemset[i:]
                
                support_itemset = sum(1 for transaction in transactions if set(itemset).issubset(transaction))
                support_antecedent = sum(1 for transaction in transactions if set(antecedent).issubset(transaction))
                
                confidence = support_itemset / support_antecedent
                
                if confidence >= min_confidence:
                    association_rules.append((antecedent, consequent, support_itemset, support_antecedent, confidence))
    
    return association_rules

if __name__ == "__main__":
    file_path = r"C:\Users\Abhi\OneDrive\Desktop\DM Codes\Assignment 7 Frequent-itemset\Itemset.csv"

    # Read transactions from CSV file
    transactions = read_transactions_from_csv(file_path)

    # Get minimum support and confidence from the user
    min_support = int(input("Enter the minimum support (e.g., 2): "))
    min_confidence = float(input("Enter the minimum confidence (e.g., 0.5): "))

    # Generate frequent itemsets
    frequent_itemsets = generate_frequent_itemsets(transactions, min_support)

    # Generate association rules
    association_rules = generate_association_rules(frequent_itemsets, transactions, min_confidence)

    # Display the result
    print("\nFrequent Itemsets:")
    for itemset in frequent_itemsets:
        print(itemset)

    print("\nAssociation Rules:")
    for rule in association_rules:
        antecedent, consequent, support_itemset, support_antecedent, confidence = rule
        print(f"{antecedent} => {consequent} | Support: {support_itemset}, Confidence: {confidence}")
