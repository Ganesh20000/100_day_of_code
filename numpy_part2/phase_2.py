import numpy as np

val = np.arange(12)
print(val)


arr = val.reshape((3, 4))
print(arr)


print(val[2:7])

print("with step", val[0:10:2])


print("negative indexing", val[::-1])
print("_" * 50)

matrix = np.array([[1, 2, 3], [7, 5, 4], [8, 9, 6]])

print(matrix)

print(arr)
print("_" * 50)
# 2d array specifi element
print("specific no ", arr[2, 3])
print("specifi no ", arr[2, 2])
print("specific no is ", arr[1, 0])

print("_" * 50)

print("specific no is ", matrix[1, 1])
print("specific no is ", matrix[2, 2])

print("_" * 50)
# entire row target


print(arr[:, 2])
print(arr[:, 3])
print(matrix[:, 0])

print("sorting started")

unsort = np.array([5, 7, 8, 9, 4, 2, 3, 0, 1, 8, 3, 10])

ars = np.sort(unsort)
print(ars)

print("_" * 50)

arr_2d = np.array([[3, 1], [1, 2], [2, 3]])
print(arr_2d)

sort_2d = np.sort(arr_2d, axis=0)
print(sort_2d)

print("_" * 50)


#filter in numpy
number = np.arange(11)
print(number)

even = number[number % 2 == 0]

odd = number[number>2];
print("grather than 2 ",odd)
print(even)

mask= number>5
print("number greater than 5 are",number[mask])
print("_"*50)

print(matrix)
mask_2 = matrix>7
print("grather than7 ",matrix[mask_2])
print("_"*50)
#fancy indexing and np.where 
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr[[2,3,5]])
print("_"*50)
indices =[2,3,5]
print(arr[indices])

#where result 
print("_"*50)
where_result = np.where(arr>=8)
print("where clause",arr[where_result])

print("_"*50)
#condiiton array 

num = np.arange(20)
print(num)
condition = np.where(num>5, num*2,num)
print(condition)
print("_"*50)
con2 = np.where(num>15 ,"true","false")
print(con2)
print("_"*50)
# adding and removing data

arr1 = np.array([1,2,3])
arr2=np.array([2,5,6])

combined =np.concatenate((arr1, arr2))
print(combined)

com = np.concatenate((num,number))
print(com)