import numpy as np
np.random.seed(0)

rand_float = np.random.rand(10)
print("原始0~1浮点数组：")
print(rand_float)

arr_min = rand_float.min()
arr_max = rand_float.max()
norm_arr = (rand_float - arr_min) / (arr_max - arr_min) * 100
print("\n归一化到[0,100]数组：")
print(norm_arr)

cumsum_arr = np.cumsum(norm_arr)
print("\n累计和 cumsum：")
print(cumsum_arr)

cummax_arr = np.maximum.accumulate(norm_arr)
print("\n累计最大值 cummax：")
print(cummax_arr)