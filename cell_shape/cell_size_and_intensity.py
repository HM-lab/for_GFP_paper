import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from PIL import Image
import time
import glob
import pandas as pd

start = time.time()

################################################
INPUT_directory = '/Users/katohisaaki/Desktop/Pyworks/size_intensity'
channel_BF = "ch00"
channel_FP = "ch01"
text = "_Y"
data_output = True
################################################

file_list = glob.glob(INPUT_directory+"/*"+text+"*"+channel_BF+".tif")
int_mode_arr = []
size_arr = []
for filename in file_list:
    img_spot = np.array(Image.open(filename))
    img_FP = np.array(Image.open(filename.replace(channel_BF,channel_FP)))

    arr = []
    for i in np.arange(1040):
        for n in np.arange(1392):
            a = img_FP[i][n][1]
            arr.append(a)

    img_FP = np.array(arr).reshape(1040,1392)


    for l in np.arange(int(img_spot.max())-1):
        place = np.where(img_spot != l+1)
        img_copy = img_FP.copy()
        img_copy[place] = 0

        ###intensity_modeの計算###
        int_mode = stats.mode(img_copy[img_copy != 0], axis=None)[0]
        if len(int_mode) > 0:
            int_mode_arr.append(int_mode[0])
        elif len(int_mode) == 0:
            int_mode_arr.append(0)
        #########################

        ###cell_sizeの計算###
        size_px = np.count_nonzero(img_spot==l+1)
        size_arr.append(size_px)
        ####################

print(len(int_mode_arr))
# print(len(size_arr))

if data_output == True:
    Df = pd.concat([pd.DataFrame(size_arr),pd.DataFrame(int_mode_arr)],axis=1,sort=False)
    Df.columns = ["size","intensity"]
    Df.to_csv("cell_size_intensity_"+text+".csv")


plt.plot(size_arr,int_mode_arr,"o", alpha=0.8)
plt.show()
stop = time.time() - start
print(stop)
