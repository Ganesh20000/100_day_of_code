import numpy as np

arr_1d = np.array([1, 2, 3])
arr_2d = np.array([[1, 2, 3], [1, 5, 6], [8, 4, 5]])
arr_3d = np.array(
    [[[1, 2, 3], [2, 6, 6], [2, 5.5, 6], [5, 8, 6], [8, 7, 8], [7, 8, 9], [1, 5, 6]]]
)

print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)

print("_"*50)
print(arr_1d.shape)
print(arr_2d.shape)
print(arr_3d.shape)
print("_"*50)
print(arr_1d.dtype)
print(arr_2d.dtype)
print(arr_3d.astype(int))
print("_"*50)
print(arr_1d.size)
print(arr_2d.size)
print(arr_3d.size)

print("_"*50)
print(arr_2d.astype(int))