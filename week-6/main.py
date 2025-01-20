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
