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
    "1713009813": "Fishr_10000",
    "1712929329": "Fishr_5000",
    "1713252755": "Fishr_2500",
    "1712749138": "Fishr_1000",
    "1712459346": "ERM"
}

# Generating a colormap that automatically assigns a color to each group
color_map = plt.cm.get_cmap('tab20', len(groups))  # Use a colormap with enough colors
colors = {group: color_map(i) for i, group in enumerate(groups.values())}

# Define line styles for angles
line_styles = {
    'diff_1': ('-', 'Solid'),
    'diff_2': ('--', 'Dashed'),
}

plt.figure(figsize=(10, 7))

# Iterate through columns and plot
for column in df.columns[1:]:
    group_id = column.split('__')[1].split(' ')[0]
    group_name = groups.get(group_id, "Other")  # Map the identifier to group name
    angle_type = 'diff_' + column.split('_')[-1]  # Extract angle type from column name
    line_style = line_styles[angle_type][0]  # Get line style type
    linewidth = 2.5 if 'ERM' in group_name else 1.5  # Bolder lines for ERM
    plt.plot(df['Step'], df[column], label=f'{group_name} {angle_type}', color=colors[group_name], linestyle=line_style, linewidth=linewidth)

# Creating a custom legend for groups
group_legend = [Line2D([0], [0], color=color_map(i), lw=4, label=group)
                for i, group in enumerate(groups.values())]
angle_legend = [Line2D([0], [0], color='black', lw=4, linestyle=line_styles[angle][0], label=f'{angle.split("_")[1].capitalize()} - {line_styles[angle][1]}')
                for angle in line_styles]

# Adding legends inside the plot
first_legend = plt.legend(handles=group_legend, title="Groups", loc='upper center', prop={'size': 12})  # Adjust 'loc' as needed
plt.gca().add_artist(first_legend)
plt.legend(handles=angle_legend, title="Diff and Line Styles", loc='upper right', prop={'size': 12})  # Adjust 'loc' as needed

# Set y-axis limits from 0 to 0.3
plt.ylim(0, 0.3)  # Adjust range as needed

# plt.title('Value by Step')
plt.xlabel('Step')
plt.ylabel('Values')
plt.grid(True)
plt.tight_layout()  # Adjust layout to fit legend
pdf_file_path = os.path.join(script_directory, "plot_F2_b.pdf")
plt.savefig(pdf_file_path, format='pdf')