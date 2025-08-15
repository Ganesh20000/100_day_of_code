import numpy as np 

matrix = np.array([[1,2,3],[4,5,6]])
vector = np.array([7,8,9]);

result = matrix+vector;

print(result)

# Broadcasting in NumPy allows us to perform arithmetic operations on arrays of different shapes without reshaping them.