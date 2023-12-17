########1stdataframe##############

import pandas as pd

# Import data from two Excel files into DataFrames
df1 = pd.read_excel('attendance_day1.xlsx')
df2 = pd.read_excel('attendance_day2.xlsx')

# Merge the two DataFrames to find students who attended both days
merged_df = pd.merge(df1, df2, on='Name', how='inner')
students_both_days = merged_df['Name'].tolist()

# Find students who attended either day
all_students = df1['Name'].append(df2['Name']).unique()

# Find the total number of records in the merged DataFrame
total_records = merged_df.shape[0]

# Merge two DataFrames row-wise
combined_df = pd.concat([df1, df2], ignore_index=True)

# Merge two DataFrames using two columns as multi-row indexes
multi_index_df = pd.merge(df1, df2, on=['Name', 'Duration'], how='outer')

# Generate descriptive statistics for the multi-index DataFrame
descriptive_stats = multi_index_df.describe()

print("Students who attended both days:", students_both_days)
print("All students who attended workshop on either of the days:", all_students)
print("Total number of records in the merged DataFrame:", total_records)
print("Descriptive statistics for the multi-index DataFrame:")
print(descriptive_stats)

###############2dataframe################
import pandas as pd

# Read data from excel files
df1 = pd.read_excel("attendance_day1.xlsx")
df2 = pd.read_excel("attendance_day2.xlsx")

# a. Find names of students who had attended the workshop on both days
merged_df = pd.merge(df1, df2, on="Name", how="inner")
print(f"Students who attended both days: {merged_df['Name'].tolist()}")

# b. Find names of all students who have attended workshop on either of the days
merged_df = pd.merge(df1, df2, on="Name", how="outer")
print(f"Students who attended on any of the days: {merged_df['Name'].tolist()}")

# c. Merge two data frames row-wise and find the total number of records
merged_df = pd.concat([df1, df2])
print(f"Total Number of Records: {len(merged_df)}")

# d. Merge two data frames and use two columns names and duration as multi-row indexes
merged_df = pd.concat([df1, df2]).set_index(["Name", "Duration"])

# Generate descriptive statistics for this multi-index
print(merged_df.describe())

