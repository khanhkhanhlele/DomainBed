import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib.lines import Line2D  # For custom legend handles

# Get the current working directory
script_path = os.path.realpath(__file__)
script_directory = os.path.dirname(script_path)

csv_file_name = "filter_data.csv"  # Replace with your actual file name
csv_file_path = os.path.join(script_directory, csv_file_name)

# Load your CSV data into a DataFrame
df = pd.read_csv(csv_file_path)
df['Step'] *= 300

# No need to multiply Step by 300 in this case



plt.figure(figsize=(10, 7))

# Plot each column (group)
for col in df.columns[1:]:
    plt.plot(df['Step'], df[col], label=col, linewidth=2)

# Create a legend with larger font size
plt.legend(title="Groups", loc='upper center', prop={'size': 12})

# Set y-axis limits from 0 to 0.3 (adjust as needed)
plt.ylim(0, 0.3)

plt.xlabel('Step')
plt.ylabel('Values')
plt.grid(True)
plt.tight_layout()
pdf_file_path = os.path.join(script_directory, "plot_F2_c.pdf")
plt.savefig(pdf_file_path, format='pdf')
