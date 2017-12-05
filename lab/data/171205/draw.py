import os
import math
import csv

import numpy as np
from scipy import signal
from scipy.interpolate import spline
from scipy.optimize import curve_fit
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
import matplotlib

dfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/YaHei Consolas Hybrid.ttf')

root = 'lab/data/171205/200v10p150mm2cm14defects'

with open(os.path.join(root, '07.csv')) as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
rows = np.array(rows[2:])[:,:3].astype('float64')
t = 0.5 * rows[:, 0]
r = 1000 * rows[:, 1]
s = 1000 * rows[:, 2]

# 通过找最大值决定群速度计算终止时间的计算
max = 0
for i in range(394*2):
    if max < s[i]:
        max = s[i]
print(max)

plt.plot(t, s)
#plt.plot(t, r)
plt.title('signal', fontproperties=dfont)
plt.xlabel('time/us', fontproperties=dfont)
plt.ylabel('Volt/mV', fontproperties=dfont)
plt.show()