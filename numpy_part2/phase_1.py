
import numpy as np

zero = np.zeros((3,3));
print(zero);

print("_"*30)
ones = np.ones((3,4))
print("once in python\n",ones);
print("_"*30)

fulls = np.full((2,3),5)
print("full values\n" ,fulls);

print("_"*30)

random =np.random.random((2,3))
print("full of random\n ",random)

print("_"*30)

number = np.arange(0,11,2)
print("arange", number); 

print("_"*30);

print("vector and matrix and tenosr ")


vector =np.array([1,2,3,4])
print(vector);
print("_"*30)
matrix = np.array([[1,2,3],
                   [2,3,3],
                   [4,5,6]])
print(matrix)
print("_"*30)

tensor = np.array([[[1,2,3],
                    [7,8,9],
                    [4.5,5,6],
                    [1,9,5]]])
print(tensor)
print("_"*30)

# array properties

print("shape",tensor.shape)
print("dimension",tensor.ndim)
print("size",tensor.size)
print("datatype",tensor.dtype)
print("_"*30)


# array reshaping 

arr = np.arange(18)
print(arr);


reshape = arr.reshape((6,3))
print(reshape)


print("_"*30) 

flatten = reshape.flatten()
print(flatten)

raveled  = arr.ravel()
print(raveled)
print("_"*50)

ravel = tensor.ravel()
print(ravel)
 
flatt = tensor.flatten()
print(flatt)
print("_"*50)


# transpose matrix


print(matrix)
print("_"*50)
trans = matrix.T
print(trans)