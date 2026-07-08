import numpy as np
import timeit
np.random.seed(42)
#1
A = np.random.rand(1000, 2000)
B = np.random.rand(2000, 3000)

def f_dot():
    return np.dot(A, B)
def f_at():
    return A @ B
def f_matmul():
    return np.matmul(A, B)

t_dot = timeit.timeit(f_dot, number=1)
t_at = timeit.timeit(f_at, number=1)
t_matmul = timeit.timeit(f_matmul, number=1)

print(f"np.dot 耗时：{t_dot:.2f} s")
print(f"@ 运算符 耗时：{t_at:.2f} s")
print(f"np.matmul 耗时：{t_matmul:.2f} s")

#2
arr_c = np.random.rand(1000, 1000)
arr_f = np.asfortranarray(arr_c)

t_c_row = timeit.timeit(lambda: arr_c.sum(axis=1), number=10)
t_f_row = timeit.timeit(lambda: arr_f.sum(axis=1), number=10)
t_c_col = timeit.timeit(lambda: arr_c.sum(axis=0), number=10)
t_f_col = timeit.timeit(lambda: arr_f.sum(axis=0), number=10)

print("\n===== C/F内存布局求和速度 =====")
print(f"C数组 按行求和：{t_c_row:.3f}s")
print(f"F数组 按行求和：{t_f_row:.3f}s")
print(f"C数组 按列求和：{t_c_col:.3f}s")
print(f"F数组 按列求和：{t_f_col:.3f}s")

#3
A = np.random.rand(2000, 2000)
buf_square = np.empty_like(A)
buf_2a = np.empty_like(A)
result = np.empty_like(A)

np.multiply(A, A, out=buf_square)
np.multiply(2, A, out=buf_2a)
np.add(buf_square, buf_2a, out=result)
np.add(result, 1, out=result)

standard = A**2 + 2*A + 1
print("\n计算完成，最大误差：", np.max(np.abs(result - standard)))