import numpy as np

val= np.arange(12)
print(val)


arr = val.reshape((3,4))
print(arr);



print(val[2:7])

print("with step",val[0:10:2])


print("negative indexing", val[::-1])
print("_"*50)

matrix= np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

print(matrix)

print(arr)
print("_"*50)
#2d array specifi element
print("specific no " ,arr[2,3])
print("specifi no ",arr[2,2])
print("specific no is ", arr[1,0])

print("_"*50)

print("specific no is ", matrix[1,1])
print("specific no is ", matrix[2,2])

print("_"*50)
# entire row target 


print(arr[:,2])
print(arr[:,3])
print(matrix[:,0])

print("sorting started")

unsort = np.array([5,7,8,9,4,2,3,0,1,8,3,10])

ars = np.sort(unsort)
print(ars)