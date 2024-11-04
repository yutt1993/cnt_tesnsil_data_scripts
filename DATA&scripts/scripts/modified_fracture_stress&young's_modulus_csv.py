#-*-coding: UTF-8-*-
"" "
Created on Mon Nov 4 14:44:37 2024

@Author: administrator
"" "

Import OS
Import Pandas as PD

# Set the folder path
directory = r'data '

# File list
files = [[
'LFRACTURE_STRESS_DATA_PART1.CSV',
'LFRACTURE_STRESS_DATA_PART2.CSV',
'Lyoungs_modulus_data_part1.csv',
'Lyoungs_modulus_data_part2.csv',
'ZFRACTURE_STRESS_DATA_PART1.CSV',
'ZFRACTURE_STRESS_DATA_PART2.CSV',
'Zyoungs_modulus_data_part1.csv',
'Zyoungs_modulus_data_part2.csv',
'Hfracture_stress_data_part1.csv',
'Hfracture_stress_data_part2.csv',
'Hyoungs_modulus_data_part1.csv',
'Hyoungs_modulus_data_part2.csv',
]
# Define the corresponding multiple
multipliers = [41.22,41.22,41.22,41.22,48.50, 48.50, 48.50, 48.50, 43.65,43.65,43.65]
#Multipliers = [41.22,41.22,41.22,41.22,48.50,48.50, 48.50, 48.50, 41.2222,41.22,41.22]
# And processing
For File, Multiplier in Zip (Files, Multipliers):
file_path = os.path.join (Directory, File)

# Read the CSV file and ignore the first line
df = pd.read_csv (file_path, Skiprows = 1, Header = None)

#Arbridge to the corresponding multiple
df [0] = df [0] * Multiplier

# Save the modified data to the new file
new_file_path = OS.Path.join (Directory, F "Modified_ {File}")
df.to_csv (new_file_path, index = false, header = false)

Print (F "Processed {File} and saved as {new_file_path}")