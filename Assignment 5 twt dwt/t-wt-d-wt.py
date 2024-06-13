# import csv

# classrowcolMap = {}
# colMap = {}
# rowMap = {}

# with open("C:\\Users\\Abhi\\OneDrive\\Desktop\\DM Codes\\Assignment 3 Binning\\input_data.csv", mode="r") as file:
#     reader = csv.reader(file)
#     i = 0
#     for row in reader:
#         if i == 0:
#             i += 1
#             continue
#         row_name, col_name, count = row
#         val = int(count)
#         if row_name not in classrowcolMap:
#             classrowcolMap[row_name] = {}
#         classrowcolMap[row_name][col_name] = val
#         colMap[col_name] = colMap.get(col_name, 0) + val
#         rowMap[row_name] = rowMap.get(row_name, 0) + val

# for r in rowMap:
#     for c in colMap:
#         print(f"{r}-{c}: {classrowcolMap[r][c]}")

# for r in rowMap:
#     print(f"{r} -> {rowMap[r]}")

# for c in colMap:
#     print(f"{c} -> {colMap[c]}")

# colSum = sum(colMap.values())
# rowSum = sum(rowMap.values())
# print(f"colSum: {colSum}")
# print(f"rowSum: {rowSum}")

# with open("output.csv", mode="w", newline='') as fw:
#     writer = csv.writer(fw)
#     writer.writerow(["Column\\row", "", "State 1", "", "", "State 2", "", "", "Total", "", ""])
#     writer.writerow(["", "Count", "t-weight", "d-weight", "Count", "t-weight", "d-weight", "Count", "t-weight", "d-weight"])

#     for r in rowMap:
#         row = r
#         row_data = [row]
#         for c in colMap:
#             col = c
#             row_data.extend([
#                 classrowcolMap[row][col],
#                 (classrowcolMap[row][col] / rowMap[row]) * 100,
#                 (classrowcolMap[row][col] / colMap[col]) * 100
#             ])
#         row_data.extend([rowMap[row], (rowMap[row] / rowMap[row]) * 100, (rowMap[row] / colSum) * 100])
#         writer.writerow(row_data)

#     total_row = ["Total"]
#     for c in colMap:
#         col = c
#         total_row.extend([colMap[col], (colMap[col] / colSum) * 100, (colMap[col] / colMap[col]) * 100])
#     total_row.extend([colSum, 100, 100])
#     writer.writerow(total_row)
import csv

# A class to represent a cell's data in the CSV file
class CellData:
    def __init__(self):
        self.count = 0

# Function to read data from the input CSV file into the provided data structures
def read_data(filename):
    cell_data = {}
    column_total = {}
    row_total = {}

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header line

        for row in csv_reader:
            row_name, col_name, count_str = row
            count = int(count_str)

            # Update cell data
            if row_name not in cell_data:
                cell_data[row_name] = {}
            if col_name not in cell_data[row_name]:
                cell_data[row_name][col_name] = CellData()
            cell_data[row_name][col_name].count += count

            # Update column total
            if col_name not in column_total:
                column_total[col_name] = 0
            column_total[col_name] += count

            # Update row total
            if row_name not in row_total:
                row_total[row_name] = 0
            row_total[row_name] += count

    return cell_data, column_total, row_total

# Function to calculate t-weight
def calculate_t_weight(cell_data, row_total):
    t_weights = {}
    for row_name, row_total_count in row_total.items():
        t_weights[row_name] = {}
        for col_name, cell in cell_data[row_name].items():
            t_weights[row_name][col_name] = cell.count / row_total_count
    return t_weights

# Function to calculate d-weight
def calculate_d_weight(cell_data, column_total):
    d_weights = {}
    for row_name, row_data in cell_data.items():
        for col_name, cell in row_data.items():
            if col_name not in d_weights:
                d_weights[col_name] = {}
            d_weights[col_name][row_name] = cell.count / column_total[col_name]
    return d_weights

def main():
    input_file = "C:\\Users\\Abhi\\OneDrive\\Desktop\\DM Codes\\Assignment 5 twt dwt\\input.csv"
    cell_data, column_total, row_total = read_data(input_file)
    t_weights = calculate_t_weight(cell_data, row_total)
    d_weights = calculate_d_weight(cell_data, column_total)
    
    print("T-Weights:")
    for row_name, row_data in t_weights.items():
        for col_name, weight in row_data.items():
            print(f"({row_name}, {col_name}): {weight:.4f}")

    print("\nD-Weights:")
    for col_name, col_data in d_weights.items():
        for row_name, weight in col_data.items():
            print(f"({row_name}, {col_name}): {weight:.4f}")

if __name__ == "__main__":
    main()
