import numpy as np



# 2d array 



arr = np.array([[1,2,3],
                [2,3,4],
                [8,0,7],
                [8,9,4]])

#row delete
arr_d1 = np.delete(arr,1,axis=0)
print(arr_d1)

arr_d2 = np.delete(arr,1,axis=1);
print(arr_d2)

# arr_d3 = np.delete(arr,2,axis=2)
# print(arr_d3)



print("_"*50)

arr = np.array([[[1,2,3],
                [2,3,4],
                [8,9,7],
                [8,9,4]]])





#for row  axis 1 
new_arr = np.delete(arr,1,axis=1)
print(new_arr)

# for column axis 2

new_arr2= np.delete(arr,1,axis=2)
print(new_arr2)