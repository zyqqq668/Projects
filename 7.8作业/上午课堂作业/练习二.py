import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("原数组：")
print(arr)

row2_col1_3 = arr[1, 0:3]
print("\n任务1 - 第2行1~3列：", row2_col1_3)

all_row_col3 = arr[:, 2]
print("任务2 - 全部行第3列：", all_row_col3)

odd_rows = arr[::2, :]
print("任务3 - 奇数行：")
print(odd_rows)