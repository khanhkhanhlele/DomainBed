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
# Define groups based on the new mapping
groups = {
    "1713167172": "Fish_0.01",
    "1713142592": "Fish_0.05",
    "1712899414": "Fish_0.1",
    "1712218117": "Fish_0.5",
    "1712834220": "Fish_1",
    "1712459346": "ERM"
}

# Generating a colormap that automatically assigns a color to each group
color_map = plt.cm.get_cmap('tab20', len(groups))  # Use a colormap with enough colors
colors = {group: color_map(i) for i, group in enumerate(groups.values())}

plt.figure(figsize=(10, 7))

# Iterate through columns and plot
for column in df.columns[1:]:
    if 'grad_progress' in column:
        group_id = column.split('__')[1].split(' ')[0]
        group_name = groups.get(group_id, "Other")  # Map the identifier to group name
        angle_type = 'diff_' + column.split('_')[-1]  # Extract angle type from column name
        linewidth = 2.5 if 'ERM' in group_name else 1.5  # Bolder lines for ERM
        plt.plot(df['Step'], df[column], label=f'{group_name} {angle_type}', color=colors[group_name], linewidth=linewidth)

# Creating a custom legend for groups
group_legend = [Line2D([0], [0], color=color_map(i), lw=4, label=group)
                for i, group in enumerate(groups.values())]


# Adding legends inside the plot
first_legend = plt.legend(handles=group_legend, title="Groups", loc='upper center', prop={'size': 12})  # Adjust 'loc' as needed
plt.gca().add_artist(first_legend)

# Set y-axis limits from 0 to 0.3
# plt.ylim(0, 0.3)  # Adjust range as needed

# plt.title('Value by Step')
plt.xlabel('Step')
plt.ylabel('Values')
plt.grid(True)
plt.tight_layout()  # Adjust layout to fit legend
pdf_file_path = os.path.join(script_directory, "plot_F3_a.pdf")
plt.savefig(pdf_file_path, format='pdf')
