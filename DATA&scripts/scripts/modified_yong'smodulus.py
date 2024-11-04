#-*-coding: UTF-8-*-
"" "
Created on Mon Nov 4 15:03:14 2024

@Author: administrator
"" "

#-*-coding: UTF-8-*-
"" "
Create on this Oct 31 10:51:10 2024

@Author: administrator
"" "

#Youngs_modulus
Import OS
import numpy as np
Import Pandas as PD
Import Matplotlib.pyplot as PLT

# Define the directory path
Directory = R'1.7_Data '#C60-CNT D = 1.7
#Directory = R'data '#C60-CNT D = 3.4

# Initialization drawing
fig, ax = PLT.Subplots ()

labels = []

# Define the mapping corresponding to the label
label_mapping = {
'Modify_lyoungs_modulus_data_part1.csv': 'cNT (8)',
'MODIFIED_LYOUNGS_MODULUS_DATA_PART2.CSV': 'CNT (8)/(C $ _ {60}) $-l',
'Modified_zyoungs_modulus_data_part1.csv': 'cNT (12)',
'Modify_zyoungs_modulus_data_part2.csv': 'cNT (12)/(C $ _ {60}) $-z',
'Modify_hyoungs_modulus_data_part1.csv': 'cNT (15)',
'MODIFIED_HYOUNGS_MODULUS_DATA_PART2.CSV': 'CNT (15)/(C $ _ {60}) $-h',
}
# ====================================================================
# label_mapping = {
# 'MODIFIED_LYOUNGS_MODULUS_DATA_PART1.CSV': 'CNT (10)',
# 'MODIFIED_LYOUNGS_MODULUS_DATA_PART2.CSV': 'CNT (10)/(C $ _ {60}) $-L',
# 'MODIFIED_ZYOUNGS_MODULUS_DATA_PART1.CSV': 'CNT (14)',
# 'MODIFIED_ZYOUNGS_MODULUS_DATA_PART2.CSV': 'CNT (14)/(C $ _ {60}) $-z',
# 'MODIFIED_HYOUNGS_MODULUS_DATA_PART1.CSV': 'CNT (17)',
# 'MODIFIED_HYOUNGS_MODULUS_DATA_PART2.CSV': 'CNT (17)/(C $ _ {60}) $-h',
#}
# #
# ====================================================================
# Define color list
color_l = 'lightskyblue' # part1 curve color
color_z = 'darkorange' # part2 curve color
color_h = 'Lightcoral' # PART2 curve color

# All files in the catalog
For Filename in Os.listdir (Directory):
if 'youngs_modulus_data_part' in filename and filename in label_mapping:
# The complete path of the file
file_path = os.path.join (Directory, Filename)

# Read the CSV file, skip the first line
df = pd.read_csv (file_path, header = none, skiProws = 1)

# Extract the first column as the X -axis data
x = df.iloc [:, 0]

# Extract the second column as the Y -axis data
y = df.iloc [:, 1]

# Judging the file name to determine the line type and color
if 'l' in filename:
color = color_L
if 'part1' in filename:
line_style = '-'
if 'part2' in filename:
line_style = '-'
if 'z' in filename:
# line_style = '-'
color = color_z
if 'h' in filename:
# line_style = '-'
color = color_h

# Draw data
ax.plot (x, y, linedyle = line_style, marker = 'o', color = color, label = label_mapping [filename])
ax.tick_params (axis = 'both', white = 'major', labelsize = 16)
# Set the width of all borders
for spine in ax.spines.values ​​():
Spine.set_lineWidth (1.5) # Set the width of the border to 2
#
ax.legend (fontsize = 20, loc = 'upper left', bbox_to_anchor = (1, 1))

# Set title and axis tag
ax.set_xlabel ('l (å)', fontsize = 20)
ax.set_ylabel ("Yang's Modulus (GPA)", fontsize = 20)
PLT.XLIM (40, 940)
PLT.ylim (350,550)
x_ticks = np.linspace (40, 940, 6) # generate 6 points
ax.set_xticks (x_ticks)
# Save the graphic as PDF and use bbox_inches = 'tight' to ensure that the legend is included
PLT.SAVEFIG (OS.Path.Join (R "1.7_data/Mo_yang's Modulus.pdf"), bbox_inches = 'TIGHT')
#PLT.SAVEFIG (OS.Path.Join (R "Data/Mo_yang's Modulus.pdf"), bbox_inches = 'tight')))))

plt.show ()