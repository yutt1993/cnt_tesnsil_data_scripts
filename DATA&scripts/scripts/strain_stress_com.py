# - * -code: UTF -8 - * -
"" ""
Founded at 10:01:22 2024 on Wednesday, October 30th

@author: administrator
"" ""

Import operating system
Import matplotlib.pyplot as PLT

DEF PLOT_GRAPH_FROM_DIRECTORY (Directory_path, Label, COLOR = None, LINE_STYLE = None):
file_name = "grapoten.txt"
Change = []
Stress = []

For Root, DIRS, files in Os.Walk (Directory_path):
If the file_name in the file:
file_path = os.path.join (root, file_name)
try:
Use Open (File_path, 'R', Encoding = 'UTF-8') as a file:
lines = file.readlines ()
For the line [1:]: # 对于 对于
line = line.strip ()
If it is not a line: # Jump to the empty line
continue
data = line.split ()
If Len (data)> = 3: # to ensure that there is enough column
try:
strain_value = float (data [0])
stress_value = float (data [2])
strain.Application (response_Value)
Stress_Value)
Except for Valueerror:
Print (F "data conversion failed: {line.strip ()}")
Other:
Print (F "data format is incorrect: {line.strip ()}")
Except for IOERROR for E:
Print (F "cannot open the file {file_path}: {e}")

Stocking = [a (i, 0.5) I in the strain] # Treatment the resolution

If you respond and stress:
PLT.plot

# Definition color
Color_L = 'Lightskyblue'
color_z = 'darkorange'
color_h = 'turquoise'

# And label settings
Directory = [
(R "data/l0/19", 'cNT (10)', color_l, ' -'),
(R "Data/L/19", 'CNT (10)/(C $ _ {60}) $ -l', color_l, ' -'),
(R "Data/Z0/19", 'CNT (14)', color_z, ' -'),
(R "Data/Z/19", 'CNT (14)/(C $ _ {60}) $ -z', color_z, ' -'),
(R "data/h0/19", 'cNT (17)', color_h, ' -'),
(R "Data/H/19", 'CNT (17)/(C $ _ {60}) $ -h', color_h, ' -'),
This is given

# Create graphics and coordinate shaft objects
PLT.FIGURE (Figs = (10, 6))
AX = PLT.GCA () # Get the current coordinate axis

# Set the border width
Spinal spine in AX.SPINES.VALUES ():
spine.set_lineWidth (1.5)

# Draw the data of each directory
For the directory, label, color, line_style in the directory: in the directory:
plot_graph_from_directory (directory, label, color, line_style)

# Add legends and tags
PLT.Legend (fontsize = 16)
PLT.XLabel ("strain", fontsize = 20)
PLT.YLabel ("pressure (GPA)", fontsize = 20)
PLT.TICK_PARAMS (axis = 'two', = 'major', labelsize = 20)
PLT.XLIM (0, 0.5)
PLT.ylim (0, 180)

# Save the chart
PLT.Savefig
PLT.SHOW ()