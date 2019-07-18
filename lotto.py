# Rekesh
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lotto_data_frame = pd.read_csv("http://web.eecs.utk.edu/~cosc505/data/lottonums.csv")

cols = list(lotto_data_frame.columns)
winn = lotto_data_frame.loc[:,cols[1]].get_values()
mega = lotto_data_frame.loc[:,cols[2]].get_values()
winn = np.asarray([list(map(int, string.split())) for string in list(winn.flat)])

# (rali1) Counts the multiples of a number within a dataset
def freq(data):
    count = []
    dmax = data.max()
    dmin = data.min()
    for dnum in range(dmin, dmax): # only counts within extrema
        count.append((data==dnum).sum()) 
    return count

fmega = freq(mega)
rmega = range(mega.min(), mega.max())

fwinn = freq(winn)
rwinn = range(winn.min(), winn.max())

plt.plot(rmega, fmega)
plt.plot(rwinn, fwinn)
plt.show()
