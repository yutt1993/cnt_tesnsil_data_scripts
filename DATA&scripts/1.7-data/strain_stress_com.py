# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:01:22 2024

@author: Administrator
"""

import os
import matplotlib.pyplot as plt

def plot_graph_from_directory(directory_path, label, color=None, line_style=None):
    file_name = "grapoten.txt"
    strain = []
    stress = []

    for root, dirs, files in os.walk(directory_path):
        if file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    for line in lines[1:]:  # 跳过标题行
                        line = line.strip()
                        if not line:  # 跳过空行
                            continue  
                        data = line.split()
                        if len(data) >= 3:  # 确保有足够的列
                            try:
                                strain_value = float(data[0])
                                stress_value = float(data[2])
                                strain.append(strain_value)
                                stress.append(stress_value)
                            except ValueError:
                                print(f"数据转换失败: {line.strip()}")
                        else:
                            print(f"数据格式不正确: {line.strip()}")
            except IOError as e:
                print(f"无法打开文件 {file_path}: {e}")

    strain = [min(i, 0.5) for i in strain]  # 处理应变值

    if strain and stress:
        plt.plot(strain, stress, label=label, color=color, linestyle=line_style, linewidth=2.0)

# 定义颜色
color_L = 'lightskyblue'
color_z = 'darkorange'
color_h = 'turquoise'
base_path=r"../1.7_data"
# 目录和标签设置
directories = [
    (os.path.join(base_path,"l0/19"), 'CNT(8)', color_L, '--'),
    (os.path.join(base_path,"l/19"), 'CNT(8)/(C$_{60})$-L', color_L, '-'),
    (os.path.join(base_path,"z0/19"), 'CNT(12)', color_z, '--'),
    (os.path.join(base_path,"z/19"), 'CNT(12)/(C$_{60})$-Z', color_z, '-'),
    (os.path.join(base_path,"h0/19"), 'CNT(15)', color_h, '--'),
    (os.path.join(base_path,"h/19"), 'CNT(15)/(C$_{60})$-H', color_h, '-'),
]

# 创建图形和坐标轴对象
plt.figure(figsize=(10, 6))
ax = plt.gca()  # 获取当前坐标轴

# 设置边框宽度
for spine in ax.spines.values():
    spine.set_linewidth(1.5)

# 绘制每个目录的数据
for directory, label, color, line_style in directories:
    plot_graph_from_directory(directory, label, color, line_style)

# 添加图例和标签
plt.legend(fontsize=16)
plt.xlabel('Strain', fontsize=20)
plt.ylabel('Stress (GPa)', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.xlim(0, 0.5)
plt.ylim(0, 160)

# 保存图表
plt.savefig(os.path.join(base_path,"com_cntStress_strain.pdf"),bbox_inches='tight')
plt.show()