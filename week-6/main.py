# extract information with age greater than 25 from the following list of dictionaries
data = [
    {"name": "Alice", "age": 28},
    {"name": "Bob", "age": 24},
    {"name": "Charlie", "age": 30},
]
extracted_date = [item for item in data if item["age"] > 25]
print(extracted_date)

# extract information with age less than 25 from the following list of dictionaries
data = [
    {"first_name": "Alice", "last_name": "Yoobee", "age": 28},
    {"first_name": "Bob", "last_name": "Yoobee", "age": 24},
    {"first_name": "Charlie", "last_name": "Yoobee", "age": 30},
]
extracted_date = [item for item in data if item["age"] < 25]
print(extracted_date)

# use list comprehension to flatten the matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_matrix = [i for row in matrix for i in row]
print(flattened_matrix)

# use list comprehension to flatten the matrix and print first column only
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
column_matrix = [num for row in matrix for num in row]
for i in range(0, len(column_matrix), 3):
    print(column_matrix[i])
# print(column_matrix)
