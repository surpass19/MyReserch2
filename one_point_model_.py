import pandas as pd
import numpy as np
from tqdm import tqdm as tqdm
import matplotlib.pyplot as plt
import math
import os


# course.scv読み込み
course_all = pd.read_csv("awazi_61_full.csv", names=('A', 'B', 'C', 'D', 'E', 'F'))

course_all.tail(10)
course_all.info()

# コースのx座標, y座標(Series型)
course_x = course_all['A']
course_y = course_all['B']

# In[]:
def One_Point_Model(course_x, course_y, near_point_m=8, Kp=1, dt=0.1, v=12.5):

    #ダミーのnearpointを自分で指定
    near_point_2 = 2
    near_point_3 = 5
    near_point_4 = 10
    near_point_5 = 20

    # 取得データの初期化
    near_point_rad_np = [0]
    near_point_rad2_np = [0]
    near_point_rad3_np = [0]
    near_point_rad4_np = [0]
    near_point_rad5_np = [0]
    # 車両の初期化 x座標, y座標, 角度, 角速度
    model_x = [0]
    model_y = [1]
    model_Phi = [0]
    model_Phi_dot = [0]
    kyori_np = [0]

    near_point_list = [0]
    course_x_list = [int(course_x[0])]
    course_y_list = [int(course_y[0])]
    now = 0

    last_point = len(course_x) - 1
    near_point_main = 0
    near_point2 = 0
    t = 0
    # 距離差初期化
    nearpoint_difference_mae = 10000
    nearpoint_difference_mae_2 = 10000
    nearpoint_difference_mae_3 = 10000
    nearpoint_difference_mae_4 = 10000
    nearpoint_difference_mae_5 = 10000
    kyori_mae = 10000

    #WANN用変数
    count = 0


    while math.sqrt((course_x[last_point] - model_x[now]) ** 2 + (course_y[last_point] - model_y[now]) ** 2) > 5 and (t + near_point_main) < last_point:

        #一番短いところからスタート
        kyori_point = t + near_point2
        kyori = math.sqrt((course_x[kyori_point] - model_x[now]) ** 2 + (course_y[kyori_point] - model_y[now]) ** 2)

        #WANN用に保存
        #指定したnearpointと今の距離の差　一番小さいところがnearpoint
        nearpoint_difference_2 = math.sqrt((near_point_2 - kyori)**2)
        nearpoint_difference_3 = math.sqrt((near_point_3 - kyori)**2)
        nearpoint_difference = math.sqrt((near_point_m - kyori)**2)
        nearpoint_difference_4 = math.sqrt((near_point_4 - kyori)**2)
        nearpoint_difference_5 = math.sqrt((near_point_5 - kyori)**2)

        if nearpoint_difference_2 > nearpoint_difference_mae_2 and count == 0:
            #ダミーnearpoint見つかれば保存
            near_point2 = kyori_point-1
            #print(nearpoint_difference_mae_2)
            count += 1
        else:
            nearpoint_difference_mae_2 = nearpoint_difference_2

        if nearpoint_difference_3 > nearpoint_difference_mae_3 and count == 1:
            #ダミーnearpoint見つかれば保存
            near_point3 = kyori_point-1
            #print(nearpoint_difference_mae_3)
            count += 1
        else:
            nearpoint_difference_mae_3 = nearpoint_difference_3

        if nearpoint_difference > nearpoint_difference_mae and count == 2:
            #nearpoint!!!見つかれば保存
            near_point_main = kyori_point-1
            #print(nearpoint_difference_mae)
            kyori_main = math.sqrt((course_x[near_point_main] - model_x[now]) ** 2 + (course_y[near_point_main] - model_y[now]) ** 2)
            count += 1
        else:
            nearpoint_difference_mae = nearpoint_difference

        if nearpoint_difference_4 > nearpoint_difference_mae_4 and count == 3:
            #ダミーnearpoint見つかれば保存
            near_point4 = kyori_point-1
            #print(nearpoint_difference_mae_4)
            count += 1
        else:
            nearpoint_difference_mae_4 = nearpoint_difference_4

        if nearpoint_difference_5 > nearpoint_difference_mae_5 and count == 4:
            #ダミーnearpoint見つかれば保存
            near_point5 = kyori_point-1
            #print(nearpoint_difference_mae_5)
            count += 1
        else:
            nearpoint_difference_mae_5 = nearpoint_difference_5




        # 実際の距離とnearpointの差が, 今までの距離との差よりも大きくなったら
        if nearpoint_difference_5 > nearpoint_difference_mae_5 and course_x[kyori_point-1] >= model_x[now]:
            #near_point = kyori_point-1
            print('near_point_main=',near_point_main)
            kyori_np.append(kyori_main)
            near_point_list.append(near_point_main)
            course_x_list.append(int(course_x[near_point_main]))
            course_y_list.append(int(course_y[near_point_main]))
            t = 0

            # 視野角計算
            near_point_rad = math.atan2(course_y[near_point_main] - model_y[now], course_x[near_point_main] - model_x[now]) - model_Phi[now]
            #near_point_deg = math.degrees(near_point_rad)
            near_point_rad2 = math.atan2(course_y[near_point2] - model_y[now], course_x[near_point2] - model_x[now]) - model_Phi[now]
            near_point_rad3 = math.atan2(course_y[near_point3] - model_y[now], course_x[near_point3] - model_x[now]) - model_Phi[now]
            near_point_rad4 = math.atan2(course_y[near_point4] - model_y[now], course_x[near_point4] - model_x[now]) - model_Phi[now]
            near_point_rad5 = math.atan2(course_y[near_point5] - model_y[now], course_x[near_point5] - model_x[now]) - model_Phi[now]

            #視野角を配列に追加
            near_point_rad_np.append(near_point_rad)
            near_point_rad2_np.append(near_point_rad2)
            near_point_rad3_np.append(near_point_rad3)
            near_point_rad4_np.append(near_point_rad4)
            near_point_rad5_np.append(near_point_rad5)


            now = now + 1
            # モデルによって, 次の車両の角速度を決定
            # model_Phi_dot[now] = Kp * near_point_rad
            model_Phi_dot.append(Kp * near_point_rad)
            # 角速度から次の車両角度を出す
            model_Phi.append(model_Phi[now - 1] + model_Phi_dot[now] * dt)

            # 車両角度から車両の座標を計算
            # model_x[now] = model_x[now - 1] + v * dt * math.cos(model_Phi)
            # model_y[now] = model_y[now - 1] + v * dt * math.sin(model_Phi)
            model_x.append(model_x[now - 1] + v * dt * math.cos(model_Phi[now]))
            model_y.append(model_y[now - 1] + v * dt * math.sin(model_Phi[now]))

            # 距離差初期化
            nearpoint_difference_mae = 10000
            nearpoint_difference_mae_2 = 10000
            nearpoint_difference_mae_3 = 10000
            nearpoint_difference_mae_4 = 10000
            nearpoint_difference_mae_5 = 10000
            count = 0
        else:
            #nearpoint_difference_mae = nearpoint_difference
            t = t + 1
            #kyori_mae = kyori

    #print(math.sqrt((course_x[last_point] - model_x[now])** 2 + (course_y[last_point] - model_y[now]) ** 2))
    main_df = pd.DataFrame({'x_cordinate': model_x, 'y_cordinate': model_y, 'Phi': model_Phi, 'Phi_dot': model_Phi_dot, 'kyori': kyori_np, 'near_point': near_point_list, 'course_x': course_x_list, 'course_y': course_y_list})
    WANN_df = pd.DataFrame({'near_point1_rad_{}m'.format(near_point_m): near_point_rad_np, 'near_point2_rad_{}m'.format(near_point_2): near_point_rad2_np, 'near_point3_rad_{}m'.format(near_point_3): near_point_rad3_np, 'near_point4_rad_{}m'.format(near_point_4): near_point_rad4_np, 'near_point5_rad_{}m'.format(near_point_5): near_point_rad5_np})
    return pd.merge(main_df, WANN_df, right_index=True, left_index=True)

