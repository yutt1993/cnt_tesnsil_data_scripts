# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:07:27 2024

@author: Administrator
"""

#fracture_stress_curve
import os
import pandas as pd
import matplotlib.pyplot as plt

# 定义目录路径
directory = r'../1.7_data'

# 初始化绘图
fig, ax = plt.subplots()

# 创建一个空列表来保存标签
labels = []

# 定义标签对应的映射
label_mapping = {
    'Lfracture_stress_data_part1.csv': 'Cnt(8)',
    'Lfracture_stress_data_part2.csv': 'Cnt/(C$_{60})$-L',
    'Zfracture_stress_data_part1.csv': 'Cnt(12)',
    'Zfracture_stress_data_part2.csv': 'Cnt/(C$_{60})$-Z',
    'Hfracture_stress_data_part1.csv': 'Cnt(15)',
    'Hfracture_stress_data_part2.csv': 'Cnt/(C$_{60})$-H',
}

# 定义颜色列表
color_L = 'lightskyblue'    # part1 曲线颜色
color_z = 'darkorange'  # part2 曲线颜色
color_h = 'lightcoral'  # part2 曲线颜色

# 遍历目录中的所有文件
for filename in os.listdir(directory):
    if 'fracture_stress_data_part' in filename and filename in label_mapping:
        # 构建文件的完整路径
        file_path = os.path.join(directory, filename)

        # 读取CSV文件，跳过第一行
        df = pd.read_csv(file_path, header=None, skiprows=0)

        # 提取第一列作为x轴数据
        x = df.iloc[:, 0]

        # 提取第二列作为y轴数据
        y = df.iloc[:, 1]

        # 判断文件名以确定线型和颜色
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

        # 绘制数据
        ax.plot(x, y, linestyle=line_style, marker='o', color=color, label=label_mapping[filename]) 
ax.tick_params(axis='both', which='major', labelsize=16)
# 设置所有边框的宽度
for spine in ax.spines.values():
    spine.set_linewidth(1.5)  # 设置边框宽度为2

# 添加图例
ax.legend(fontsize=20, loc='upper left', bbox_to_anchor=(1, 1))
# ax.legend(handles=handles, fontsize=24, loc='upper left', bbox_to_anchor=(0.1, 0.9), frameon=False)

# 设置标题和轴标签
ax.set_xlabel('L (Å)', fontsize=20)
ax.set_ylabel('Fracture Stress (GPa)', fontsize=20)
plt.xlim(0, 20)
# 将图形保存为PDF，使用bbox_inches='tight'以确保图例被包含
plt.savefig(os.path.join(r'../1.7_data/Fracture Stress.pdf'), bbox_inches='tight')

# 显示图形
plt.show()