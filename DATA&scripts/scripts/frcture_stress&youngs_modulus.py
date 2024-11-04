# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 11:25:46 2024

@author: Administrator
"""

#single helix chain____fracture_stress_data&youngs_modulus_data
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd  

directories = [
    r'data/h0',
    r'data/h',
]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

fracture_data = [] 

for directory in directories:
    angles = []
    fracture_stress_values = []

    for subdir in os.listdir(directory):
        sub_dir_path = os.path.join(directory, subdir)

        if os.path.isdir(sub_dir_path):
            # read grapoten.txt file
            file_path = os.path.join(sub_dir_path, 'grapoten.txt')
            if os.path.isfile(file_path):
                with open(file_path, 'r') as f:
                    lines = f.readlines()

                max_value = float('-inf')
                max_value_strain = None

                strain_data = []  
                fracture_stress_data = []  

                for line in lines[1:]:
                    data = line.split()
                    strain = float(data[0])
                    fracture_stress = float(data[2])

                    strain_data.append(strain)
                    fracture_stress_data.append(fracture_stress)

                    if fracture_stress > max_value:
                        max_value = fracture_stress
                        max_value_strain = strain

                angles.append(subdir)  
                fracture_stress_values.append(max_value)  # Fracture Stress

        
                df = pd.DataFrame({
                    'Strain': strain_data,
                    'Fracture Stress (GPa)': fracture_stress_data
                })
                df.to_csv(os.path.join(sub_dir_path, f'{subdir}_fracture_stress_data.csv'), index=False)

    
    def sort_key(x):
        try:
            return float(x)
        except ValueError:
            return float('inf')

    angles_sorted, fracture_stress_values_sorted = zip(*sorted(zip(angles, fracture_stress_values), key=lambda x: sort_key(x[0])))

    
    fracture_data.append({
        'Angle': angles_sorted,
        'Fracture Stress (GPa)': fracture_stress_values_sorted,
        'Material': 'CNT(8)' if directory == directories[0] else '(C$_{60})$@SWCNT_Single_helix_chain(17)'
    })

    ax1.plot(angles_sorted, fracture_stress_values_sorted, 'o-', label='CNT(17)' if directory == directories[0] else '(C$_{60})$@SWCNT_Single_helix_chain(17)')


all_slopes = []
all_dir_names = []

for main_dir in directories:
    slopes = []
    dir_names = []

    for subdir in os.listdir(main_dir):
        subdir_path = os.path.join(main_dir, subdir)

        if os.path.isdir(subdir_path):
            data_path = os.path.join(subdir_path, 'grapoten.txt')
            data = np.loadtxt(data_path, skiprows=1)
            x = data[:, 0]
            y = data[:, 2]

            slope_range = np.where((x >= 0) & (x <= 0.05))
            x_slope = x[slope_range]
            y_slope = y[slope_range]
            slope, _ = np.polyfit(x_slope, y_slope, 1)

            slopes.append(slope)
            dir_names.append(subdir)

    sorted_indices = np.argsort(np.array([sort_key(x) for x in dir_names]))
    sorted_dir_names = [dir_names[i] for i in sorted_indices]
    sorted_slopes = [slopes[i] for i in sorted_indices]

    all_slopes.append(sorted_slopes)
    all_dir_names.append(sorted_dir_names)

ax2.plot(all_dir_names[0], all_slopes[0], 'o-', label='CNT(17)')
ax2.plot(all_dir_names[1], all_slopes[1], 'o-', label='(C$_{60})$@SWCNT_Single_helix_chain(17)')

ax1.text(-0.2, 1, '(a)', transform=ax1.transAxes, fontsize=14,
         verticalalignment='top', horizontalalignment='left')
ax2.text(-0.2, 1, '(b)', transform=ax2.transAxes, fontsize=14,
         verticalalignment='top', horizontalalignment='left')
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.85, wspace=0.3)

ax1.set_xticks(angles_sorted[::2])  
ax2.set_xticks(angles_sorted[::2])  
ax1.set_xlabel('L (Å)')
ax1.set_ylabel('Fracture stress (GPa)')

ax2.set_xlabel('L (Å)')
ax2.set_ylabel("Young's modulus (GPa)")

plt.subplots_adjust(wspace=0.3)
ax1.legend()
ax2.legend()

fracture_df_list = []
for data in fracture_data:
    df = pd.DataFrame({
        'Angle': data['Angle'],
        'Fracture Stress (GPa)': data['Fracture Stress (GPa)'],
    })
    fracture_df_list.append(df)

fracture_df = pd.concat(fracture_df_list, axis=1)

fracture_df_columns_1 = fracture_df.iloc[:, :2]
fracture_df_columns_2 = fracture_df.iloc[:, 2:]

fracture_df_columns_1.to_csv(r'D:data/Hfracture_stress_data_part1.csv', index=False)
fracture_df_columns_2.to_csv(r'data/Hfracture_stress_data_part2.csv', index=False)

youngs_modulus_df_list = []
for i, dir_names in enumerate(all_dir_names):
    df = pd.DataFrame({
        'Angle': dir_names,
        "Young's Modulus (GPa)": all_slopes[i],
    })
    youngs_modulus_df_list.append(df)

youngs_modulus_df = pd.concat(youngs_modulus_df_list, axis=1)

youngs_modulus_df_columns_1 = youngs_modulus_df.iloc[:, :2]
youngs_modulus_df_columns_2 = youngs_modulus_df.iloc[:, 2:]

youngs_modulus_df_columns_1.to_csv(r'data/Hyoungs_modulus_data_part1.csv', index=False)
youngs_modulus_df_columns_2.to_csv(r'data/Hyoungs_modulus_data_part2.csv', index=False)

plt.savefig(os.path.join(r'data/H.pdf'))
plt.show()