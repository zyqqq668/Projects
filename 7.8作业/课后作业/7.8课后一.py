import numpy as np
import matplotlib.pyplot as plt

#创建1D、2D、3D随机数组
np.random.seed(0)
arr1d = np.random.randint(1, 20, size=8)             
arr2d = np.random.randint(1, 10, size=(4, 4))           
arr3d = np.random.rand(2, 3, 3)                         
print("一维数组：", arr1d)
print("二维数组：\n", arr2d)
print("三维数组形状：", arr3d.shape)

#索引、切片操作
print("\n=== 索引切片 ===")
print("一维数组前5个元素：", arr1d[:5])
print("二维数组第2行全部元素：", arr2d[1, :])
print("二维数组所有行第3列：", arr2d[:, 2])
print("二维左上角2×2子矩阵：\n", arr2d[:2, :2])

#形状变换
flat_arr = arr2d.flatten()
reshape_arr = flat_arr.reshape(2, 8)
arr_T = arr2d.T
print("\n二维展平：", flat_arr)
print("重塑(2,8)：\n", reshape_arr)
print("二维矩阵转置：\n", arr_T)

#封装矩阵基础运算函数
def mat_add(m1, m2):
    return m1 + m2

def mat_elem_mul(m1, m2):
    return m1 * m2

def mat_dot(m1, m2):
    return m1 @ m2

def mat_trans(m):
    return m.T

A = np.random.randint(1, 5, (2, 2))
B = np.random.randint(1, 5, (2, 2))
print("\n=== 矩阵运算 ===")
print("矩阵A：\n", A)
print("矩阵B：\n", B)
print("A+B：\n", mat_add(A, B))
print("逐元素相乘：\n", mat_elem_mul(A, B))
print("矩阵乘法：\n", mat_dot(A, B))

#随机数据统计分析
rand_data = np.random.normal(10, 3, size=500)
print("\n=== 随机数据统计 ===")
print("均值：", round(np.mean(rand_data), 2))
print("方差：", round(np.var(rand_data), 2))
print("标准差：", round(np.std(rand_data), 2))
print("最大值、最小值：", np.max(rand_data), np.min(rand_data))

plt.figure(figsize=(6,3))
plt.hist(rand_data, bins=30)
plt.title("随机正态数据分布")
plt.show()