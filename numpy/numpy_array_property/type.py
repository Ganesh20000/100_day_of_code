import numpy as np
arr_1d = np.array([1, 2, 3])
arr_2d = np.array([[1, 2, 3], [1, 5, 6], [8, 4, 5]])
arr_3d = np.array(
    [[[1, 2, 3], [2, 6, 6], [2, 5.5, 6], [5, 8, 6], [8, 7, 8], [7, 8, 9], [1, 5, 6]]]
)


ff =arr_2d.astype(float)


print(ff)
print(ff.dtype)
print(ff.size)