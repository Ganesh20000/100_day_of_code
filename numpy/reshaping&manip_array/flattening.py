import numpy as np

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

print(arr.ndim)

print(arr.ravel())
print(arr.flatten())


print("_"*50)
flat1 = arr.ravel()
flat2 =arr.flatten()

print(flat1);
print(flat2)

flat1[5]=60;
print(flat1)

flat2[5]=100;
print(flat2)


