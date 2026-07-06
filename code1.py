import pandas as pd
import os
# Create sample data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [23, 30, 28, 35, 26],
    "Salary": [50000, 65000, 72000, 80000, 60000],
    "Department": ["HR", "IT", "Finance", "IT", "Marketing"]
}

# Create DataFrame
df = pd.DataFrame(data)
data_read = "data"
os.makedirs(data_read, exist_ok=True)

file_path = os.path.join(data_read, "sample.csv")
df.to_csv(file_path, index=False)

print("CSV file saved successfully!")