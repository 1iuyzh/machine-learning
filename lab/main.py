import numpy as np
# 材料参数
# E1 E2 E3 G12 G13 G23 v12 v13 v23 p
p = np.array([155, 7.6, 7.6, 4.32, 4.32, 3.23, 0.344, 0.344, 0.344, 1.678])
# 单层矩阵
C0 = np.array([
    [1/p[0], -p[6]/p[0], -p[7]/p[0], 0, 0, 0],
    [-p[6]/p[0], 1/p[1], -p[8]/p[1], 0, 0, 0],
    [-p[7]/p[0], -p[8]/p[1], 1/p[2], 0, 0, 0],
    [0, 0, 0, 1/p[5], 0, 0],
    [0, 0, 0, 0, 1/p[4], 0],
    [0, 0, 0, 0, 0, 1/p[3]]])
a = np.array([])