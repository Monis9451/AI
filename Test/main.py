# import pandas as pd;
# import os;
# import csv

# records = 'Recod.csv'
# with open(records, mode = 'w', newline = '') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Student ID', 'Name', 'Age', 'Major', 'Math', 'Physics', 'Chemistry'])
#     writer.writerow([601, 'Monis', 19, 'Computer Science', 88, 92, 85])
    
# print(f'{records} has been created successfully.')
# print(pd.read_csv('Recod.csv').head())

import pandas as pd

# Create a sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)

# Write DataFrame to an Excel file
df.to_excel("sample_data.xlsx", index=False)
print("Data written to sample_data.xlsx")

# Read the data back from the Excel file
df_read = pd.read_excel("sample_data.xlsx")
print("Data read from sample_data.xlsx:")
print(df_read)
