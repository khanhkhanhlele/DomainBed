import pandas as pd
import matplotlib.pyplot as plt
import os

# Get the current working directory
script_path =os.path.realpath(__file__)
script_directory = os.path.dirname(script_path)

csv_file_name = "data.csv"  # Replace with your actual file name
csv_file_path = os.path.join(script_directory, csv_file_name)

# Load your CSV data into a DataFrame
df = pd.read_csv(csv_file_path)


# Now that we have the data, let's proceed with the steps as requested by the user.

# 1. Remove columns that have "_MIN" or "_MAX" in their names
columns_to_keep = [column for column in df.columns if not ('_MIN' in column or '_MAX' in column)]
df_filtered = df[columns_to_keep]

# 2. Filter rows where the 'Step' is less than or equal to 70
df_filtered = df_filtered[df_filtered['Step'] <= 70]
df_filtered_path = os.path.join(script_directory, "filter_data.csv")
df_filtered.to_csv(df_filtered_path, index=False)