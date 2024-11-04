import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams.update({'font.size': 18})

base_path=r"."
directories = [
    os.path.join(base_path,"L"),
    os.path.join(base_path,"Z"),
    os.path.join(base_path,"H"),
]

file_name = 'merged_C60Cnt_Min_Xdata.txt'

plt.figure(figsize=(10, 6))

colors = ['r', 'g', 'b']
labels = ['CNT(10)/C$_{60}$-L', 'CNT(14)/C$_{60}$-Z', 'CNT(17)/C$_{60}$-H']

for directory, color, label in zip(directories, colors, labels):
  
    fracture_positions_file = os.path.join(directory, file_name)

    fracture_positions_df = pd.read_csv(fracture_positions_file, sep='\s+', header=None)
    x_values = fracture_positions_df.iloc[:, 0]
    y_values = fracture_positions_df.iloc[:, 1]

    diff_values = x_values - y_values

    # Compute a histogram of the differences and calculate the frequency
    counts, bin_edges = np.histogram(diff_values, bins=10)

    # Calculate the median of each interval and the median frequency
    bin_centers = []
    freq_medians = []

    for i in range(len(bin_edges) - 1):
        bin_data = diff_values[(diff_values >= bin_edges[i]) & (diff_values < bin_edges[i + 1])]
        if len(bin_data) > 0:
        
            freq_median = counts[i] if counts[i] > 0 else 0  
            freq_medians.append(freq_median)

            bin_center = (bin_edges[i] + bin_edges[i + 1]) / 2
            bin_centers.append(bin_center)

    
    plt.scatter(bin_centers, freq_medians, color=color, s=100, label=label)
    plt.plot(bin_centers, freq_medians, color=color, linestyle='-', linewidth=2)

plt.xlabel('ΔN', fontsize=20)
plt.ylabel('Frequency', fontsize=20)
ax = plt.gca()
ax.tick_params(axis='both', which='major', labelsize=16)  
for spine in ax.spines.values():
    spine.set_linewidth(1.5)  
plt.xlim(-5,5)
plt.xticks(np.arange(-5, 6, 1))

plt.legend()

save_path = os.path.join(base_path,"Histogram.pdf")
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path, bbox_inches="tight", dpi=600)

plt.show()

# Print the median frequency for each interval
# for label, freq_medians in zip(labels, freq_medians_list):
#     print(f"{label} Frequency medians:", freq_medians)