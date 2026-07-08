import numpy as np
np.random.seed(0)

arr = np.random.randint(0, 10, size=(3, 4))
print("Original array:")
print(arr)

reshaped_arr = arr.reshape(4, 3)
print("\nReshaped array (4,3):")
print(reshaped_arr)

filtered_arr = arr[arr > 5]
print("\nFiltered array (elements greater than 5):")
print(filtered_arr)