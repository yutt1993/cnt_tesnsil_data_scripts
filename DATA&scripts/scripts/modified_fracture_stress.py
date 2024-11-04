# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:48:12 2024

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:07:27 2024

@author: Administrator
"""

#fracture_stress_curve
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

directory = r'1.7_data'#C60-CNT d=1.7
#directory = r'data'#C60-CNT d=3.4
fig, ax = plt.subplots()

labels = []

label_mapping = {
'modified_Lfracture_stress_data_part1.csv': 'Cnt(8)',
'modified_Lfracture_stress_data_part2.csv': 'Cnt(8)/(C$_{60})$-L',
'modified_Zfracture_stress_data_part1.csv': 'Cnt(12)',
'modified_Zfracture_stress_data_part2.csv': 'Cnt(12)/(C$_{60})$-Z',
'modified_Hfracture_stress_data_part1.csv': 'Cnt(15)',
'modified_Hfracture_stress_data_part2.csv': 'Cnt(15)/(C$_{60})$-H',
} #============================================================================
# label_mapping = {
#     'modified_Lfracture_stress_data_part1.csv': 'Cnt(10)',
#     'modified_Lfracture_stress_data_part2.csv': 'Cnt(10)/(C$_{60})$-L',
#     'modified_Zfracture_stress_data_part1.csv': 'Cnt(14)',
#     'modified_Zfracture_stress_data_part2.csv': 'Cnt(14)/(C$_{60})$-Z',
#     'modified_Hfracture_stress_data_part1.csv': 'Cnt(17)',
#     'modified_Hfracture_stress_data_part2.csv': 'Cnt(17)/(C$_{60})$-H',
# }
#
# =============================================================================

color_L = 'lightskyblue'     
color_z = 'darkorange'  
color_h = 'lightcoral'  

for filename in os.listdir(directory):
if 'fracture_stress_data_part' in filename and filename in label_mapping:

file_path = os.path.join(directory, filename)

df = pd.read_csv(file_path, header=None, skiprows=0)

x = df.iloc[:, 0]

y = df.iloc[:, 1]
# =============================================================================
#         print(f"x: {x}")
#         print(f"y: {y}")
# =============================================================================

if 'L' in filename:
color = color_L
if 'part1' in filename:
line_style = '-'
if 'part2' in filename:
line_style = '--'
if 'Z' in filename:
#             line_style = '--'
color = color_z
if 'H' in filename:
#             line_style = '--'
color = color_h

ax.plot(x, y, linestyle=line_style, marker='o', color=color, label=label_mapping[filename])
ax.tick_params(axis='both', which='major', labelsize=16)

for spine in ax.spines.values():
spine.set_linewidth(1.5)  

ax.legend(fontsize=20, loc='upper left', bbox_to_anchor=(1, 1))
# ax.legend(handles=handles, fontsize=24, loc='upper left', bbox_to_anchor=(0.1, 0.9), frameon=False)

ax.set_xlabel('L (Å)', fontsize=20)
ax.set_ylabel('Fracture Stress (GPa)', fontsize=20)
plt.xlim(20, 940)
plt.ylim(100,180)
x_ticks = np.linspace(40, 940, 6)  
ax.set_xticks(x_ticks)

plt.savefig(os.path.join(r'1.7_data/mo_Fracture Stress.pdf'), bbox_inches='tight')
#plt.savefig(os.path.join(r'data/mo_Fracture Stress.pdf'), bbox_inches='tight')

plt.show()