## NBA Stats Correlation Analysis
## Author: John Paul Talag
## Date: 3/16/25
## Description: This program analyzes correlations between NBA performance metrics using raw CSV data.
## Collaboration: I used Generative AI to help refine errors within the code.

import csv

def calculate_correlation(x, y):
    """
    Calculate the Pearson correlation coefficient between two lists.

    Parameters:
    - x (list of float): First variable
    - y (list of float): Second variable

    Returns:
    - float: Correlation coefficient between -1 and 1
    """
    if len(x) != len(y) or not x:
        return 0

    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))
    denominator_x = sum((x[i] - mean_x) ** 2 for i in range(len(x))) ** 0.5
    denominator_y = sum((y[i] - mean_y) ** 2 for i in range(len(y))) ** 0.5

    if denominator_x == 0 or denominator_y == 0:
        return 0

    return numerator / (denominator_x * denominator_y)


def extract_column_pair(data, col1, col2):
    """
    Extracts valid numeric data from two columns in the dataset.

    Parameters:
    - data (list of dict): Parsed CSV rows
    - col1 (str): First column name
    - col2 (str): Second column name

    Returns:
    - tuple: Two lists of floats representing values from col1 and col2
    """
    x_vals, y_vals = [], []
    for row in data:
        if col1 in row and col2 in row:
            try:
                x = float(row[col1])
                y = float(row[col2])
                x_vals.append(x)
                y_vals.append(y)
            except ValueError:
                continue  # Skip non-numeric or missing data
    return x_vals, y_vals


def load_csv(filepath):
    """
    Loads CSV file and returns data as a list of dictionaries.

    Parameters:
    - filepath (str): Path to the CSV file

    Returns:
    - list of dict: Each row represented as a dictionary
    """
    with open(filepath, newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def main():
    # Set file path (replace with your own path if needed)
    file_path = "/Users/junpoltalog/Downloads/NBA Stats 202324 All Stats  NBA Player Props Tool (4).csv"

    # Load the CSV data
    data = load_csv(file_path)

    # Basic check: How many players? What are the column names?
    print(f"Data loaded: {len(data)} entries")
    if data:
        print("Column Names:", list(data[0].keys()))
    else:
        print("No data found!")
        return

    # Define the stat pairs we want to analyze
    correlation_pairs = [
        ("3P%", "PPG", "3P% and PPG"),
        ("AGE", "MPG", "Age and MPG"),
        ("FTA", "FT%", "FTA and FT%")
    ]

    # Optional user input: compare any two columns
    # Uncomment below to allow user-defined comparisons
    """
    col1 = input("Enter first stat (e.g., 'AST'): ")
    col2 = input("Enter second stat (e.g., 'TO'): ")
    correlation_pairs.append((col1, col2, f"{col1} and {col2}"))
    """

    # Loop through each stat pair and calculate correlation
    for col1, col2, label in correlation_pairs:
        x, y = extract_column_pair(data, col1, col2)
        if x and y:
            corr = calculate_correlation(x, y)
            print(f"Correlation between {label}: {corr:.4f}")
        else:
            print(f"Not enough data for {label} correlation.")

    # Test your correlation function to validate accuracy
    print("\n--- Correlation Function Testing ---")
    print("Test 1 (Perfect Positive):", calculate_correlation([1, 2, 3, 4], [10, 20, 30, 40]))  # ~1.0
    print("Test 2 (Perfect Negative):", calculate_correlation([1, 2, 3, 4], [40, 30, 20, 10]))  # ~-1.0

    print("\nAnalysis complete!")


if __name__ == "__main__":
    main()