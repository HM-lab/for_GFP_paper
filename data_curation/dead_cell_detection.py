import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from PIL import Image
import time
import glob
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

start = time.time()

################################################
INPUT_directory = '/Users/katohisaaki/Desktop/GFP_paper/dead_cell'
channel_BF = "ch00"
channel_FP = "ch01"
channel_nucleus = "ch02"
temp = "30C"
FP = "Venus"
text = "311"
data_output = True
################################################

file_list = glob.glob(INPUT_directory+"/"+temp+"/"+FP+"/*"+text+"*"+channel_BF+".tif")
# print(file_list)
int_mode_arr = []
nuclues_max_arr = []
for filename in file_list:
    img_spot = np.array(Image.open(filename))
    # img_FP = np.array(Image.open(filename.replace(channel_BF,channel_FP)))
    img_nucleus = np.array(Image.open(filename.replace(channel_BF,channel_nucleus)))

    # arr_FP = []
    # for i in np.arange(1040):
    #     for n in np.arange(1392):
    #         a = img_FP[i][n][1]
    #         arr_FP.append(a)
    #
    # img_FP = np.array(arr_FP).reshape(1040,1392)

    # import seaborn as sns
    # sns.heatmap(img_FP)
    # plt.show()

    arr_nucleus = []
    for m in np.arange(1040):
        for o in np.arange(1392):
            b = img_nucleus[m][o][0]
            arr_nucleus.append(b)

    img_nucleus = np.array(arr_nucleus).reshape(1040,1392)

    # import seaborn as sns
    # sns.heatmap(img_nucleus)
    # plt.show()

    for l in np.arange(int(img_spot.max())-1):
        ###cell_sizeの計算###
        size_px = np.count_nonzero(img_spot==l+1)
        ####################

        if size_px < 1000:
            pass
        else:
            place = np.where(img_spot != l+1)
            # img_copy_FP = img_FP.copy()
            # img_copy_FP[place] = 0

            img_copy_nucleus = img_nucleus.copy()
            img_copy_nucleus[place] = 0

            # ###intensity_modeの計算###
            # int_mode = stats.mode(img_copy_FP[img_copy_FP != 0], axis=None)[0]
            # if len(int_mode) > 0:
            #     int_mode_arr.append(int_mode[0])
            # elif len(int_mode) == 0:
            #     int_mode_arr.append(0)
            # #########################

            ###nuclues_maxの計算###
            if not img_copy_nucleus[np.unravel_index(np.argmax(img_copy_nucleus), img_copy_nucleus.shape)] == 0:
                nuclues_max = max(img_copy_nucleus[img_copy_nucleus != 0])
                nuclues_max_arr.append(nuclues_max)
            else:
                nuclues_max_arr.append(0)
            ####################

# print(len(int_mode_arr))
print(len(nuclues_max_arr))

if data_output == True:
    Df = pd.DataFrame(nuclues_max_arr)
    # Df.columns = ["size","intensity"]
    Df.to_csv("/Users/katohisaaki/Desktop/GFP_paper/dead_cell_csv/dead_cell_"+temp+"_"+FP+"_"+text+".csv")

#
# ###########
# arr_zero = np.zeros(len(nuclues_max_arr))
# ###########
#
#
#
# array_2D = []
# # array_2D.append([int_mode_arr,nuclues_max_arr])
# array_2D.append([arr_zero,nuclues_max_arr])
# data = np.array(array_2D[0]).T
# # print(data)
# scaler = MinMaxScaler()
# data_norm = scaler.fit_transform(data)
# # print(data_norm)
#
# total_length = len(data_norm.T[1])
# dead_cell_num = np.count_nonzero(data_norm.T[1] > 0.05)
# live_cell_num = total_length - dead_cell_num
#
# print("live : dead = "+str(live_cell_num)+" : "+str(dead_cell_num))
#
# stop = time.time() - start
# print(stop)
# plt.hist(data_norm.T[1],bins=100, alpha=0.8)
# plt.axvline(x=0.05, color="red")
# # plt.plot(data_norm.T[1],data_norm.T[0], "o", alpha=0.8)
# # plt.xlabel("dead_cell_intensity")
# # plt.ylabel("FP_intensity")
# plt.show()
