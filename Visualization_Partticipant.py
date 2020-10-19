import pandas as pd
import numpy as np
from tqdm import tqdm as tqdm
import matplotlib.pyplot as plt

# 実験結果読み込み
# In[]:
participant1_1 = pd.read_csv("participant1/analysis/rundata/dc5_amada-1_1.csv", names=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'))
#participant1_2 = pd.read_csv("participant1/analysis/rundata/dc5_amada-29_0.csv", names=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'))
#participant1_2

# In[]:
course_all1 = pd.read_csv('participant1/course/awazi_61_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all2 = pd.read_csv('participant1/course/awazi_62_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all3 = pd.read_csv('participant1/course/awazi_63_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all4 = pd.read_csv('participant1/course/awazi_64_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all5 = pd.read_csv('participant1/course/awazi_65_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all6 = pd.read_csv('participant1/course/awazi_66_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))

course_all7 = pd.read_csv('participant1/course/fuji_21_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all8 = pd.read_csv('participant1/course/fuji_22_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))

course_all9 = pd.read_csv('participant1/course/fujiazami_21_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all10 = pd.read_csv('participant1/course/fujiazami_22_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))

course_all11 = pd.read_csv('participant1/course/ise_31_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all12 = pd.read_csv('participant1/course/ise_32_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all13 = pd.read_csv('participant1/course/ise_33_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))

course_all14 = pd.read_csv('participant1/course/niigata_41_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
#course_all15 = pd.read_csv('participant1/course/niigata_42_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all16 = pd.read_csv('participant1/course/niigata_43_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all17 = pd.read_csv('participant1/course/niigata_44_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))

course_all18 = pd.read_csv('participant1/course/sagawa2_31_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all19 = pd.read_csv('participant1/course/sagawa2_32_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all20 = pd.read_csv('participant1/course/sagawa2_33_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))

course_all21 = pd.read_csv('participant1/course/shiga2_61_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all22 = pd.read_csv('participant1/course/shiga2_62_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all23 = pd.read_csv('participant1/course/shiga2_63_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all24 = pd.read_csv('participant1/course/shiga2_64_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all25 = pd.read_csv('participant1/course/shiga2_65_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all26 = pd.read_csv('participant1/course/shiga2_66_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))

course_all27 = pd.read_csv('participant1/course/yamagata1_51_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all28 = pd.read_csv('participant1/course/yamagata1_52_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all29 = pd.read_csv('participant1/course/yamagata1_53_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all30 = pd.read_csv('participant1/course/yamagata1_54_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all31 = pd.read_csv('participant1/course/yamagata1_55_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))

course_all32 = pd.read_csv('participant1/course/yamagata2_21_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
course_all33 = pd.read_csv('participant1/course/yamagata2_22_full.csv',names=('A', 'B', 'C', 'D', 'E', 'F'))
# In[]:
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.tick_params(which='both', direction='in',
                top=bool, right=bool, labelbottom=True)
#ax1.set_xlim(0.0, 10000)
ax1.set_xlabel("x Coordinate")
# ax1.set_ylim(0, 2)
ax1.set_ylabel("y Coordinate")
ax1.grid()
ax1.plot(participant1_1['C'], participant1_1['D'], "-", color='red', lw=1)
#ax1.plot(course_all['A'], course_all['B'], "-", color='black', lw=1)
#ax1.plot(course_all['C'], course_all['D'], "-", color='black', lw=1)
#ax1.plot(course_all['E'], course_all['F'], "-", color='black', lw=1)

# In[]:
course_all = course_all6
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.tick_params(which='both', direction='in',
                top=bool, right=bool, labelbottom=True)
#ax1.set_xlim(0.0, 10000)
ax1.set_xlabel("x Coordinate")
# ax1.set_ylim(0, 2)
ax1.set_ylabel("y Coordinate")
ax1.grid()
ax1.plot(course_all['A'], course_all['B'], "-", color='red', lw=1)
ax1.plot(course_all['C'], course_all['D'], "-", color='black', lw=1)
ax1.plot(course_all['E'], course_all['F'], "-", color='black', lw=1)
ax1.plot(participant1_1['C'], participant1_1['D'], "-", color='red', lw=1)


# zoomするsubplotの位置
# axes([左からどのくらい離すか, 下からどのくらい離すか, 幅, 高さ])
sub_axes = plt.axes([.2, .3, .25, .25])
sub_axes.tick_params(which='both', direction='in',
                     top=bool, right=bool, labelbottom=True)
sub_axes.tick_params(labelsize=7)
sub_axes.grid(which='major', color='gray', alpha=0.1,
              linestyle=':', linewidth=0.3)
sub_axes.set_xlim(0.0, 100)
# sub_axes.set_xticks([0, 0.2, 0.4, 0.6])
sub_axes.set_ylim(-10, 10)

# subplotを描く
sub_axes.plot(course_all['A'], course_all['B'], "-", color='red', lw=1)
sub_axes.plot(course_all['C'], course_all['D'], "-", color='black', lw=1)
sub_axes.plot(course_all['E'], course_all['F'], "-", color='black', lw=1)
sub_axes.plot(participant1_1['C'], participant1_1['D'], "-", color='blue', lw=1)


# zoomするsubplotの位置
# axes([左からどのくらい離すか, 下からどのくらい離すか, 幅, 高さ])
sub_axes2 = plt.axes([.6, .6, .25, .25])
sub_axes2.tick_params(which='both', direction='in',
                      top=bool, right=bool, labelbottom=True)
sub_axes2.tick_params(labelsize=7)
sub_axes2.grid(which='major', color='gray', alpha=0.1,
               linestyle=':', linewidth=0.3)
sub_axes2.set_xlim(8500, 8510)
#sub_axes2.set_xlim(4990, 4900)
# sub_axes.set_xticks([0, 0.2, 0.4, 0.6])
sub_axes2.set_ylim(-3990,-3980)
#sub_axes2.set_ylim(-1000, -1010)

# subplotを描く
sub_axes2.plot(course_all['A'], course_all['B'], "-", color='red', lw=1)
sub_axes2.plot(course_all['C'], course_all['D'], "-", color='black', lw=1)
sub_axes2.plot(course_all['E'], course_all['F'], "-", color='black', lw=1)
sub_axes2.plot(participant1_1['C'], participant1_1['D'], "-", color='blue', lw=1)

# In[]:
'''
終わり
'''
