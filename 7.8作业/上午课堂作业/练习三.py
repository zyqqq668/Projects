import numpy as np
np.random.seed(0)

A = np.random.randint(1, 6, size=(2, 3))
B = np.random.randint(1, 6, size=(2, 3))
print("A数组：")
print(A)
print("B数组：")
print(B)

elem_mul = A * B
print("\n逐元素乘法 A * B：")
print(elem_mul)

mat_mul = A @ B.T
print("\n矩阵乘法 A @ B.T：")
print(mat_mul)

mat = np.array([[1, 2], [3, 4]])
print("\n待求和矩阵：")
print(mat)
sum_col = np.sum(mat, axis=0)
sum_row = np.sum(mat, axis=1) 
print("按列求和(axis=0)：", sum_col)
print("按行求和(axis=1)：", sum_row)

float_arr = np.array([1.2, 3.5, 2.8])
mean_val = np.mean(float_arr)
std_val = np.std(float_arr)
round_arr = np.round(float_arr)
print("\n数组[1.2,3.5,2.8]计算结果：")
print("均值：", mean_val)
print("标准差：", std_val)
print("四舍五入：", round_arr)