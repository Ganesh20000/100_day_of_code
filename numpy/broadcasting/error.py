import numpy as np 

arr1 = np.array([[1,2,3],
            [4,6,5]])

arr2= np.array([1,2])

reshape2 = arr2.reshape(1,2,1)
print(reshape2)
print(reshape2.ndim)
reshape = arr1.reshape(2,3,1)
print(reshape.ndim)
print(reshape)
print("_"*50)

result = arr1+arr2
print(result)