# In[]:
test2 = One_Point_Model(course_x, course_y)
course_all = pd.read_csv('awazi_61_full.csv',
                         names=('A', 'B', 'C', 'D', 'E', 'F'))
test = pd.read_pickle('one_point_model_awazi61.pickle')
test2 = pd.read_pickle('one_point_model_awazi61_WANN0714.pickle')
pd.set_option('display.max_rows', 7000)
test2.head(100)

# In[]:
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.tick_params(which='both', direction='in',
                top=bool, right=bool, labelbottom=True)
ax1.set_xlim(0.0, 10000)
ax1.set_xlabel("x Coordinate")
# ax1.set_ylim(0, 2)
ax1.set_ylabel("y Coordinate")
ax1.grid()
ax1.plot(course_all['A'], course_all['B'], "-", color='red', lw=1)
ax1.plot(course_all['C'], course_all['D'], "-", color='black', lw=1)
ax1.plot(course_all['E'], course_all['F'], "-", color='black', lw=1)

# In[]:
# plot
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.tick_params(which='both', direction='in',
                top=bool, right=bool, labelbottom=True)
ax1.set_xlim(0.0, 10000)
ax1.set_xlabel("x Coordinate")
# ax1.set_ylim(0, 2)
ax1.set_ylabel("y Coordinate")
ax1.grid()
ax1.plot(course_all['A'], course_all['B'], "-", color='red', lw=1)
ax1.plot(test2['x_cordinate'], test2['y_cordinate'])

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
sub_axes.plot(test2['x_cordinate'], test2['y_cordinate'])


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
sub_axes2.plot(test2['x_cordinate'], test2['y_cordinate'])

# In[]:
plt.plot(course_all['A'], course_all['B'], "-", color='red')
#plt.plot(test['x_cordinate'], test['y_cordinate'])
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()

'''

終わり


'''
