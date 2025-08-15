import numpy as np

# arr = np.array([1,2,3,4,5,6,7,8,9])

arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr.ndim)
print(arr)
# 2d convert
reshape_arr = arr.reshape(3,3)
print(reshape_arr);

print(reshape_arr.ndim);

print("_"*50)

reshape_arr_3d = arr.reshape(3,3,1);

print(reshape_arr_3d)
print(reshape_arr_3d.ndim)
print("_"*50)
s = np.reshape(arr,(3,3))
print(s)

o = np.arange(12)


print(o)
s = np.reshape(o,(4,3))
print(s)